from bottle import route, run, template
import sqlite3


@route('/todos')
def get_todos():
   connection = sqlite3.connect("todo.db")
   cursor = connection.cursor()
   cursor.execute("select * from todo")
   result = cursor.fetchall()
   return str(result)
    
run(host='localhost', port=8080)