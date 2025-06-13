from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.collection import Collection
from pymongo.database import Database

import os
from dotenv import load_dotenv
from urllib.parse import quote_plus


class MongoManager:
    def __init__(self, uri: str):
        self.client = MongoClient(uri, server_api=ServerApi("1"), tls=True)
        try:
            ping = self.client.admin.command({"ping": 1})
            print(ping)
        except Exception:
            raise Exception("An exception occurred")
        self.__db = None
        self.__collection = None

    @property
    def client(self) -> MongoClient:
        return self.__client

    @client.setter
    def client(self, value: MongoClient) -> None:
        self.__client = value

    @property
    def db(self)->Database|None:
        return self.__db

    @db.setter
    def db(self, db_name: str) -> None:
        self.__db = self.__client[db_name]
        if self.__collection is not None:
            self.collection = self.__collection.name

    @property
    def collection(self) -> Collection|None:
        return self.__collection

    @collection.setter
    def collection(self, collection_name: str) -> None:
        if self.db != None:
            self.__collection =  self.db[collection_name]

    def close_connection(self):
        self.client.close()
        print("connection close successfully!")

    def list_collections(self) -> list:
        if self.db != None:
            collections = self.db.list_collection_names()
            return collections
        else:
            raise Exception("database not exits")

    def list_databases(self) -> list:
        try:
            databases = self.client.list_database_names()
            return databases
        except Exception as e:
            raise Exception(
                "Unable to list the databases due to the following error: ", e
            )

    @staticmethod
    def get_uri_encoded() -> str:
        # Load config from a .env file:
        load_dotenv(verbose=True)
        username = os.environ["DB_USER"]
        password = os.environ["DB_PASSWORD"]
        cluster = os.environ["CLUSTER"]
        # Encoder le nom d'utilisateur et le mot de passe
        encoded_username = quote_plus(username)
        encoded_password = quote_plus(password)
        # Consolidation de l'uri de connexion
        uri = f"mongodb+srv://{encoded_username}:{encoded_password}@{cluster}.mongodb.net/"
        return uri

    # CRUD
    def create_one_document(self, document: dict) -> dict:
        try:
            if self.collection!=None:
                insert_result = self.collection.insert_one(document)
                return {
                    "acknowledged": insert_result.acknowledged,
                    "insertedId": insert_result.inserted_id,
                }
            else:
                raise Exception("collection must not be None")
        except Exception as e:
            raise Exception(
                "Unable to insert the document due to the following error:", e
            )

    def create_many_documents(self, documents: list[dict]) -> dict:
        try:
            if self.collection!=None:
                insert_result = self.collection.insert_many(documents)
                return {
                    "acknowledged": insert_result.acknowledged,
                    "insertedIds": insert_result.inserted_ids,
                }
            else:
                raise Exception("collection must not be None")
        except Exception as e:
            raise Exception(
                "Unable to insert the documents due to the following error: ", e
            )

    def update_one_document(self, query: dict, new_values: dict):
        try:
            if self.collection!=None:
                update_result = self.collection.update_one(query, new_values)
                return {
                    "acknowledged": update_result.acknowledged,
                    "insertedId": update_result.upserted_id,
                    "matchedCount": update_result.matched_count,
                    "modifiedCount": update_result.modified_count,
                }
            else:
                raise Exception("collection must not be None")
        except Exception as e:
            raise Exception(
                "Unable to update the document due to the following error:", e
            )

    def update_many_documents(self, query: dict, new_values: dict):
        try:
            if self.collection!=None:
                update_result = self.collection.update_many(query, new_values)
                return {
                    "acknowledged": update_result.acknowledged,
                    "insertedId": update_result.upserted_id,
                    "matchedCount": update_result.matched_count,
                    "modifiedCount": update_result.modified_count,
                }
            else:
                raise Exception("collection must not be None")
        except Exception as e:
            raise Exception(
                "Unable to update the documents due to the following error: ", e
            )

    def read_one_document(self, query: dict):
        try: 
            if self.collection!=None:
                document = self.collection.find_one(query)
                return document
            else:
                raise Exception("collection must not be None")
        except Exception as e:
            raise Exception(
                "Unable to read the document due to the following error:", e
            )

    def read_many_documents(self, query: dict):
        try:
            if self.collection!=None:
                documents = self.collection.find(query)
                return list(documents)
            else:
                raise Exception("collection must not be None")
        except Exception as e:
            raise Exception(
                "Unable to read the documents due to the following error:", e
            )

    def delete_one_document(self, query: dict):
        try:
            if self.collection!=None:
                delete_result = self.collection.delete_one(query)
                return {
                    "acknowledged": delete_result.acknowledged,
                    "deletedCount": delete_result.deleted_count,
                }
            else:
                raise Exception("collection must not be None")
        except Exception as e:
            raise Exception(
                "Unable to delete the document due to the following error:", e
            )

    def delete_many_documents(self, query: dict):
        try:
            if self.collection!=None:
                delete_result = self.collection.delete_many(query)
                return {
                    "acknowledged": delete_result.acknowledged,
                    "deletedCount": delete_result.deleted_count,
                }
            else:
                raise Exception("collection must not be None")
        except Exception as e:
            raise Exception(
                "Unable to delete the documents due to the following error: ", e
            )

    def create_collection(
        self, collection_name: str, schema: dict
    ) -> Collection | None:
        """_summary_

        Args:
            collection_name (str)
            schema (dict)

        Raises:
            Exception: i error occured

        Returns:
            Collection | None: Collection if collection is create None if collection already exists
        """
        try:
            if collection_name not in self.list_collections():
                self.collection = collection_name
                if self.db!=None:
                    doc = self.db.create_collection(collection_name, validator=schema)
                    return doc
                else:
                    raise Exception("database must not be None")
        except Exception as e:
            raise Exception("An exception occurred", e)

db_manager = MongoManager(uri=MongoManager.get_uri_encoded())
# database_name = db_manager.list_databases()
# print(database_name)
# db_manager.db = "tp_school"
# collection_name = db_manager.list_collections()
# print(collection_name)
# db_manager.db = "users"
# collection_name = db_manager.list_collections()
# print(collection_name)
