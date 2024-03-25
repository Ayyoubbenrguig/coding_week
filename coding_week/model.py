
import numpy as np
import pandas as pd
import pickle as pkl

# ALS factorization function (Cette fonction réalise une factorisation matricielle de la matrice des évaluations R, en utilisant l'algorithme Alternating Least Squares (ALS))
def als_factorization(R, K, steps=10, alpha=0.01, beta=0.02):
    """
    Perform matrix factorization using ALS.

    Parameters:
    - R (numpy array): User-item ratings matrix.
    - K (int): Number of latent features.
    - steps (int): Number of iterations.
    - alpha (float): Learning rate.
    - beta (float): Regularization parameter.

    Returns:
    - P (numpy array): User-latent features matrix.
    - Q (numpy array): Item-latent features matrix.
    """
    # Initialize user and item latent feature matrix
    P = np.random.rand(R.shape[0], K)
    Q = np.random.rand(R.shape[1], K)


    # Transpose Q for ease of calculation
    Q = Q.T

    for step in range(steps):
        # Update user features
        for i in range(R.shape[0]):
            for j in range(R.shape[1]):
                if R[i][j] > 0:
                    eij = R[i][j] - np.dot(P[i,:], Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])

        # Update item features
        for i in range(R.shape[1]):
            for j in range(R.shape[0]):
                if R[j][i] > 0:
                    eij = R[j][i] - np.dot(P[j,:], Q[:,i])
                    for k in range(K):
                        Q[k][i] = Q[k][i] + alpha * (2 * eij * P[j][k] - beta * Q[k][i])
    

    with open('./models/P_matrix.pkl', 'wb') as f:
        pkl.dump(P, f)

    with open('./models/Q_matrix.pkl', 'wb') as f:
        pkl.dump(Q.T, f)
    return P, Q.T


def get_user_recommendations(user_id, P, Q, R_original, num_recommendations=5):
    user_ratings_prediction = np.dot(P[int(user_id), :], Q.T)
    already_rated = np.where(R_original[int(user_id), :] > 0)[0]
    user_ratings_prediction[already_rated] = -1
    top_movie_indices = np.argsort(user_ratings_prediction)[-num_recommendations:][::-1]
    top_movie_ids = top_movie_indices + 1  # Add 1 if movie IDs are 1-based
    return top_movie_ids
# Function to get recommendations with movie titles and genres
def run_als_and_get_recommendations_with_titles(P, Q, data_path, user_id, K_values, train=False):
    l = []
    # Load user ratings
    ratings = pd.read_csv(data_path, sep='\t', header=None, names=['user_id', 'item_id', 'rating', 'timestamp'])
    n_users = ratings['user_id'].max()
    n_items = ratings['item_id'].max()
    R = np.zeros((n_users, n_items))
    for row in ratings.itertuples():
        R[row[1]-1, row[2]-1] = row[3]

    movie_titles, movie_genres = load_movie_info('./data/u.item', './data/u.genre')


    for K in [K_values]:
        print(f"\nRunning ALS with K={K}")
        if train : 
            P, Q = als_factorization(R, K)
        user_id_idx = user_id - 1  # Adjust if user_id in the dataset is 1-based
        recommended_movie_ids = get_user_recommendations(user_id_idx, P, Q, R, num_recommendations=5)

        # Print recommendations with titles and genres
        print(f"Recommendations for user {user_id} with K={K}:")
        for i, movie_id in enumerate(recommended_movie_ids):
            title = movie_titles[movie_id - 1]  # Adjust for 0-based indexing
            genres = movie_genres[movie_id - 1]
            print(f"Movie ID: {movie_id}, Title: {title}, Genres: {', '.join(genres)}")
            movie_info = {
                'ranking': i + 1,
                'id': movie_id,
                'title': title,
                'genres': ' | '.join(genres)
            }
            l.append(movie_info)

    print(l)
    return l

#la recommendation des films avec le nom et le genre
def load_movie_info(movie_path, genre_path):
    # Charger les informations de films.
    movie_info = pd.read_csv(movie_path, sep='|', header=None, encoding='ISO-8859-1', engine='python', index_col=False)
    movie_titles = movie_info.iloc[:, 1]
    movie_genres = movie_info.iloc[:, 5:]

    # Charger les genres.
    genre_info = pd.read_csv(genre_path, sep='|', header=None, encoding='ISO-8859-1', engine='python', index_col=False)
    genre_map = {row[1]: row[0] for row in genre_info.itertuples(index=False)}

    # Créer une liste de genres pour chaque film.
    genre_names = []
    for index, row in movie_genres.iterrows():
        genres_for_movie = [genre_map[idx] for idx, val in enumerate(row) if val == 1]
        genre_names.append(genres_for_movie)

    return movie_titles, genre_names


# Chargement de la matrice P

with open('./models/P_matrix.pkl', 'rb') as f:
    P = pkl.load(f)
with open('./models/Q_matrix.pkl', 'rb') as f:
    Q = pkl.load(f)

if __name__ == "__main__":

    data_path = './data/u.data'
    user_id = 5
    k = 2
    run_als_and_get_recommendations_with_titles(P, Q, data_path, user_id, k, train=True)

