import pandas as pd
import matplotlib.pyplot as plt

# changer la limite d'affichage de pandas à None
pd.set_option('display.max_rows', None)

# charger les donnees a partir d'un fichier
data = pd.read_csv('ml-100k/uf.data', sep='\t', header=None, names=['user_id', 'item_id', 'rating', 'timestamp'])
data = data[(data['rating']==1)]

# grouper les donnees par utilisateur et compter le nombre de ratings
ratings_count = data.groupby('item_id')['rating'].count()

# Sélectionner les 30 premiers utilisateurs
ratings_count_top10 = ratings_count.sort_values(ascending=False).head(10)

# Créer un graphique à barres pour les 30 premiers utilisateurs
ratings_count_top10.plot(kind='bar')

# Ajouter des étiquettes et un titre
plt.xlabel('Films')
plt.ylabel("Nombre d'évaluations")
plt.title("TOP 10 films avec la note de 1/5")
####################################
fig, ax = plt.subplots()
ax.pie(ratings_count_top10, labels=ratings_count_top10.index, autopct='%1.1f%%')#, autopct='%1.1f%%'
ax.set_aspect('equal')  # Pour rendre le cercle parfaitement rond

# Ajouter un cercle blanc au centre pour créer l'effet doughnut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)
plt.title("TOP 10 films avec la note de 1/5")
plt.show()
###########################
          

# Afficher le graphique
plt.show()