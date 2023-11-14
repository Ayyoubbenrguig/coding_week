# Ce code permet d'afficher un graphe qui donne la répartition la métier ou occupation des utilisateurs

import pandas as pd
import matplotlib.pyplot as plt

# changer la limite d'affichage de pandas à None
pd.set_option('display.max_rows', None)

# charger les données a partir d'un fichier
data = pd.read_csv('ml-100k/u.user', sep='|', header=None, names=['user_id','age','gender','occcupation','zip code'])
print(data)

# grouper les donnees par utilisateur et compter le nombre de ratings
ratings_count = data.groupby('occcupation')['user_id'].count()

# Sélectionner les 30 premiers utilisateurs
ratings_count_top30 = ratings_count.sort_values(ascending=False).head(10)

# Créer un graphique en barres pour les 30 premiers utilisateurs
plt.bar(ratings_count_top30.index, ratings_count_top30.values)

# Ajouter des étiquettes et un titre
plt.xlabel('Occupations')
plt.ylabel('Nombre d\'utilisateurs')
plt.title('Répartition des occupations des utilisateurs')

# Afficher le graphique
plt.show()