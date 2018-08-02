#!/usr/bin/python2

import web
import rrdtool
import json
from datetime import datetime
import subprocess 

rrdPath='/home/alarm/git/weatherweb/weatherweb.rrd'
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
    lastDay = subprocess.call("rrdtool xport DEF:wwt=" + rrdPath + ":temp:AVERAGE DEF:wwh=" + rrdPath + ":humidity:AVERAGE XPORT:wwt:temp XPORT:wwh:humidity --json --showtime") 
    return lastDay

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()


