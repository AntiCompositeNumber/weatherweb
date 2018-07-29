#!/usr/bin/python2

import web
import rrdtool

render = web.template.render('templates/')

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        lastUpdate = rrdtool.lastupdate("weatherweb.rrd")
        temp = lastUpdate["temp"]
        humidity = lastUpdate["humidity"]
        updateTime = lastUpdate["date"]
        return render.index(temp,humidity,updateTime)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


