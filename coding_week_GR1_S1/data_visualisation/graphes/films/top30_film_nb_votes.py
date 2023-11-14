# Ce code permet de donner le top 10 des films qui ont reçu le maximum de votes
# et affiche dans la console les films ayant eu le plus grand nombre de votes, et ceux ayant eu le plus petit nombre de votes

import pandas as pd
import matplotlib.pyplot as plt

# changer la limite d'affichage de pandas à None
pd.set_option('display.max_rows', None)

# charger les donnees a partir d'un fichier
data = pd.read_csv('ml-100k/uf.data', sep='\t',encoding='ISO-8859-1', header=None, names=['user_id', 'item_id', 'rating', 'timestamp'])

# grouper les donnees par utilisateur et compter le nombre de ratings
ratings_count = data.groupby("item_id")["rating"].count()
#print(ratings_count)

# Sélectionner les 30 premiers utilisateurs
ratings_count_top30 = ratings_count.sort_values(ascending=False).head(10)

# Afficher les résultats
max_ratings = ratings_count.max()
max_users = ratings_count[ratings_count == max_ratings].index.tolist()
min_ratings = ratings_count.min()
min_users = ratings_count[ratings_count == min_ratings].index.tolist()
print(f"La/Les Films qui ont le nombre maximal de votes ({max_ratings}) sont les Films : {max_users}.")
print(f"La/Les Films qui ont le nombre minimal de votes ({min_ratings}) sont les Films : {min_users}.")

# mettre le résultat dans un fichier count.txt
with open("count.txt", "w", encoding='utf-8') as file:
    file.write(str(ratings_count))

# Créer un graphique à barres pour les 30 premiers utilisateurs
ratings_count_top30.plot(kind='bar')

# Ajouter des étiquettes et un titre
plt.xlabel('Utilisateurs')
plt.ylabel("Nombre d'évaluations")
plt.title("Nombre d'évaluations par Film (30 premiers)")

# Afficher le graphique
plt.show()