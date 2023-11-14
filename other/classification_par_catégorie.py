import pandas as pd
import matplotlib.pyplot as plt

# changer la limite d'affichage de pandas à None
pd.set_option('display.max_rows', None)

# charger les donnees a partir d'un fichier
data = pd.read_csv('../ml-100k/u.item',encoding='ISO-8859-1', sep='|', header=None, names=[' item id','item title','release date','video release date',' IMDb URL ','unknown',' Action','Adventure',' Animation','Comedy','Crime', 'Documentary ', 'Drama ', 'Fantasy',
              "Film-Noir" , "Horror ", "Musical" , "Mystery" , "Romance" , "Sci-Fi ",
              "Thriller" ," War ",' Western' ])
#data=data_1[(data_1['occupation']==5)]
print(data)
# grouper les donnees par utilisateur et compter le nombre de ratings

ratings_count = data.groupby('occcupation')['user_id'].count()



# Sélectionner les 30 premiers utilisateurs
ratings_count_top30 = ratings_count.head(30)

# Afficher les résultats
max_ratings = ratings_count.max()
max_users = ratings_count[ratings_count == max_ratings].index.tolist()
min_ratings = ratings_count.min()
min_users = ratings_count[ratings_count == min_ratings].index.tolist()


print(f"La/Les Films qui ont le nombre maximal de votes ({max_ratings}) sont les utilisateurs : {max_users}.")
print(f"La/Les Films qui ont le nombre minimal de votes ({min_ratings}) sont les utilisateurs : {min_users}.")

# mettre le résultat dans un fichier count.txt
with open("count.txt", "w", encoding='utf-8') as file:
    file.write(str(ratings_count))

# Créer un graphique à barres pour les 30 premiers utilisateurs
ratings_count_top30.plot(kind='bar')

# Ajouter des étiquettes et un titre
plt.xlabel('Utilisateurs')
plt.ylabel("catégorie sociale")
plt.title("Nombre des pesonnes par catégorie")

# Afficher le graphique
plt.show()