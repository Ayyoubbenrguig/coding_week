import pandas as pd
import matplotlib.pyplot as plt

# Charger les données à partir du fichier u.data en utilisant la fonction read_csv de pandas
data = pd.read_csv("ml-100k/uf.data", sep="\t",encoding="ISO-8859-1", names=["user_id", "item_id", "rating", "timestamp"])

# Calculer la moyenne des évaluations pour chaque film
mean_ratings = data.groupby("item_id")["rating"].mean()

# Compter le nombre d'évaluations pour chaque film
count_ratings = data.groupby("item_id")["rating"].count()

# Créer un DataFrame contenant la moyenne et le nombre d'évaluations pour chaque film
movie_stats = pd.DataFrame({"mean_rating": mean_ratings, "count_rating": count_ratings})

# Filtrer les films ayant moins de 50 évaluations
popular_movies = movie_stats[movie_stats["count_rating"] >= 50]

# Trier les résultats par ordre décroissant de moyenne des évaluations et afficher les 30 premiers
top_movies = popular_movies.sort_values(by="mean_rating", ascending=False).head(30)

# Créer un graphique en barres pour le nombre d'évaluations
ax1 = top_movies['count_rating'].plot(kind='bar', color='blue', alpha=0.5)
ax1.set_ylabel("Nombre d'évaluations")
ax1.set_title("Nombre d'évaluations et moyenne des évaluations pour les 30 premiers films")

# Créer un deuxième axe y pour la moyenne des évaluations
ax2 = plt.twinx()
ax2.set_ylim([4, top_movies['mean_rating'].max()])
ax2.set_ylabel('Moyenne des évaluations')

# Ajouter la courbe de la moyenne des évaluations au deuxième axe y
top_movies['mean_rating'].plot(kind='line', color='red', ax=ax2)

# Faire pivoter les étiquettes de l'axe x à 90 degrés
plt.xticks(rotation='vertical')

# Afficher le graphique
plt.show()
