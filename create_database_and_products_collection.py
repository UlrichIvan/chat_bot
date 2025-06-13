from manager import MongoManager
# Nom du produit
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
                "name",
                "price",
                "description",
                "category"
            ],
            "properties": {
                "name": {
                    "bsonType": "string",
                },
                "price": {
                    "bsonType": "double",
                },
                "description": {"bsonType": "string"},
                "category": {
                    "bsonType": "string",
                },
            },
        }
    },
)
