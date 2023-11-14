from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row
from pyspark.sql import SparkSession

# initialisation de la session spark
spark = SparkSession.builder.appName("MovieRecommendationALS").getOrCreate()

# lecture des données des évaluations des utilisateurs sur les films
ratings = spark.read.text("ml-100k/u.data").rdd

# conversion des données en format Row
ratings = ratings.map(lambda x: Row(userId=int(x[0]), movieId=int(x[1]),
                                   rating=float(x[2]), timestamp=int(x[3])))

# création du dataframe
ratings_df = spark.createDataFrame(ratings)

# création du modèle ALS
als = ALS(maxIter=10, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating",
          coldStartStrategy="drop")
model = als.fit(ratings_df)

# prédictions pour les utilisateurs et les films non évalués
userRecs = model.recommendForAllUsers(10)

# affichage des prédictions pour l'utilisateur 1
userRecs.filter(userRecs.userId == 1).show()

# évaluation du modèle
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
                                predictionCol="prediction")
predictions = model.transform(ratings_df)
rmse = evaluator.evaluate(predictions)
print("Root-mean-square error = " + str(rmse))