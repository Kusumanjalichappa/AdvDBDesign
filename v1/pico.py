import pickle
import os

items = [ ]

filename = None

def everything(v):
    return v

def always(v):
    return True

def never(v):
    return False

def open_database(name):
    global filename
    global items
    filename = name
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            items = pickle.load(f)
    else:
        items = [ ]

def commit():
    global filename
    global items
    with open(filename, "wb") as f:
        pickle.dump(items,f)

def insert(data):
    items.append(data)
    commit()

def query(select=everything, where=always):
    return [select(item) for item in items if where(item)]

def delete(where=never):
    global items
    kept_items = [item for item in items if not where(item)]
    items = kept_items
    commit()

def update(where=never, content=lambda v:{}):
    global items
    for item in items:
        if where(item):
            new_values = content(item)
            for key in new_values.keys():
                item[key] = new_values[key]
    commit()

if __name__ == "__main__":
    open_database("pico.pkl")
    delete(where=always)
    insert({"id":1, "task":"do something useful", "status":0})
    insert({"id":2, "task":"do something else useful", "status":0})
    insert({"id":3, "task":"do something enjoyable", "status":0})
    select = lambda v : v
    where = lambda v : True
    # for item in query(select=everything, where=always):
    #     print(item)
    # for item in query(select=lambda v:v['task'], where=lambda v:v['id']==3):
    #     print(item)
    # print(query(select=everything, where=lambda v:v['id']==1))
    # delete(where=lambda v:v['id']==1)
    # print(query(select=everything, where=lambda v:v['id']==1))
    print(query(select=everything, where=lambda v:v['id']==2))
    update(where=lambda v:v['id']==2, content=lambda v:{'status':v['status']+1})
    print(query(select=everything, where=lambda v:v['id']==2))


