from sklearn import tree
import numpy as np
import pandas as pd
import csv


#[height, weight, shoe size]
# On charge le dataset

print ("************************************************************")
print ("Bienvenue sur le premier test de machine learning")
print ("************************************************************")

taille = input("Veuillez saisir la taille en centimètres : ")
poids = input("Veuillez saisir le poids en kilo : ")
pointure = input("Veuillez saisir la pointure : ")

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
prediction = clf.predict([[taille, poids, pointure]])

#affichage du résultat prédit
print ("La personne en question est donc probablement : ")
print (prediction)

