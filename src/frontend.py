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

bp = flask.Blueprint("frontend", __name__, url_prefix="")


@bp.route("/")
def index():
    return flask.render_template("index.html")


@bp.route("/current")
def current():
    return flask.render_template("current.html")


@bp.route("/devices")
def devices():
    return flask.render_template("devices.html")


@bp.route("/devices/aircon")
def air_conditioner():
    return flask.render_template("kenmore_simple.html")
