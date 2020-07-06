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

import rrdtool
from . import Sensor


class RrdSensor(Sensor):
    def __init__(self, **kwargs):
        self.writable: bool = True
        self.rrd_file: str = kwargs["rrd_file"]

    def write(self):
        pass

    def create(self):
    def exists(self):
        try:
            f = open(self.rrd_file)
        except FileNotFoundError:
            return False

        f.close()
        try:
            rrdtool.info(self.rrd_file)
        except rrdtool.OperationalError as err:
            raise FileNotFoundError:


