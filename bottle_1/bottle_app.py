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


@get('/')
def get_show_list():
   connection = sqlite3.connect("todo.db")
   cursor = connection.cursor()
   cursor.execute("select * from todo")
   result = cursor.fetchall()
   cursor.close() #close the cursor, use 1 cursor per transaction.
  # return str(result)
   return template("show_list.tpl",rows=result)


@get('/new_item')
def get_new_item():
    return template("new_item.tpl")


#create a POST handler
@post("/new_item")
def post_new_item():
    #we are getting a request that has information that needs to be saved
    new_item = request.forms.get("new_item").strip() #strip is used to remove white spaces
    connection = sqlite3.connect("todo.db")
    cursor= connection.cursor()
    cursor.execute("insert into todo (task, status) values (?,?)", (new_item, 1))
    #cursor.lastrowid #gives the last row id
    connection.commit() #commit to the database
    cursor.close()
    #return "The new item is [" +new_item + " ].."
    redirect("/")#redirect to home page


@get("/delete_item/<id:int>")
def get_delete_item(id):
    print("we are deleting", id)
    connection = sqlite3.connect("todo.db")
    cursor= connection.cursor()
    cursor.execute("delete from todo where id=?", (id,))
    #cursor.lastrowid #gives the last row id
    connection.commit() #commit to the database
    cursor.close()
    #return "The new item is [" +new_item + " ].."
    redirect("/")#redirect to home page


if ON_PYTHONANYWHERE:
    application= default_app()
else:
    #dev envi run localhost
    debug(True)
    run(host='localhost', port=8080)


