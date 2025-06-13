import spacy
import re
import os
from manager import MongoManager

DOC_KEYS=[
    "nom",
    "prix",
    "description",
    "catégorie"
]

TARGETS_PROMPT=[
    "prix",
    "informations"
]

def get_keys(prompt:str)->list:
    s=re.sub(r"\d+", "", prompt)
    docs=nlp(s)
    texts=[
        doc.text.strip() for doc in docs 
        if doc.text.strip()!="" and not doc.is_stop and not doc.is_punct 
    ]
    return texts
def get_mongodb_manager()->MongoManager:
    mongo_manager = MongoManager(uri=MongoManager.get_uri_encoded())
    mongo_manager.db = "exam_db"
    mongo_manager.collection="products"
    return mongo_manager

# load langage package of french
nlp = spacy.load("fr_core_news_sm")

print("\n\nBienvenue je suis votre assistant pour répondre à vos questions\n\n")


manager=get_mongodb_manager()
product_collection=manager.collection
try:
    while True:
        print("Mots clés à utliser:",end="\n\n")
        for i,v in enumerate(TARGETS_PROMPT):
            print(f"{i+1}.{v}",end="\n\n")
        # get input of user
        prompt=input("\n\nEntrer un prompt en utilisant les mots clés indiqués ci dessus pour un produit(exemple : prix du PC): \n\n")
        
        # get list of importants keys of prompt 
        keys=get_keys(prompt=prompt)
        rgx="|".join(keys)
        
        if product_collection!=None:
            query={
                "$or":[
                    { key:{"$regex":rgx,"$options":"i"} }
                    for _,key in enumerate(DOC_KEYS)
                ]
            }
            product=product_collection.find_one(query)
            if product:
                print("\n\n")
                print("="*5,"Résultats","="*5,end="\n\n")
                # si le prix est demandé
                if TARGETS_PROMPT[0] in keys:
                    print("Voici ce que nous avons pu trouvé qui correspond à votre demande",end="\n\n")    
                    print(f"Le prix de {product.get('nom')} est de {product.get('prix')} €")
                elif TARGETS_PROMPT[1] in keys:
                    print("Voici ce que nous avons pu trouvé qui correspond à votre demande",end="\n\n")    
                    print(f"Informations sur le produit {product.get('nom')}",end="\n\n")
                    for k,v in product.items():
                        if k!="_id":
                            print(f"{k} : {v}" if k!= "prix" else f"{k} : {v} €"  ,end="\n\n")
                else :
                    print("Désolé nous n'avons pas pu trouvé de réponse à votre question.")
                    print("\n\nVeuillez etre précis en utilisant les mots clés : prix,informations.")
            else :
                print("Désolé nous n'avons pas pu trouvé de réponse à votre question veuillez etre précis.")
            loop_answer=str(input("\n\nAvez vous d'autres questions ? entré OUI pour continuer et Non pour quitter le chat\n\n"))
            print(os.name)
            if loop_answer.lower()=="oui":
                os.system("cls" if os.name in ("nt","dos") else "clear")
                continue
            else:
                break
        else:
            print("impossible de vous repondre!")
    print("\n\nAurevoir!!!\n\n")
except:
    print("\n\nUne erreur est survenue, veuillez poser à nouveau votre question s'il vous plait\n\n")

