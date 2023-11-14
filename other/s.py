from surprise import Dataset
from surprise import Reader
from surprise import AlgoBase
from surprise.model_selection import cross_validate
from surprise.prediction_algorithms.matrix_factorization import ALS

# Chargement des données
reader = Reader(line_format='user item rating timestamp', sep='\t')
data = Dataset.load_from_file('u.data', reader=reader)

# Définition de l'algorithme ALS
algo = ALS(n_factors=20, reg_u=12, reg_i=5)

# Évaluation de l'algorithme en utilisant la validation croisée
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)

# Entraînement de l'algorithme sur l'ensemble de données
trainset = data.build_full_trainset()
algo.fit(trainset)

