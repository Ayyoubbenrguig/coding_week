# Ce code permet de nettoyer la data des caractères non reconnus concernant le nombre d’occurrences
# des villes à partir de leurs zip codes,
# du fichier u.item, il permet aussi de trier la liste par ordre alphabétique des villes

import pandas as pd  
l = []
with open('codes/data_visualisation/graphes/map_visu_users/data_map.csv', "r") as file, open("codes/data_visualisation/graphes/map_visu_users/data_map_clean.csv", "w") as file2:
    for ligne in file:
        count, ville = ligne.split("\t")
        #print(count, ville[:-2])
        if [count, ville[:-1]] not in l:
            l.append([count, ville[:-1]])
            l = sorted(l, key=lambda x: x[1])
    l = l[1:-1]
    for ville in l:
        ville = "\t".join(ville) + "\n"
        print(ville)
        file2.write(ville)