from pymongo import MongoClient
from ..ENV import MONGO_URI
conn = MongoClient(MONGO_URI)

print("conn: ", conn)