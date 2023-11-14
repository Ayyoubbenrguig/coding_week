from surprise import accuracy, Dataset, SVD
from surprise.model_selection import train_test_split

# Load the movielens-100k dataset (download it if needed),
data = Dataset.load_builtin("ml-100k")

# sample random trainset and testset
# test set is made of 25% of the ratings.
trainset, testset = train_test_split(data, test_size=0.25)

# We'll use the famous SVD algorithm.
algo = SVD()

# Train the algorithm on the trainset, and predict ratings for the testset
algo.fit(trainset)
predictions = algo.test(testset)
#predictions = algo.fit(trainset).test(testset)
# Then compute RMSE
accuracy.rmse(predictions)


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
