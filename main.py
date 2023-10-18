import web
from web import form

PORT = 8080

web.config.debug = True

render = web.template.render('templates')

URLS = ("/", "index",
        "/lista", "lista",
        "/articulo", "articulo",
        "/sumar", "sumar",
        "/restar", "restar")

class index():
    
    def GET(self):
        return render.index()
    
class restar():

    def GET(self):
        input=web.input()
        id=input.id
        db = web.database(dbn='mysql', host='192.168.1.100', db='produccion', user='remote', password='flores01')
        data = db.select('produccion.publicaciones',where="idpublicacion = "+id,what="megusta")
        megustaanterior = int(data[0]['megusta'])
        db.update('produccion.publicaciones', where="idpublicacion = "+id, megusta = megustaanterior - 1)
        data = db.select('produccion.publicaciones',where="idpublicacion = "+id)
        data_list = list(data)
        db.ctx.db.close()
        return render.articulo(data_list)
    
    
class sumar():

    def GET(self):
        input=web.input()
        id=input.id
        db = web.database(dbn='mysql', host='192.168.1.100', db='produccion', user='remote', password='flores01')
        data = db.select('produccion.publicaciones',where="idpublicacion = "+id,what="megusta")
        megustaanterior = int(data[0]['megusta'])
        db.update('produccion.publicaciones', where="idpublicacion = "+id, megusta = megustaanterior +1)
        data = db.select('produccion.publicaciones',where="idpublicacion = "+id)
        data_list = list(data)
        db.ctx.db.close()
        return render.articulo(data_list)

class articulo():
    
    def GET(self):
        input=web.input()
        id=input.id
        db = web.database(dbn='mysql', host='192.168.1.100', db='produccion', user='remote', password='flores01')
        data = db.select('produccion.publicaciones',where="idpublicacion = "+id)
        data_list = list(data)
        db.ctx.db.close()
        return render.articulo(data_list)

class lista():

    def GET(self):
        db = web.database(dbn='mysql', host='192.168.1.100', db='produccion', user='remote', password='flores01')
        data = db.select('produccion.publicaciones')
        data_list = list(data)
        db.ctx.db.close()
        return render.lista(data_list) 


app = web.application(URLS, globals())

if __name__ == "__main__":
    app.run()
