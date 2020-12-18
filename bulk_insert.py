import pymongo

client = pymongo.MongoClient("mongodb+srv://alpha-user:alpha-user@cluster0.r1xpx.mongodb.net/<dbname>?retryWrites=true&w=majority",
                             connectTimeoutMS=30000,
                             socketTimeoutMS=None,
                             # socketKeepAlive=True,
                             connect=False, maxPoolsize=1)

db = client.todo

task_collection = db["task"]

task_list = [
  {"task":"Asia","status":False,"randomNum":-82},
  {"task":"N.America","status":True,"randomNum":-63},
  {"task":"S.America","status":False,"randomNum":3},
  {"task":"Africa","status":True,"randomNum":77},
  {"task":"Europe","status":False,"randomNum":43},
  {"task":"Antartica","status":True,"randomNum":631},
  {"task":"Why Australia whats to be called Oceania","status":True,"randomNum":632},
  {"task":"Random Places on earth","status":False,"randomNum":85},
]

result = task_collection.insert_many(task_list)

print(result.inserted_ids)