from bottle import route, run, template
import sqlite3


@route('/todos')
def get_todos():
   connection = sqlite3.connect("todo.db")
   cursor = connection.cursor()
   cursor.execute("select * from todo")
   result = cursor.fetchall()
   cursor.close() #close the cursor, use 1 cursor per transaction.
  # return str(result)
   return template("show_list.tpl",rows=result)

run(host='localhost', port=8080)