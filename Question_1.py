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
# data = [
#     {
#         "title": "Harry Potter à l'école des sorciers",
#         "author": "J. K. Rowling",
#         "year": 2021,
#         "gender": "Fantasy",
#     },
#     {
#         "title": "Harry Potter et la chambre des secrets",
#         "author": "J. K. Rowling",
#         "year": 2022,
#         "gender": "Fantasy",
#     },
#     {
#         "title": "Livre vieux",
#         "author": "Auteur inconnu",
#         "year": 1800,
#         "gender": "Fantasy",
#     },
#     {
#         "title": "Harry Potter à l'école des sorciers",
#         "author": "Copycat",
#         "year": 2012,
#         "gender": "Fantasy",
#     },
# ]

# if collection:
#     try:
#         result = collection.create_index("title", unique=True)
#         results = collection.insert_many(data)
#         print(results, result)
#     except Exception as e:
#         raise Exception("An exception occurred", e)
