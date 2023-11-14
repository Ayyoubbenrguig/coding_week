# Ce code permet d'afficher un graphe du TOP 10 d'utilisateurs ayant voté sur le maximum de films
# Il affiche aussi dans le terminal l'utilisateur 737 qui a voté sur le maximum de films (405)
# Et les utilisateurs qui ont voté sur le minimum de films (20) ce qui est cohérent avec le dataset

import pandas as pd
import matplotlib.pyplot as plt

# changer la limite d'affichage de pandas à None
pd.set_option('display.max_rows', None)

# charger les donnees a partir d'un fichier
data = pd.read_csv('ml-100k/u.data', sep='\t', header=None, names=['user_id', 'item_id', 'rating', 'timestamp'])

# grouper les donnees par utilisateur et compter le nombre de ratings
ratings_count = data.groupby('user_id')['rating'].size().sort_values(ascending=False)

# Sélectionner les 30 premiers utilisateurs
ratings_count_top30 = ratings_count.sort_values(ascending=False).head(10)

# Afficher les résultats
max_ratings = ratings_count.max()
max_users = ratings_count[ratings_count == max_ratings].index.tolist()
min_ratings = ratings_count.min()
min_users = ratings_count[ratings_count == min_ratings].index.tolist()
print(f"La/Les personnes qui ont le nombre maximal de votes ({max_ratings}) sont les utilisateurs : {max_users}.")
print(f"La/Les personnes qui ont le nombre minimal de votes ({min_ratings}) sont les utilisateurs : {min_users}.")

# mettre le résultat dans un fichier count.txt
with open("count.txt", "w") as file:
    file.write(str(ratings_count))

# Créer un graphique à barres pour les 30 premiers utilisateurs
ratings_count_top30.plot(kind='bar')

# Ajouter des étiquettes et un titre
plt.xlabel('Utilisateurs')
plt.ylabel("Nombre d'évaluations")
plt.title("Nombre d'évaluations par utilisateur (10 premiers)")

# Afficher le graphique
plt.show()