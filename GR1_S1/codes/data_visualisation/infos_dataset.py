# Ce progaramme permet de visualiser certaines données présentent dans le dataset ml-100K, et la matrice R (users/items)

import pandas as pd
import numpy as np
from scipy import sparse

# Chargement des notation du fichier u.data
ratings_df = pd.read_csv('ml-100k/u.data',encoding="ISO-8859-1", sep='\t', names=['user_id', 'item_id', 'rating', 'timestamp'])

# Chargement des informations du fichier u.item
item_info = pd.read_csv('ml-100k/u.item',encoding="ISO-8859-1", sep='|', header=None, usecols=[1])   # Information about the items (keeps only movie's name)
item_info.columns = ['title']

# Calcul du nombre d'utilisateurs et de films dans le dataset
num_users = len(ratings_df['user_id'].unique())
num_films = len(ratings_df['item_id'].unique())
R_shape = (num_users, num_films)
print(f"Il y a {num_users} utilisateurs dans la base de données u.data")
print(f"Il y a {num_films} films dans la base de données u.data")

# Création de X qui contient les deux colonnes 'user_id' et 'item_id' et y et contient 'rating'
X = ratings_df[['user_id', 'item_id']].values
y = ratings_df['rating'].values
  
n_users = len(ratings_df['user_id'].unique())
n_items = len(ratings_df['item_id'].unique())
R_shape = (n_users, n_items)

# Création de la matrice R
row  = X[:,0]
col  = X[:,1]
data = y
matrix_sparse = sparse.csr_matrix((data,(row,col)), shape=(R_shape[0]+1,R_shape[1]+1))  # sparse matrix in compressed format (CSR)
R = matrix_sparse.todense()   # convert sparse matrix to dense matrix, same as: matrix_sparse.A
R = R[1:,1:]                  # removing the "Python starts at 0" offset
R = np.asarray(R)             # convert matrix object to ndarray object

# Calcule du taux de remplissage de la matrice R
taux_de_remplissage_R = len(R.nonzero()[0]) / float(R.shape[0] * R.shape[1])
print("\nLa matrice R (users/items) : ")
print(R)
print(f"\n{taux_de_remplissage_R*100:.4f}% de la matrice est réellement remplie, le reste ne contient que des zéros")



