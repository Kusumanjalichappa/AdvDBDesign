#!/usr/local/bin/python3.8

# utility application to reset the mongo database at mongo atlas

# pip3 install --user pymongo[srv,tls]

import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://alpha-user:alpha-user@cluster0.r1xpx.mongodb.net/<dbname>?retryWrites=true&w=majority",
                             connectTimeoutMS=30000,
                             socketTimeoutMS=None,
                             # socketKeepAlive=True,
                             connect=False, maxPoolsize=1)

if __name__ == "__main__":
    print("Check out the nodes serving this database...")
    print(client.nodes)

    print("View the names of the database on this server...")
    print(client.list_database_names())

    print("Get the todo database...")
    todo_database = client.todo

    print("View the names of the collections in this database...")
    print(todo_database.list_collection_names())

    print("Discard any old collections...")
    for name in todo_database.list_collection_names():
        if name.startswith("task"):
            todo_database.drop_collection(name)
    print(todo_database.list_collection_names())

    print("Get the (new) task collection reference")
    task_collection = todo_database.task

    print("Insert a task into the task collection")
    result = task_collection.insert_one({'task':"read some Mongo documentation", "status":False})
    print("result = ",[ result ])

    print(dir(result))
    print([result.inserted_id])
    print(str(result.inserted_id))

    print("Insert some more tasks")
    task_collection.insert_one({'task':"try some example PyMongo code", "status":False})
    task_collection.insert_one({'task':"modify the web app to use PyMongo", "status":False})
    print(todo_database.list_collection_names())

    print("Find all of the tasks")
    results = task_collection.find()
    for result in results:
        print(result)

    print("Find a random task")
    results = task_collection.find_one()
    print("result = ",result)

    print("Search for some tasks using regex, and using a projection of only selected fields")
    results = task_collection.find( {"task": {"$regex": "some"}} , ["_id","status"])
    for result in results:
        print(result)

    print("Search for nonexistent task using regex")
    result = task_collection.find_one( {"task": {"$regex": "not found anywhere"}} )
    print([ result ])

    print("Find the modify task using regex")
    result = task_collection.find_one( {"task": {"$regex": "modify"}} )
    print([ result ])
    print(type(result["_id"]))

    print("Convert the modify task _id to a string")
    _id = str(result["_id"])
    print([ _id ])

    print("Find the modify task by id")
    result = task_collection.find_one( {"_id" : ObjectId(_id)} )
    print([ result ])
    print(type(result["_id"]))

    print("Delete the modify task")
    result = task_collection.delete_one( {"_id": ObjectId(_id)} )

    print("Verify the task is gone")
    results = task_collection.find()
    for result in results:
        print(result)

    print("Re-insert the modify task")
    task_collection.insert_one({'task':"modify the web app to use PyMongo", "status":False})

    print("Verify the task is present")
    results = task_collection.find()
    for result in results:
        print(result)

    print("Find the modify task (again) using regex")
    result = task_collection.find_one( {"task": {"$regex": "modify"}} )
    print([ result ])
    print(type(result["_id"]))
    _id = str(result["_id"])
    print([ _id ])

    result = task_collection.update_one( {"_id" : ObjectId(_id)}, {'$set': {'status': True}} )
    print([ result ])

    print("Verify the task is updated")
    results = task_collection.find()
    for result in results:
        print(result)

    result = task_collection.update_one( {"task": {"$regex": "modify"}}, {'$set': {'status': False}} )
    print([ result ])

    print("Verify the task is updated")
    results = task_collection.find()
    for result in results:
        print(result)
