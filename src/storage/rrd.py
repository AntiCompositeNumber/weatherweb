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


"""Pythonic wrapper around python-rrdtool"""
import rrdtool
import datetime
from typing import Optional, Union, Sequence, NamedTuple, Tuple


class RRD:
    pass


class RrdLastUpdate(NamedTuple):
    date: datetime.datetime
    row: Tuple[Optional[float]]


class Gauge(RRD):
    """A single-source gauge round-robin database"""

    def __init__(self, rrd_file: str, keys: Sequence[str] = []) -> None:
        self.rrd_file = rrd_file
        self.keys = keys
        self.row = NamedTuple("GaugeRow", [(key, Optional[float]) for key in keys])

    def create(self, start: Optional[datetime.datetime] = None) -> None:
        pass

    def info(self) -> dict:
        pass

    def update(self, *values, timestamp: Union[datetime.datetime, str] = "N") -> None:
        if len(values) == 1 and isinstance(values[0], tuple):
            args = list(values[0])
        else:
            args = values
        if isinstance(timestamp, datetime.datetime):
            args.insert(0, datetime.timestamp())
        rrdtool.update(self.rrd_file, ":".join(str(arg) for arg in args))

    def lastupdate(self) -> RrdLastUpdate:
        args = [self.rrd_file]
        if self.daemon:
            args.extend(["--daemon", self.daemon])
        data = rrdtool.lastupdate(*args)
        return RrdLastUpdate(date=data["date"], row=self.row._make(data["ds"].values()))

    @property
    def now(self):
        lu = self.lastupdate()
        if (datetime.datetime.now() - lu.date) > datetime.timedelta(
            seconds=self.step * 2
        ):
            raise ValueError
        return lu.row

    @now.setter
    def now(self, values):
        self.update(*values)
