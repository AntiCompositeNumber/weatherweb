#!/usr/bin/env python2

import json
from datetime import datetime
import subprocess
import web
import rrdtool
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
rrdPath = 'weatherweb.rrd'
render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/api/current', 'currentAPI',
    '/api/day', 'dayAPI'
    )

class index:
    def GET(self):
        return render.index()

class currentAPI:
    def GET(self):
        lastUpdate = rrdtool.lastupdate(rrdPath)
        current = {"date":datetime.isoformat(lastUpdate["date"]) + "Z", "temp":round(lastUpdate["ds"]["temp"], 1), "humidity":round(lastUpdate["ds"]["humidity"], 0)}
        currentJSON = json.dumps(current)
        return currentJSON
class dayAPI:
    def GET(self):
        lastDay = subprocess.check_output("/home/alarm/git/weatherweb/day.sh")
        return lastDay

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
