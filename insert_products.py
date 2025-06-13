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
   "nom": "Ordinateur Portable",
   "prix": 350.67,
   "description": "Ordinateur performant avec 16 Go de RAM et un écran Full HD.",
   "catégorie": "Windows"
  },
 {
   "nom": "PC Portable",
   "prix":500.85,
   "description": "PC performant avec 32 Go de RAM et 1000 GO.",
   "catégorie": "Dell"
  },
  {
   "nom": "tablette",
   "prix": 450.0,
   "description": "tablette performant avec 32 Go de RAM et un écran Full HD.",
   "catégorie": "Appel"
  },
  {
   "nom": "Iphone 16",
   "prix": 549.78,
   "description": "iphone performant avec 128 Go de RAM et un écran Full HD.",
   "catégorie": "Appel"
  },
   {
   "nom": "Samsung 11",
   "prix": 88.99,
   "description": "tablette performant avec 32 Go de RAM et un écran Full HD.",
   "catégorie": "Samsung"
  },
]
results = mongo_manager.create_many_documents(data)
print(results)

