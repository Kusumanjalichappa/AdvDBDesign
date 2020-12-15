import sqlite3
import random
random.seed()

from tinydb import TinyDB, Query

db = TinyDB("todo.json")
db.truncate()

def get_items():
    global db
    return db.all()

# def get_item(id):
#     connection = sqlite3.connect("todo.db")
#     cursor = connection.cursor()
#     cursor.execute("select * from todo where id=?",(id,))
#     result = cursor.fetchall()
#     cursor.close()
#     if len(result) == 0:
#         return None
#     return result[0]

# def update_status(id, value):
#     connection = sqlite3.connect("todo.db")
#     cursor = connection.cursor()
#     cursor.execute("update todo set status=? where id=?",(value, id))
#     connection.commit()
#     cursor.close()

# def create_item(task, status):
#     connection = sqlite3.connect("todo.db")
#     cursor = connection.cursor()
#     cursor.execute("insert into todo (task, status) values (?,?)", (task, status))
#     id = cursor.lastrowid
#     connection.commit()
#     cursor.close()
#     return id

# def update_item(id, updated_task):
#     connection = sqlite3.connect("todo.db")
#     cursor = connection.cursor()
#     cursor.execute("update todo set task=? where id=?", (updated_task, id))
#     connection.commit()
#     cursor.close()

# def delete_item(id):
#     connection = sqlite3.connect("todo.db")
#     cursor = connection.cursor()
#     cursor.execute("delete from todo where id=?", (id,))
#     connection.commit()
#     cursor.close()

# def _random_text():
#     random_text = str(random.randint(10000,20000))
#     return random_text

def test_get_items():
    global db
    db.insert({"task":"task1","status":0})
    db.insert({"task":"task2","status":1})
    print("testing get_items")
    results = get_items()
    print(results)

    # assert type(results) is list
    # assert len(results) > 0
    # for item in results:
    #     assert type(item) is tuple
    # id, task, status = results[0]
    # assert type(id) is int
    # assert type(task) is str
    # assert type(status) is int
    # assert status in [0,1]

# def test_get_item():
#     print("testing get_item(id)")
#     results = get_items()
#     assert len(results) > 0
#     id, task, status = results[0]
#     result = get_item(id)
#     assert type(result) is tuple
#     id2, task2, status2 = result
#     assert id2 == id
#     assert task2 == task
#     assert status2 == status

# def test_create_item():
#     print("testing create_item()")
#     example_task = "This is an example item #" + _random_text()
#     id = create_item(example_task, 0)
#     returned_id, task, status = get_item(id)
#     assert returned_id == id
#     assert task == example_task
#     assert status == 0

# def test_update_status():
#     print("testing update_status()")
#     example_task = "This is an example item #" + _random_text()
#     id = create_item(example_task, 0)
#     _, _, status = get_item(id)
#     assert status == 0
#     update_status(id, 1)
#     _, _, status = get_item(id)
#     assert status == 1
#     update_status(id, 0)
#     _, _, status = get_item(id)
#     assert status == 0

# def test_update_item():
#     print("testing update_item()")
#     example_task = "This is an example item #" + _random_text()
#     id = create_item(example_task, 0)
#     updated_task = example_task + " updated..."
#     update_item(id, updated_task)
#     _, task, status = get_item(id)
#     assert task == updated_task

# def test_delete_item():
#     print("testing delete_item()")
#     example_task = "This is an example item #" + _random_text()
#     id = create_item(example_task, 0)
#     returned_id, _, _ = get_item(id)
#     assert returned_id == id
#     delete_item(id)
#     assert get_item(id) == None

if __name__ == "__main__":
    test_get_items()
    # test_get_item()
    # test_create_item()
    # test_update_status()
    # test_update_item()
    # test_delete_item()
    print("done.")