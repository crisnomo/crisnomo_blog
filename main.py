import web
from web import form

PORT = 8080

web.config.debug = True
render = web.template.render('templates')

URLS = ("/", "index")

class index():
    
    def GET(self):
        return render.index()
    


app = web.application(URLS, globals())

if __name__ == "__main__":
    app.run()
