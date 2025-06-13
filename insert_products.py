from manager import MongoManager
# Nom du produit
# Prix
# Description
# Catégorie
mongo_manager = MongoManager(uri=MongoManager.get_uri_encoded())
mongo_manager.db = "exam_db"
mongo_manager.collection="products"
data = [
   {
   "name": "Ordinateur Portable",
   "price": 350.67,
   "description": "Ordinateur performant avec 16 Go de RAM et un écran Full HD.",
   "category": "Windows"
  },
 {
   "name": "PC Portable",
   "price":500.85,
   "description": "PC performant avec 32 Go de RAM et 1000 GO.",
   "category": "Dell"
  },
  {
   "name": "tablette",
   "price": 450.0,
   "description": "tablette performant avec 32 Go de RAM et un écran Full HD.",
   "category": "Appel"
  },
  {
   "name": "Iphone 16",
   "price": 549.78,
   "description": "iphone performant avec 128 Go de RAM et un écran Full HD.",
   "category": "Appel"
  },
   {
   "name": "Samsung 11",
   "price": 88.99,
   "description": "tablette performant avec 32 Go de RAM et un écran Full HD.",
   "category": "Samsung"
  },
]
results = mongo_manager.create_many_documents(data)
print(results)

