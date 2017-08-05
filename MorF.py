from sklearn import tree
import numpy as np
import pandas as pd
import csv


#[height, weight, shoe size]
# On charge le dataset

data = pd.read_csv('test.csv', sep=";")
data = pd.DataFrame(data)


#récuperer le nombre de ligne du dataset
n = len(data) 
#création d'une liste qu'on va remplir (mensuration)
maliste = list() 

#remplissage de la liste crée précedemment
for row in range(n): 
	liste_mensuration = np.array([data.taille[row], data.poids[row] , data.shoe_size[row]])
	maliste.append(liste_mensuration)

#création de l'objet arbre de décision
clf = tree.DecisionTreeClassifier() 

#lecture des data pour l'apprentissage
clf = clf.fit(maliste, data.sexe)

#prédiction des nouvelles valeurs
prediction = clf.predict([[155, 60, 39]])

#affichage du résultat prédit
print (prediction)

