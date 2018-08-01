#!/usr/bin/python2

import web
import rrdtool
import json
from datetime import datetime

render = web.template.render('templates/')

urls = (
  '/', 'index',
  '/api/current', 'currentAPI'
)

class index:
  def GET(self):
     return render.index()

class currentAPI:
  def GET(self):
    lastUpdate = rrdtool.lastupdate("weatherweb.rrd")
    current = {"date":datetime.isoformat(lastUpdate["date"]) + "Z", "temp":round(lastUpdate["ds"]["temp"], 1), "humidity":round(lastUpdate["ds"]["humidity"], 0)}
    currentJSON = json.dumps(current) 
    return currentJSON

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()


