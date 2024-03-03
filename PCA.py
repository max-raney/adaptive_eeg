from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

"""
dataset = "Place data here"

dataset = np.loadtxt(dataset)
"""

components = 2


dataset = np.random.randn(1024, 2048)

pca = PCA(n_components=components)
pca.fit(dataset)
pca_result = pca.transform(dataset)

explained_variance = pca.explained_variance_ratio_


plt.figure(figsize=(10, 6))

plt.xlabel('PCA-1')
plt.ylabel('PCA-2')

plt.scatter(pca_result[:, 0], pca_result[:, 1])

plt.grid(True)

plt.show()