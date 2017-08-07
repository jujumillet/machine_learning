# On importe les librairies dont on aura besoin pour ce tp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# On charge le dataset
house_data = pd.read_csv('house.csv')

# On décompose le dataset et on le transforme en matrices pour pouvoir effectuer notre calcul
X = np.matrix([np.ones(house_data.shape[0]), house_data['surface'].as_matrix()]).T
y = np.matrix(house_data['loyer']).T


# On effectue le calcul exact du paramètre theta
theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
print(theta)
# On affiche le nuage de points dont on dispose et la droite
plt.plot(house_data['surface'], house_data['loyer'], 'ro', markersize=2)
#[les extrèmes] [ordonnées à l'origine, equation]
plt.plot([0, 250], [theta.item(0), theta.item(0) + 250 * theta.item(1)])
plt.show()
