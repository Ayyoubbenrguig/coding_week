import pandas as pd
import matplotlib.pyplot as plt

# charger les données à partir d'un fichier
data = pd.read_csv('ml-100k/uf.data', sep='\t', header=None, names=['user_id', 'item_id', 'rating', 'timestamp'])

# grouper les données par film et compter le nombre d'évaluations par note
ratings_count = data.groupby(["item_id", "rating"])["rating"].count().unstack().fillna(0)

# sélectionner les 10 films les plus évalués
top_films = ratings_count.sum(axis=1).sort_values(ascending=False).head(10)
ratings_count = ratings_count.loc[top_films.index]

# créer un diagramme à barres empilées pour chaque film
ax = ratings_count.plot(kind='bar', stacked=True)

# ajouter des étiquettes et un titre
ax.set_xlabel('Films')
ax.set_ylabel('Nombre d\'évaluations')
ax.set_title('Proportions des évaluations par film TOP 10')

# afficher le graphique
plt.show()