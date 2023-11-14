from surprise import NMF
from surprise import Dataset, Reader
from surprise.model_selection import cross_validate

# Load the movielens-100k dataset (download it if needed).
data = Dataset.load_builtin('ml-100k')

# Use the famous NMF algorithm.
algo = NMF()

# Run 5-fold cross-validation and print results.
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=2, verbose=True)

while True:
    # Récupération de l'id de l'utilisateur et du film pour évaluer le modèle
    uid = input("Entrer un id d'utilisateur : ")
    iid = input("Entrer un id de film : ")

    for rating in data.raw_ratings:
            print(rating[0], rating[1])
            # r_ui reçoit la valeur -1 si un utilisateur n'a pas évalué un film et qu'on veut l'estimer
            r_ui=-1
            if rating[0] == uid and rating[1] == iid:
                r_ui = rating[2]
                break

    #get a prediction for specific users and items.
    pred = algo.predict(uid, iid, r_ui=r_ui, verbose=True)
