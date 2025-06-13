from manager import MongoManager
# Nom
# Prix
# Description
# Catégorie
mongo_manager = MongoManager(uri=MongoManager.get_uri_encoded())
mongo_manager.db = "exam_db"
collection = mongo_manager.create_collection(
    collection_name="products",
    schema={
        "$jsonSchema": {
            "bsonType": "object",
            "additionalProperties": True,
            "required": [
                "nom",
                "prix",
                "description",
                "catégorie"
            ],
            "properties": {
                "nom": {
                    "bsonType": "string",
                },
                "prix": {
                    "bsonType": "double",
                },
                "description": {"bsonType": "string"},
                "catégorie": {
                    "bsonType": "string",
                },
            },
        }
    },
)
