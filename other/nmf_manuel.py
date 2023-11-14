import numpy as np

# Load the data
data = np.genfromtxt('../ml-100k/u1.base', delimiter='\t', dtype=int)

# Set the number of latent factors
K = 200

# Set the learning rate
gamma = 0.01

# Set the regularization parameter
Lambda = 0.1

# Get the number of users and items
N = int(np.max(data[:, 0]))
M = int(np.max(data[:, 1]))

# Initialize the user and item matrices
P = np.random.rand(N, K)
Q = np.random.rand(M, K)

# Train the model
for epoch in range(200):
    for i in range(data.shape[0]):
        # Get the user ID, item ID, and rating for the current data point
        n = data[i, 0] - 1
        m = data[i, 1] - 1
        rating = data[i, 2]

        # Compute the error
        e = rating - np.dot(P[n], Q[m])

        # Update the user and item matrices
        P[n] += gamma * (e * Q[m] - Lambda * P[n])
        Q[m] += gamma * (e * P[n] - Lambda * Q[m])

    # Compute the training error
    train_error = 0.0
    for i in range(data.shape[0]):
        n = data[i, 0] - 1
        m = data[i, 1] - 1
        rating = data[i, 2]
        train_error += (rating - np.dot(P[n], Q[m]))**2
    train_error /= data.shape[0]
    print('Epoch %d, training error: %.4f' % (epoch+1, train_error))
while True:
    # Get the user ID and item ID for the test point
    test_user = int(input("entrer un id d'utilisateur : "))
    test_item = int(input("entrer un id de film : "))

    # Predict the rating for the test point
    predicted_rating = np.dot(P[test_user-1], Q[test_item-1])

    # Print the predicted rating
    print('Predicted rating for user %d on item %d: %.2f' % (test_user, test_item, predicted_rating))