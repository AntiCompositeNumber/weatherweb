#!/bin/bash

/usr/bin/rrdtool xport \
	DEF:wwt=weatherweb.rrd:temp:AVERAGE \
	DEF:wwh=weatherweb.rrd:humidity:AVERAGE \
	XPORT:wwt:temp \
	XPORT:wwh:humidity \
	--json --showtime
