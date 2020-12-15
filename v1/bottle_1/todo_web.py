from bottle import get, post, template,request,redirect
import sqlite3
import os

#check which envi we are running the application dev or prod
ON_PYTHONANYWHERE =  "PYTHONANYWHERE_DOMAIN" in os.environ 
assert ON_PYTHONANYWHERE ==False


if ON_PYTHONANYWHERE:
    pass
else:
    #dev envi import run and debug
    from bottle import  run,debug

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
    new_item = request.forms.get("new_item")#so we have to get access to the request module
    return "The new item is [" + new_item +"]..."

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

if ON_PYTHONANYWHERE:
    pass
else:
    #dev envi run localhost
    debug(True)
    run(host='localhost', port=8080)