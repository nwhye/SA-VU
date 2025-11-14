from sklearn.cluster import KMeans, AgglomerativeClustering
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from sklearn import model_selection
from sklearn.decomposition import PCA
import pandas as pd


dataset = pd.read_table("data.txt", delimiter='\t', header=None)

dataset[8] = pd.factorize(dataset[8])[0]

X = dataset.iloc[:, 1:8].values
y = dataset.iloc[:, 8:9].values

y_uniq = np.unique(y)
nt = len(y_uniq)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=1)

pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train, 2)
X_test_pca = pca.fit_transform(X_test, 2)

colours = mcolors.CSS4_COLORS
clrs = list(colours)


def clustering_1(n_k):
    clustering1 = KMeans(n_clusters=n_k)
    clustering1.fit(X_train)

    plt.figure()
    for i, l in enumerate(clustering1.labels_):
        plt.scatter(X_train_pca[i, 0], X_train_pca[i, 1], color=colours[clrs[l]])
    plt.title(f'KMeans{n_k} train')
    plt.show()

    labels = clustering1.predict(X_test)
    print("Data labels: ", labels)
    uni_labs1 = np.unique(labels)
    print(uni_labs1)

    n = len(uni_labs1)
    Ns = np.zeros((n,), dtype=np.int32)
    for i in range(n):
        Ns[i] = np.sum(labels == i)
    print("Elements in each cluster:", Ns)

    plt.figure()
    for i, l in enumerate(labels):
        plt.scatter(X_test_pca[i, 0], X_test_pca[i, 1], color=colours[clrs[l]])
    plt.title(f'KMeans{n_k} test')
    plt.show()

    NNs = np.zeros((n_k, n_k), dtype=np.int32)
    for t, p in zip(y_test, labels):
        NNs[t, p] += 1

    print("Cluster stats:\n", NNs)


clustering_1(8)

clustering_1(12)

clustering_1(16)


def clustering(linkage, n_clusters, distance_threshold):
    clustering = AgglomerativeClustering(linkage=linkage, n_clusters=n_clusters, distance_threshold=distance_threshold)
    clustering.fit(X_test)
    labels = clustering.labels_
    print('Number of clusters:', len(np.unique(labels)))
    uniquelabels = np.unique(labels)
    n = len(uniquelabels)
    Ns = np.zeros((n,), dtype=np.int32)
    for i in range(n):
        Ns[i] = np.sum(labels == i)
    print("Elements in each cluster:", Ns)

    NNs = np.zeros((nt, n), dtype=np.int32)
    for t, p in zip(y_test, labels):
        NNs[t, p] += 1

    print("Cluster stats:\n", NNs)

    plt.figure()
    for i, l in enumerate(clustering.labels_):
        plt.scatter(X_test_pca[i, 0], X_test_pca[i, 1], color=colours[clrs[l]])
    plt.title(f'AC {linkage} (DT: {distance_threshold})')
    plt.show()


clustering('complete', None, 0.5)

clustering('ward', None, 0.53)