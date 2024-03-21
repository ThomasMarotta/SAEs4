from pymongo import MongoClient

class ClientMongo:
    def __init__(self):
        self.connection_url = "mongodb://localhost:27017/TennisMania"
        self.client = None
        self.db = None
        self.collections = None

    def connect(self):
        try:
            self.client = MongoClient(self.connection_url)
            self.db = self.client.get_database()
            self.collections = self.db.list_collection_names()
            print("Connected to MongoDB successfully")
        except Exception as e:
            print("Failed to connect to MongoDB:", e)

    def close_connection(self):
        try:
            if self.client:
                self.client.close()
                print("Connection to MongoDB closed successfully")
        except Exception as e:
            print("Failed to close MongoDB connection:", e)

    def get_client(self):
        return self.client

    def get_database(self):
        return self.db

    def get_collections(self):
        return self.collections

    def get_joueurs_collection(self):
        return self.db["Joueurs"]

    def get_tournoi_collection(self):
        return self.db["Tournoi"]