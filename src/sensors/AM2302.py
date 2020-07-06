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

import datetime
from . import Sensor, Condition
from typing import Optional, Iterator


class AM2302(Sensor):
    def __init__(self, sensor_type, location):
        self.sensor_type = sensor_type
        self.location = location
        self.writable = True

    def current(self):
        pass

    def hisorical(
        self,
        timestamp: datetime.datetime,
        variance: Optional[datetime.timedelta] = None,
        resolution: str = "",
    ) -> Condition:
        pass

    def range(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        resolution: str = "",
    ) -> Iterator[Condition]:
        pass

    def write(self):
        pass

    def run(self):
        pass
