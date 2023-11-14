# Ce code utilise le fichier u.item pour récupérer le nom des films et remplace l'id des films par leurs noms
# dans un fichier uf.data, ceci est pour que les statistiques affiches les noms des films et non pas leurs ids

# ouverture du fichier pour les films pour avoir les noms
dico_films = {}
with open("u.item", "r") as fichier_films:
    for ligne in fichier_films:
        ligne_donnée = ligne.split("|")
        dico_films[ligne_donnée[0]] = ligne_donnée[1]

# ouverture du fichier pour les notations
with open("u.data", "r") as fichier_notations:
    with open("uf.data", "w") as fichier_nouveau:
        for ligne in fichier_notations:
            ligne_donnée = ligne.split("|")
            ligne_donnée[1] = str(dico_films[ligne_donnée[1]])[:-7]
            fichier_nouveau.write("\t".join(ligne_donnée))
