import numpy as np
import pickle

# Chargement des données avec numpy
data = np.genfromtxt('ml-100k/u.data', delimiter='\t', dtype=int)

with open('ml-100k/NMF_matrices.pkl', 'rb') as file:
    P = pickle.load(file)
    Q = pickle.load(file)

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

