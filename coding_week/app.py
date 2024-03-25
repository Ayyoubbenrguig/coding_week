from flask import Flask, render_template, request, redirect, url_for, flash
import model

data_path = './data/u.data'
user_id = 5
k = 2

app = Flask(__name__)
app.secret_key = '123456789'

utilisateur_fictif = {'username': 'ecc', 'password': 'ecc'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # Récupérer les données du formulaire
    username = request.form['username']
    password = request.form['password']

    # Vérifier si l'utilisateur et le mot de passe correspondent à l'utilisateur fictif
    if username == utilisateur_fictif['username'] and password == utilisateur_fictif['password']:
        # Authentification réussie, rediriger vers la page principale
        flash('Authentification réussie !', 'success')
        return redirect(url_for('main'))
    else:
        # Authentification échouée, afficher un message d'erreur
        flash('Authentification échouée. Veuillez réessayer.', 'error')
        return redirect(url_for('index'))


@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        # Traitement des données du formulaire
        user_id = int(request.form['user_id'])
        # Effectuez vos calculs ici pour recommander des films en fonction de user_id
        top_movies = model.run_als_and_get_recommendations_with_titles(model.P, model.Q, data_path, user_id, k)

        # Puis, retournez les résultats
        return render_template('main.html', top_movies=top_movies)  # Remplacer top_movies par vos résultats
    else:
        # Si la méthode n'est pas POST, renvoyer simplement la page main.html sans données
        return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
