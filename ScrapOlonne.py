#!/usr/bin/env python
# coding: utf-8

# In[2]:


#!/usr/bin/env python3
import pylbc
import pandas as pd
from os import path

lat_paris, lng_paris = 46.50, -1.78333
radius = 10 # in kilometers

query = pylbc.Search()
query.set_price(mini=800000, maxi=900000)
query.set_category('ventes')
query.set_real_estate_types(['maison'])

# option 1: faire une recherche autour d'un point donné (ici, paris) dans un rayon donné (ici 50kms)
query.set_coordinates(lat=lat_paris, lng=lng_paris, radius=radius)

# option 2 : recherche par départements, ici toute la bretagne :-)
# query.set_departments(['22', '56', '35', '29'])

# affichage de la requete avant envoi
query.show_filters()

# pré-requête pour récupérer les métadonnées
infos = query.request_infos()
print(infos)
#infos2 = query.request_once()
#print(infos2)
print("A total of %d results is announced by the server." % infos['total'])

resultatOlonne=pd.DataFrame()
# récupération et affichage de tous les résultats
for result in query.iter_results():
    print(result)
    
    data = [{'title': result.title, 'publication_date': result.publication_date, 'price': result.price, 'real_estate_type': result.real_estate_type, 'square': result.square, 'url': result.url, 'thumbnail': result.thumbnail,'coordinates': result.coordinates}]
    resultatOlonne=resultatOlonne.append(data)

resultatOlonne['statutArticle']='En vente'
resultatOlonne['nouvelArticle']=1
resultatOlonne['dateVente']=0
resultatOlonne.to_csv('resultatOlonne.csv',index=False)

#Si la BDD n existe pas on la cree
if not path.exists('dataBaseOlonne.csv'):
    resultatOlonne.to_csv('dataBaseOlonne.csv',index=False)
    

