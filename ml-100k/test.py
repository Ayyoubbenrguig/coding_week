# ouverture du fichier pour les films pour avoir les noms
dico_films = {}
with open("u.item", "r") as fichier_films:
    for ligne in fichier_films:
        ligne_donnée = ligne.split("|")
        dico_films[ligne_donnée[0]] = ligne_donnée[1]
    #print(dico_films)

# ouverture du fichier pour les notations
with open("u.data", "a+") as fichier_notations:
    with open("uf.data", "w") as fichier_nouveau:
        for ligne in fichier_notations:
            print(ligne)
            ligne_donnée = ligne.split("|")
            print(ligne_donnée)

            ligne_donnée[1] = dico_films[ligne_donnée[1]]
            print("   ".join(ligne_donnée))
