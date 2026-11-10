from pymongo import MongoClient
MONGODB_URI= "mongodb://localhost:27017/"
MONGODB_DATABASE="T2605E"
COLLECTION_NAME="Students"
class MongoDB:
    def __init__(self):
        self.client= MongoClient(MONGODB_URI)
        self.db= self.client[MONGODB_DATABASE]
        self.collection= self.db[COLLECTION_NAME]
    def kiem_tra_ket_not(self):
        self.client.admin.command('ping')
        return True