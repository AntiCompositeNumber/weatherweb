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
import os
import subprocess
import logging
import json


# Set up logging
logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s:%(message)s",
    level=logging.DEBUG,
    # filename="app.log",
)
logger = logging.getLogger(__name__)


def create_app():
    # Load Flask config
    app = flask.Flask(__name__)
    try:
        with open(
            os.path.realpath(os.path.join(os.path.dirname(__file__), "../config.json"))
        ) as f:
            conf = json.load(f)
            app.config.update(conf.get("flask", ""))
    except FileNotFoundError:
        pass
    app.config.setdefault(
        "data_dir", os.path.realpath(os.path.join(os.path.dirname(__file__), "../data"))
    )
    # Put the short hash of the current git commit in the config
    rev = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        universal_newlines=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    app.config["version"] = rev.stdout

    from . import frontend, api

    app.register_blueprint(frontend.bp)
    app.register_blueprint(api.bp)

    return app


app = create_app()
