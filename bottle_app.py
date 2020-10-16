# A very simple Bottle Hello World app for you to get started with...
#from bottle import default_app

from bottle import get, post, template,request,redirect
import sqlite3
import os


#check which envi we are running the application dev or prod
ON_PYTHONANYWHERE =  "PYTHONANYWHERE_DOMAIN" in os.environ
#assert ON_PYTHONANYWHERE ==True


if ON_PYTHONANYWHERE:
    #on PA,set up to connect the WSGI server
    from bottle import default_app
else:
    #dev envi import run and debug
    from bottle import run,debug

#list all the DB functions
from storage import get_items, get_item, update_status,create_item,update_item,delete_item

@get('/')
def get_show_list():
   result =get_items()
   return template("show_list.tpl",rows=result)


@get('/new_item')
def get_new_item():
    return template("new_item.tpl")


#create a POST handler
@post("/new_item")
def post_new_item():
    new_item  = request.forms.get("new_item").strip()
    create_item(new_item,1)
    redirect("/")#redirect to home page


#update
@get("/update_item/<id:int>")
def get_update_item(id):
    result = get_item(id)
    return template("update_item", row=result)

@post("/update_item")
def post_update_item():
    id = int(request.forms.get("id").strip())
    updated_item = request.forms.get("updated_item").strip()
    update_item(id,updated_item)
    redirect("/")


@get("/set_status/<id:int>/<value:int>")
def get_set_status(id, value):
    update_status(id,value)
    redirect("/")


@get("/delete_item/<id:int>")
def get_delete_item(id):
    delete_item(id)
    redirect("/")#redirect to home page


if ON_PYTHONANYWHERE:
    application= default_app()
else:
    #dev envi run localhost
    debug(True)
    run(host='localhost', port=8080)


