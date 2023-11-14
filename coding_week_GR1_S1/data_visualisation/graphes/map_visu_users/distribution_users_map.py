# Ce code permet de générer une carte des états unis, où est affichée la localisation de tout les utilisateurs
# Ce dataset vient initialement du site web site pour la database des (zip code | longitude | latitude) des USA : https://simplemaps.com/static/data/us-zips/1.82/basic/simplemaps_uszips_basicv1.82.zip,
# qui donne la villes des USA correspondante au zip code provenant du fichier u.user,
# Avec Microsoft Excel, on a calculé le nombre d’occurrence de chaque ville, et avec l'api "https://nominatim.openstreetmap.org/search?q=<ville>, USA&format=geojson"
# on a convertit la ville en (latitude/longitude)
# Finalement avec le module folium, on a créer le fichier le fichier "carte_USA" qui affiche les points sur la carte des états unis 

import folium
import pandas as pd

# Charger les données depuis le fichier CSV
data = pd.read_csv('codes/data_visualisation/graphes/map_visu_users/data_map_clean.csv', delimiter='\t', header=None, names=['occurrences', 'ville'])

# Créer une carte centrée sur les USA
map = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

# Ajouter des marqueurs pour chaque ville
for index, row in data.iterrows():
    print(index, row["ville"])
    popup_text = f"Occurences: {row['occurrences']}"
    geocode = folium.GeoJson(data=f'https://nominatim.openstreetmap.org/search?q={row["ville"]}, USA&format=geojson').add_to(map)
    geocode.add_child(folium.Popup(popup_text))

# Afficher la carte
map.save('map.html')
