#!/usr/bin/env python
# coding: utf-8

# In[27]:


#!/usr/bin/env python3
#!pip install pylbc
import pylbc
import pandas as pd
from datetime import date
import numpy as np

dataBase=pd.read_csv('dataBaseOlonne.csv')

newFile=pd.read_csv('resultatOlonne.csv')

#On met la colonne nouvel article sur 0 en prevision de la comparaision avec les nouveaux articles
dataBase['nouvelArticle']=0

dataBase=dataBase.append(newFile)

#On teste si les articles apparaissent 2 fois dans la BDD
dataBase['articleEnDouble']=dataBase.duplicated(['url'],keep=False)

#Si un article ancien n'apparait plus dans la nouvelle recherche il est vendu, on l'identifie et on note la date
dataBase['articleVendu']=np.where((dataBase['nouvelArticle']==0 )& (dataBase['articleEnDouble']==False),1,0)
dataBase['statutArticle']=np.where(dataBase['articleVendu']==1,'Vendu',dataBase['statutArticle'])
dataBase['dateVente']=np.where(dataBase['articleVendu']==1,date.today(),dataBase['dateVente'])

#Si un article est dans les 2 BDD on le supprime
dataBase['articleEnDouble']=np.where((dataBase['nouvelArticle']==1) & (dataBase['articleEnDouble']==True),1,0)

dataBase=dataBase[dataBase['articleEnDouble']==0]

dataBase.to_csv('dataBaseOlonne.csv',index=False)

