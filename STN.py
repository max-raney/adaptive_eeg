from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt

"""
dataset = "Place data here"

dataset = np.loadtxt(dataset)
"""

components = 2


dataset = np.random.randn(1024, 2048)

tsne = TSNE(n_components=components)
tsne_result = tsne.fit_transform(dataset)

plt.scatter(tsne_result[:, 0], tsne_result[:, 1])

plt.grid(True)

plt.show()