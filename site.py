#!/usr/bin/python2

import web

render = web.template.render('templates/')

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        temp = 72
        humidity = 23
        return render.index(temp,humidity)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


