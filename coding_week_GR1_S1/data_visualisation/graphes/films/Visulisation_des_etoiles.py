# Ce bout code python permet de calculer le nombre de notations à un 1, 2, .., 5 points,
# il ne s'execute qu'une seule fois, changer executer à True pour le faire

executer = False
if executer:
    L = [1, 2, 3, 4, 5]
    for k in L:
        count = 0
        with open("ml-100k/u.item", "r", encoding='ISO-8859-1') as f: 
            for line in f:
                words = line.split()
                if len(words) >= 3 and words[2] == str(k):
                    count += 1
                print(f"Le nombre {k} apparaît {count} fois dans le fichier.")

"---------------------------------------------------------------"
"---------------------------------------------------------------"
"---------------------------------------------------------------"
"---------------------------------------------------------------"

# Ce code permet de créer un diagramme circulaire qui affiche les proportions des votes pour chaque note de 1 à 5

import matplotlib.pyplot as plt

label = ["✭", "✭✭", "✭✭✭", "✭✭✭✭", "✭✭✭✭✭"]
size = [(6110/100000)*100 , (11370/100000)*100, (27145/100000)*100, (34174/100000)*100 , (21201/100000)*100] 
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', "red"]

plt.pie(size, labels=label, colors=colors, autopct='%1.1f%%')
title = plt.title("Titre : Distribution d'évaluations des films")
title.set_color('blue')
title.set_fontweight('bold')
title.set_fontsize(14)
title.set_position([.5, 1.05])

plt.show()