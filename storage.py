import sqlite3

def get_item(id):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo where id=?",(id,))
    result = cursor.fetchall()
    cursor.close()
    return result[0]

def get_items():
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("select * from todo")
    result = cursor.fetchall()
    cursor.close()
    return result

def update_status(id,value):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set status=? where id=?",(value, id))
    connection.commit()
    cursor.close()

def create_item(task,status):
    #we are getting a request that has information that needs to be saved
    connection = sqlite3.connect("todo.db")
    cursor= connection.cursor()
    cursor.execute("insert into todo (task, status) values (?,?)", (task, status))
    #cursor.lastrowid #gives the last row id
    id = cursor.lastrowid
    connection.commit() #commit to the database
    cursor.close()
    return id


def update_item(id,updated_task):
    connection = sqlite3.connect("todo.db")
    cursor = connection.cursor()
    cursor.execute("update todo set task=? where id=?", (updated_task, id))
    connection.commit()
    cursor.close()


def delete_item(id):
    connection = sqlite3.connect("todo.db")
    cursor= connection.cursor()
    cursor.execute("delete from todo where id=?", (id,))
    #cursor.lastrowid #gives the last row id
    connection.commit() #commit to the database
    cursor.close()

def test_get_items():
    print("testing items")
    results = get_items()
    assert type(results) is list
    assert len(results) > 0
    print(results)
    for item in results:
         assert type(item) is tuple
    id, task,status = results[0]
    assert type(id) is int
    assert type(task) is str
    assert type(status) is int
    assert status in [0,1]

def test_get_item():
    print("testing get_items(id)")
    results = get_items()
    assert len(results) > 0
    id,_,_ = results[0]  #id,task,status ..but since the other 2 variable are not imp we can do this
    result = get_item(id)
    assert type(result) is tuple
    id2,task,status = result
    assert id2 ==id
    print(result)

def delete_item():
    print("testing delete_item()")
    example_task = "This is an example item #" + _random_text()
    id = create_item(example_task, 0)
    returned_id, _, _ = get_item(id)
    assert returned_id == id
    delete_item(id)
    assert get_item(id) == None

def test_update_item():
    print("testing update_item()")
    example_task = "This is an example item #" + _random_text()
    id = create_item(example_task, 0)
    updated_task = example_task + " updated..."
    update_item(id, updated_task)
    _, task, status = get_item(id)
    assert task == updated_task

import random
random.seed()

def _random_text():
    random_text = str(random.randint(10000,20000))
    return random_text

def test_create_item():
    random_text = str(random.randint(10000,20000))
    example_task = "This is an example item" + random_text
    create_item(example_task, 0)
    items= get_items()
    found = False
    for item in items:
        print(item)
        id, task,status = item
        if task == example_task:
            found = True
    assert found == True
    print("item seem to have been created")

def test_update_status():
    print("testing update_status()")
    example_task = "This is an example item #" + _random_text()
    id = create_item(example_task, 0)
    _, _, status = get_item(id)
    assert status == 0
    update_status(id, 1)
    _, _, status = get_item(id)
    assert status == 1
    update_status(id, 0)
    _, _, status = get_item(id)
    assert status == 0

def test_delete_item():
    print("testing delete_item()")
    example_task = "This is an example item #" + _random_text()
    id = create_item(example_task, 0)
    returned_id, _, _ = get_item(id)
    assert returned_id == id
    delete_item(id)
    assert get_item(id) == None


#python idiom
#this will make sure to run test_get_item runs only when we run the this fiel
#directly, its mostly used to test function before incorporating it into web
if __name__ == "__main__":
    #test_get_items()
    #test_get_item()
    #test_create_item()
    test_update_status()
    test_update_item()
    test_delete_item()
    print("done.")
