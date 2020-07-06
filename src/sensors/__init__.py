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
import abc
from typing import NamedTuple, Optional, Iterator, List


class Condition(NamedTuple):
    temperature: float
    humidity: float
    timestamp: datetime.datetime
    sensor: "Sensor"


class Sensor(abc.ABC):
    def __init__(self, **kwargs):
        self.sensor_type = kwargs["sensor_type"]
        self.location = kwargs["location"]

    @property
    @abc.abstractmethod
    def current(self) -> Condition:
        pass

    @abc.abstractmethod
    def hisorical(
        self,
        timestamp: datetime.datetime,
        variance: Optional[datetime.timedelta] = None,
        resolution: str = "",
    ) -> Condition:
        pass

    @abc.abstractmethod
    def range(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        resolution: str = "",
    ) -> Iterator[Condition]:
        pass


class Sensors:
    sensors: List[Sensor] = []

    @classmethod
    def register(cls, sensor):
        cls.sensors.append(sensor)



