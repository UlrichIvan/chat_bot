from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from pymongo.collection import Collection
from pymongo.database import Database


class MongoManager:
    def __init__(self, uri: str,db_name: str = "test"):
        self.__client = MongoClient(uri, server_api=ServerApi("1"), tls=True)
        try:
            ping = self.__client.admin.command({"ping": 1})
            print(
                f"Pinged your deployment: {ping}. You successfully connected to MongoDB!"
            )
        except Exception as e:
            raise Exception(
                "Unable to connect to MongoDB due to the following error: ", e
            )
        
        self.__db= self.__client[db_name]
        self.__collection= None

    @property
    def db(self)->Database:
        return self.__db

    @db.setter
    def db(self, db_name: str):
        self.__db = self.__client[db_name]
        # réaffectation obligatoire de la collection car changement de database
        if self.__collection is not None:
            self.collection = (
                self.__collection.name
            )  # .name car collection est un objet

    @property
    def collection(self)->Collection | None:
        return self.__collection

    @collection.setter
    def collection(self, coll_name: str):
        self.__collection = self.db[coll_name]
 
    def close_connection(self):
        self.__client.close()
        print("Connection closed.")

    def list_databases(self):
        try:
            databases = self.__client.list_database_names()
            return databases
        except Exception as e:
            raise Exception(
                "Unable to list the databases due to the following error: ", e
            )

    def list_collections(self):
        if self.db is not None:
            try:
                collections = self.db.list_collection_names()
                return collections
            except Exception as e:
                raise Exception(
                    "Unable to list the collections due to the following error: ", e
                )
        else:
            raise Exception("Veuillez paramétrer une db")


# db_manager = MongoManager(
#     uri="mongodb+srv://Cluster10367:test-gema@gema-test.ly5is3l.mongodb.net/"
# )
# database_name = db_manager.list_databases()
# print(database_name)
# db_manager.db = "sample_mflix"
# collection_name = db_manager.list_collections()
# print(collection_name)
# db_manager.db = "tp"
# collection_name = db_manager.list_collections()
# print(collection_name)
