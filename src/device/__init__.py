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

import subprocess
from typing import Callable

Devices = []


class Device:
    pass


class IRDevice(Device):
    def __init__(self, ir_device: str = "/dev/lirc0"):
        self.ir_device = ir_device

    def transmit(self, keycode: str):
        cmd = [
            "ir-ctl",
            "--dev",
            self.ir_device,
            "--keymap",
            self.keymap,
            "--keycode",
            keycode,
        ]
        subprocess.run(cmd, check=True)

    def _closest_bound(self, value: int, low: int, high: int) -> int:
        if low > value or high < value:
            raise ValueError(value)
        if value - low <= high - value:
            return low
        else:
            return high

    def _set_to_value(self, current: int, target: int, set_func: Callable) -> int:
        if current > target:
            action = "down"
        elif current < target:
            action = "up"
        else:
            return current
        diff = abs(current - target)
        for i in range(diff):
            set_func(action)
        return target

    def _ensure(self, target: int, low: int, high: int, set_func: callable) -> int:
        bound = self._closest_bound(target, low, high)
        if bound == low:
            self._set_to_value(current=high, target=low, set_func=set_func)
        elif bound == high:
            self._set_to_value(current=low, target=high, set_func=set_func)
        else:
            raise ValueError
        return self._set_to_value(current=bound, target=target, set_func=set_func)


class UnknownStateError(Exception):
    pass
