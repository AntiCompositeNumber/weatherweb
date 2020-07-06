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


from typing import Optional, List
import itertools
from src.device import IRDevice, Devices, UnknownStateError

AUTO = -1


class KenmoreAC(IRDevice):
    controllable: bool = True
    exclusive: bool = True
    max_temp: int = 90
    min_temp: int = 60
    max_fan: int = 3
    min_fan: int = 1
    timer_values: List[float] = list(
        itertools.chain(
            [x / 2 for x in range(1, 19)], [float(x) for x in range(10, 25)]
        )
    )
    keymap = "/etc/rc_keymaps/kenmore.toml"
    power: Optional[bool] = None
    mode: str = ""
    fan: int = 0
    temp: int = 0
    timer: Optional[float] = None
    sleep: Optional[bool] = None

    def __init__(
        self,
        exclusive: bool = True,
        power: Optional[bool] = None,
        mode: str = "",
        fan: int = 0,
        temp: int = 0,
        timer: Optional[float] = None,
        sleep: Optional[bool] = None,
        **kwargs,
    ) -> None:
        self.exclusive = exclusive
        if power is not None:
            self.power = power
        if mode != "":
            self.mode = mode
        if fan:
            self.fan = fan
        if temp:
            self.temp = temp
        if timer is not None:
            self.timer = timer
        if sleep is not None:
            self.sleep = sleep

        super().__init__(**kwargs)

    def set_power(self, action: str = "toggle", value: Optional[bool] = None) -> None:
        if not self.exclusive and action != "toggle":
            raise UnknownStateError
        elif action == "toggle":
            self.transmit("KEY_POWER")
            if self.power is not None:
                self.power = not self.power
        elif action == "set":
            if value is None:
                raise TypeError
            if self.power is None:
                raise UnknownStateError
            elif self.power ^ value:
                self.transmit("KEY_POWER")
                self.power = value
        else:
            raise KeyError(f"action must be one of 'toggle', 'set', not '{action}'")

    def set_mode(self, value: str):
        modes = {
            "cool": "KEY_PLAY",
            "energy_saver": "KEY_SLOW",
            "fan_only": "KEY_PAUSE",
        }
        self.transmit(modes[value])
        self.mode = value

    def set_fan(self, action: str, value: int = 0, ensure: bool = False):
        if action == "up":
            self.transmit("KEY_VOLUMEUP")
            if self.fan > 0:
                if self.fan < self.max_fan:
                    self.fan += 1
            else:
                self.fan = 0
        elif action == "down":
            self.transmit("KEY_VOLUMEDOWN")
            if self.fan > 0:
                if self.fan > self.min_fan:
                    self.fan -= 1
            else:
                self.fan = 0
        elif action == "auto":
            self.transmit("KEY_SHUFFLE")
            self.fan = AUTO
        elif action == "set":
            if value < self.min_fan or value > self.max_fan:
                raise ValueError
            if ensure or self.fan < 1:
                self.fan = self._ensure(value, self.min_fan, self.max_fan, self.set_fan)
            else:
                self.fan = self._set_to_value(self.fan, value, self.set_fan)
        else:
            raise KeyError

    def set_temp(self, action: str, value: int = 0, ensure: bool = False):
        if action == "up":
            self.transmit("KEY_UP")
            if self.temp > 0:
                if self.temp < self.max_temp:
                    self.temp += 1
            else:
                self.temp = 0
        elif action == "down":
            self.transmit("KEY_DOWN")
            if self.temp > 0:
                if self.temp > self.min_temp:
                    self.temp -= 1
            else:
                self.temp = 0
        elif action == "set":
            if value < self.min_temp or value > self.max_temp:
                raise ValueError
            if ensure or self.temp < 1:
                self.temp = self._ensure(
                    value, self.min_temp, self.max_temp, self.set_temp
                )
            else:
                self.temp = self._set_to_value(self.temp, value, self.set_temp)
        else:
            raise KeyError

    def set_timer(self, action: str, value: float = 0.0):
        value = float(value)
        if action == "up":
            self.transmit("KEY_UP")
            self.timer = self.timer_values[self.timer_values.index(value) + 1]
        elif action == "down":
            self.transmit("KEY_DOWN")
            self.timer = self.timer_values[self.timer_values.index(value) - 1]
        elif action == "commit":
            self.set_mode(self.mode)
        elif action == "toggle":
            self.transmit("KEY_TIME")
            if self.timer is not None:
                if self.timer == 0.0:
                    self.timer = 0.5
                else:
                    self.timer = 0.0
        elif action == "set":
            self.set_timer("toggle")
            for i in range(self.timer_values.index(float(value))):
                self.set_timer("up")
            self.set_timer("commit")
        else:
            raise KeyError(action)

    def set_sleep(self, action: str, value: Optional[bool] = None):
        if not self.exclusive and action != "toggle":
            raise UnknownStateError
        elif action == "toggle":
            self.transmit("KEY_SLEEP")
            if self.sleep is not None:
                self.sleep = not self.sleep
        elif action == "set":
            if value is None:
                raise TypeError
            if self.sleep is None:
                raise UnknownStateError
            elif self.sleep ^ value:
                self.transmit("KEY_POWER")
                self.sleep = value
        else:
            raise KeyError(action)


Devices.append(KenmoreAC)
