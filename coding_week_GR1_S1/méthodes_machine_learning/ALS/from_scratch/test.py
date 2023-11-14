# Ce code permet de tester l'entraînement du modèle avec le fichier ALS_from_scratch

import pickle
import numpy as np

with open('ALS_matrices.pkl', 'rb') as file:
    P = pickle.load(file)
    Q = pickle.load(file)

while True:
    # Récupération de l'id de l'utilisateur et du film pour évaluer le modèle
    test_user = int(input("Entrer un id d'utilisateur : "))
    test_item = int(input("Entrer un id de film : "))

    # Predir la notation
    predicted_rating = np.dot(P[test_user-1], Q[test_item-1])

    print('Evaluation prédit pour l\'utilisateur {} sur le film {} for user on item: {:.2f}\n'.format(test_user, test_item, predicted_rating))



