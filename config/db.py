from pymongo import MongoClient

conn = MongoClient("mongodb://sid:sid@ac-wfun7tx-shard-00-00.n0xs2pt.mongodb.net:27017,ac-wfun7tx-shard-00-01.n0xs2pt.mongodb.net:27017,ac-wfun7tx-shard-00-02.n0xs2pt.mongodb.net:27017/?ssl=true&replicaSet=atlas-1zgt1x-shard-0&authSource=admin&retryWrites=true&w=majority")

print("conn: ", conn)