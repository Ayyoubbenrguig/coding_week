"""
Ce code python permet d'entrainer un modèle de machine learning pour un système de recommandation en utilisant la factorisation de matrice avec l'algorithme NMF
Ce programme n'utilise aucune bibliothèque pour l'entrainement, il utilise seulement les formules mathématiques du modèle et numpy
"""

import numpy as np
import pickle

# Chargement des données avec numpy
data = np.genfromtxt('u1.base', delimiter='\t', dtype=int)

# Nombre K des caractéristiques latentes
K = 20
dico = {}

user = int(input("Entrez l'utilisateur : "))
l = []
g = []
for i in range(data.shape[0]):
    n = data[i, 0] - 1
    m = data[i, 1] - 1
    if n == user:
        l.append(m)

for i in range(data.shape[0]):  
    n = user   
    m = data[i, 1] - 1 
    if m not in l and m not in g:
        rating = data[i, 2]
        error = (rating - np.dot(P[n], Q[m]))**2
        dico[error] = i
        g.append(m)
    else : continue
dico = {k: v for k, v in sorted(dico.items(), key=lambda item: item[0])}

print("--------------------------------")
print("le top 10 des id films pour l'utilisateur {user} est :")
count = 0
for key in dico:
    if count < 10:
        print(dico[key])
    count += 1

dico = {}

user = int(input("Entrez l'utilisateur : "))
l = []
g = []
for i in range(data.shape[0]):
    n = data[i, 0] - 1
    m = data[i, 1] - 1
    if n == user:
        l.append(m)

for i in range(data.shape[0]):  
    n = user   
    m = data[i, 1] - 1 
    if m not in l and m not in g:
        rating = data[i, 2]
        error = (rating - np.dot(P[n], Q[m]))**2
        dico[error] = i
        g.append(m)
    else : continue
dico = {k: v for k, v in sorted(dico.items(), key=lambda item: item[0])}

print("--------------------------------")
print("le top 10 des id films pour l'utilisateur {user} est :")
count = 0
for key in dico:
    if count < 10:
        print(dico[key])
    count += 1

dico = {}

user = int(input("Entrez l'utilisateur : "))
l = []
g = []
for i in range(data.shape[0]):
    n = data[i, 0] - 1
    m = data[i, 1] - 1
    if n == user:
        l.append(m)

for i in range(data.shape[0]):  
    n = user   
    m = data[i, 1] - 1 
    if m not in l and m not in g:
        rating = data[i, 2]
        error = (rating - np.dot(P[n], Q[m]))**2
        dico[error] = i
        g.append(m)
    else : continue
dico = {k: v for k, v in sorted(dico.items(), key=lambda item: item[0])}

print("--------------------------------")
print("le top 10 des id films pour l'utilisateur {user} est :")
count = 0
for key in dico:
    if count < 10:
        print(dico[key])
    count += 1

dico = {}

user = int(input("Entrez l'utilisateur : "))
l = []
g = []
for i in range(data.shape[0]):
    n = data[i, 0] - 1
    m = data[i, 1] - 1
    if n == user:
        l.append(m)

for i in range(data.shape[0]):  
    n = user   
    m = data[i, 1] - 1 
    if m not in l and m not in g:
        rating = data[i, 2]
        error = (rating - np.dot(P[n], Q[m]))**2
        dico[error] = i
        g.append(m)
    else : continue
dico = {k: v for k, v in sorted(dico.items(), key=lambda item: item[0])}

print("--------------------------------")
print("le top 10 des id films pour l'utilisateur {user} est :")
count = 0
for key in dico:
    if count < 10:
        print(dico[key])
    count += 1


# Set the learning rate
gamma = 0.01

# Nombre Lambda pour le paramètre de régularisation 
Lambda = 0.1

# Nombre N des utilisateurs et le nombre M des films
N = int(np.max(data[:, 0]))
M = int(np.max(data[:, 1]))

# Création des matrices P et Q de tailles respectives (N, K) et (M, K) avec des nombres aléatoires 
P = np.random.rand(N, K)
Q = np.random.rand(M, K)

# Nombre d'itérations pour l'entraînement du modèle
iter = 30

print("Début de l'entraînement...\n")

# Entraînement du modèle avec un nombre d'itération de 30
for epoch in range(iter):
    for i in range(data.shape[0]):
        # Récupération de l'id de l'utilisateur, l'id du film et la notation
        n = data[i, 0] - 1
        m = data[i, 1] - 1
        rating = data[i, 2]

        # Afficher l'erreur
        e = rating - np.dot(P[n], Q[m])

        # Mises à jour des matrices P et Q
        P[n] += gamma * (e * Q[m] - Lambda * P[n])
        Q[m] += gamma * (e * P[n] - Lambda * Q[m])

    # Afficher l'erreur pour l’entraînement du modèle
    train_error = 0.0
    for i in range(data.shape[0]):
        n = data[i, 0] - 1
        m = data[i, 1] - 1
        rating = data[i, 2]
        train_error += (rating - np.dot(P[n], Q[m]))**2
    train_error /= data.shape[0]
    print('Erreur d\'entraînement après l\'itération %d, est de : %.4f' % (epoch+1, train_error))

with open('NMF_matrices.pkl', 'wb') as file:
    pickle.dump(P, file, pickle.HIGHEST_PROTOCOL)
    pickle.dump(Q, file, pickle.HIGHEST_PROTOCOL)

if input("Voulez vous tester le modèle (y/n).") in ["y", "Y", "1"]:
    while True:
        # Récupération de l'id de l'utilisateur et du film pour évaluer le modèle
        test_user = int(input("entrer un id d'utilisateur : "))
        test_item = int(input("entrer un id de film : "))

        # Predir la notation
        predicted_rating = np.dot(P[test_user-1], Q[test_item-1])

        # Afficher la notation
        print('Evaluation prédit pour l\'utilisateur {} sur le film {} for user on item: {:.2f}\n'.format(test_user, test_item, predicted_rating))