## Simple application de chat avec mongoDB et le NLP

# Requirements

1. Python : doit etre accecible depuis une ligne de commande

2. Systeme d'exploitation : Linux,MacOS et Windows

3. Environnement virtuel crée à avec de python

4. Créer un fichier .env à la racine du projet et le remplir en se basant sur le fichier .env.example

### Fonctionnalités :

1. Informations pour un prduit

2. Prix pour un produit

### Librairies

Toutes les libraires necessaires se trouvent dans le fichier requirements.txt

### Installation des librairies :

```cmd
pip install -r requirements.txt
```

### Scénario

Cette application est une simple application de chat bot utilisant le NLP et MongoDB pour repondre aux demandes de l'utilisateur sur la base des mots clés bien definit dans le prompt.<br>

### Comment fonctionne le scénario

Lorsque un utilisateur entre un prompt voici ce qui se passe :

1. Le chat bot récupère le prompt et extrait les mots clés nécessaires grace au NLP basé sur la librairie `Spacy`.

2. une fois les mots clés récupérés, le chat bot effectue une recherche dans la base de données pour trouver le produit qui repond à la demande du prompt.

3. Une fois le produit trouvé, sur la base des mots clés de notre modèle(prix ou informations),le chat bot réponds à l'utilisateur avec un format simple et instructif.

4. une fois la réponse récu par l'utilisateur, le chat bot va lui demander s'il veut faire une autre recherche ou quitter le chat.

5. Si l'utilisateur appuis sur `OUI` alors le chat bot continuera le dialogue avec lui en lui demandant un nouveau prompt.

6. Dans le cas ou l'utilisateur choisit `NON` alors la communication avec le chat bot se termine directement et un message d'Aurevoir lui est adressé.
