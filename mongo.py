import pymongo as mo

client = mo.MongoClient('localhost', 27017)
db = client['test']
names_collection = db['users']

names = names_collection.find()
for name in names:
    print(name)


