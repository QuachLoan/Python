from pymongo import MongoClient

MONGODB_URI = "mongodb://localhost:27017/"

DATABASE_NAME = "T2605E"

COLLECTION_NAME = "Products"

class MongoDB:

    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client[DATABASE_NAME]
        self.collection = self.db[COLLECTION_NAME]

    def kiem_tra_ket_noi(self):
        self.client.admin.command("ping")
        return True