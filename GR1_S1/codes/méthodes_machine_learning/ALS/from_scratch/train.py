"""
Ce code python permet d'entraîner un modèle de machine learning pour un système de recommandation
en utilisant la factorisation de matrice avec l'algorithme ALS (Alternative Least Square)
Ce programme n'utilise aucune bibliothèque pour l'entraînement, il utilise seulement les formules mathématiques du modèle et numpy
"""

import numpy as np
import pickle

# Chargement des données avec numpy
data = np.genfromtxt('ml-100k/u1.base', delimiter='\t', dtype=int)

# Nombre K des caractéristiques latentes qui doit etre trés inférieur au nombre des ilisateur pour un choix optimale.
K = 20     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
# Nombre Lambda pour le parametre de regularistion 
Lambda = 0.1

# Nombre N des utilisateurs et le nombre M des films
N = int(np.max(data[:, 0]))
M = int(np.max(data[:, 1]))

# Création des matrices P et Q de tailles réspectives (N, K) et (M, K) avec des nombres aléatoires 
P = np.random.rand(N, K)
Q = np.random.rand(M, K)

# Initialisation de l'erreur epsilon et du seuil delta
epsilon = 0.001
delta = 1e-4

# Nombre d'itérations que fait le programme d'entraînement
iter = 1

print("Début de l'entraînement...\n")


# Répéter le nombre d'itération 10 fois
for it in range(iter):
    # Mise à jour de la matrice P
    for u in range(N):
        Ru = data[:, 0] == (u + 1)
        if np.sum(Ru) > 0:
            YRu = Q[data[Ru, 1] - 1, :]
            P[u, :] = np.linalg.solve(np.dot(YRu.T, YRu) + Lambda * np.eye(K), np.dot(YRu.T, data[Ru, 2]))

    # Mise à jour de la matrice Q
    for i in range(M):
        Ri = data[:, 1] == (i + 1)
        if np.sum(Ri) > 0:
            XTi = P[data[Ri, 0] - 1, :]
            Q[i, :] = np.linalg.solve(np.dot(XTi.T, XTi) + Lambda * np.eye(K), np.dot(XTi.T, data[Ri, 2]))

    # Afficher l'erreur de l'entraînement
    train_error = 0.0
    for i in range(data.shape[0]):
        n = data[i, 0] - 1
        m = data[i, 1] - 1
        rating = data[i, 2]
        train_error += (rating - np.dot(P[n], Q[m]))**2
    train_error /= data.shape[0]
    print('Erreur d\'entraînement après l\'itération %d est de : %.4f' % (it+1, train_error))

with open('ALS_matrices.pkl', 'wb') as file:
    pickle.dump(P, file, pickle.HIGHEST_PROTOCOL)
    pickle.dump(Q, file, pickle.HIGHEST_PROTOCOL)


# Teste du modèle
print("\n---Entraînement du modèle fini---\n")

if input("Voulez vous tester le modèle (y/n).") in ["y", "Y", "1"]:
    while True:
        # Récupération de l'id de l'utilisateur et du film pour évaluer le modèle
        test_user = int(input("Entrer un id d'utilisateur : "))
        test_item = int(input("Entrer un id de film : "))

        # Predir la notation
        predicted_rating = np.dot(P[test_user-1], Q[test_item-1])

        print('Evaluation prédit pour l\'utilisateur {} sur le film {} for user on item: {:.2f}\n'.format(test_user, test_item, predicted_rating))
