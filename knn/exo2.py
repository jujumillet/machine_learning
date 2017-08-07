import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_mldata
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

mnist = fetch_mldata('MNIST original', data_home='./scikit_learn_data')

num_samples = 5000
sample = np.random.randint(mnist.data.shape[0], size=num_samples)
X  = mnist.data[sample]
y = mnist.target[sample]

sample_viz = X.reshape((-1, 28, 28))
"""
for index, val in enumerate(np.random.randint(num_samples, size=16)):
	plt.subplot(4,4, index+1)
	plt.axis('off')
	plt.imshow(sample_viz[val], cmap=plt.cm.gray_r, interpolation="nearest")
	plt.title('%i'%y[val])
plt.show()
"""
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, train_size=0.7)

#knn = KNeighborsClassifier(3)

#knn.fit(Xtrain, ytrain)

#print (knn.predict(Xtrain[10:15]))
#print (ytrain[10:15])

#print (1-knn.score(Xtest, ytest)) #1-knn.score = l'erreur

krange = range(2,15)
errors = []
for k in krange:
	knn = KNeighborsClassifier(k)
	knn.fit(Xtrain, ytrain)
	errors.append(1-knn.score(Xtest, ytest))

plt.plot(krange, errors)
plt.show()