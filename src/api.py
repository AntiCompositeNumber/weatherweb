#!/usr/bin/env python3
# coding: utf-8
# SPDX-License-Identifier: Apache-2.0


# Copyright 2020 AntiCompositeNumber

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import flask
from src import device
from src.device import kenmore
from flask_restx import Api, Resource  # type: ignore


bp = flask.Blueprint("api", __name__, url_prefix="/api")
api = Api(bp, prefix="/v1")


@api.route("/conditions")
class Conditions(Resource):
    def get(self):
        return


@api.route("/devices")
class Devices(Resource):
    def get(self):
        return device.Devices


@api.route("/device/kenmore/<prop>")
class Kenmore(Resource):
    dev = kenmore.KenmoreAC(power=True, mode="cool", temp=75, fan=-1)

    def get(self, prop):
        if prop == "mode":
            if self.dev.power:
                return self.dev.mode
            else:
                return self.dev.power
        elif prop == "temp":
            if self.dev.temp:
                return self.dev.temp
            else:
                return None
        elif prop == "fan":
            if self.dev.fan > 0:
                return self.dev.fan
            elif self.dev.fan == -1:
                return "auto"
            else:
                return None
        elif prop == "timer":
            return self.dev.timer
        elif prop == "all":
            return {
                "mode": self.dev.mode if self.dev.power else self.dev.power,
                "temp": self.dev.temp,
                "fan": self.dev.fan,
                "timer": self.dev.timer,
            }

    @api.param("data", _in="formData")
    def post(self, prop):
        data = flask.request.form["data"]
        if prop == "mode":
            if data == "off":
                self.dev.set_power("set", False)
            elif data in ("cool", "energy_saver", "fan_only"):
                if not self.dev.power:
                    self.dev.set_power("set", True)
                self.dev.set_mode(data)
            else:
                flask.abort(400)
            return self.dev.mode if self.dev.power else self.dev.power
        elif prop == "temp":
            if data in ("up", "down"):
                self.dev.set_temp(data)
            else:
                self.dev.set_temp("set", int(data))
            return self.dev.temp
        elif prop == "fan":
            if data in ("up", "down", "auto"):
                self.dev.set_fan(data)
            else:
                self.dev.set_fan("set", int(data))
            return self.dev.temp
        elif prop == "timer":
            return NotImplemented


@api.route("/device/kenmore/simple/<btn>")
class KenmoreSimple(Resource):
    dev = kenmore.KenmoreAC()

    def post(self, btn):
        if btn == "power":
            self.dev.set_power("toggle")
        elif btn == "timer":
            self.dev.set_timer("toggle")
        elif btn == "fan_up":
            self.dev.set_fan("up")
        elif btn == "fan_down":
            self.dev.set_fan("down")
        elif btn == "temp_up":
            self.dev.set_temp("up")
        elif btn == "temp_down":
            self.dev.set_temp("down")
        elif btn == "cool":
            self.dev.set_mode("cool")
        elif btn == "energy_saver":
            self.dev.set_mode("energy_saver")
        elif btn == "fan_only":
            self.dev.set_mode("fan_only")
        elif btn == "auto_fan":
            self.dev.set_fan("auto")
        elif btn == "sleep":
            self.dev.set_sleep("toggle")
