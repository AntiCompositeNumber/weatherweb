#! /usr/bin/env python

import rrdtool

#This python3 script creates a new rrdtool database
#It expects data in Fahrenheit and % every 1 minute.
#Data is stored at 1 minute intervals for 1 week,
#then at 10 minute intervals for six  months. 

rrdtool.create(
        "weatherweb.rrd",
        "--start", "N",
        "--step", "1m",
        "DS:temp:GAUGE:120:-40.1:177",
        "DS:humidity:GAUGE:2m:0:100",
        "RRA:AVERAGE:0.5:1m:1w",
        "RRA:AVERAGE:0.5:10m:6M",
        "RRA:AVERAGE:0.5:1h:5y"
        )
