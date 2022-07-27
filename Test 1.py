import pymongo

client = pymongo.MongoClient("mongodb+srv://Rajat_Nigam:rajat123@firstcluster.secrrxz.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "Rajat Nigam",
    "email" : "rajat@123",
    "company" : "Amazon"
}
db1=client["mongotest"]
coll = db1['test1']
coll.insert_one(d)