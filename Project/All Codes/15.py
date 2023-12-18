import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from sklearn.cluster import KMeans

def spectral_cluster(matrix, k):
    n = len(matrix)
    D = [[0] * n for i in range(n)]
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
        D[i][i] = sum

    L = [[0] * n for i in range(n)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            L[i][j] = D[i][j] - matrix[i][j]

    u, v = np.linalg.eig(L)
    indices = np.argsort(u)[1:]
    V = []
    for i in range(k):
        V.append(v[:, indices[i]])

    return np.real(V)

G = nx.karate_club_graph()
n = len(G.nodes)

A = [[0 for i in range(n)] for j in range(n)]
for i in G.edges:
    A[i[0]][i[1]] = 1
    A[i[1]][i[0]] = 1

V = np.array(spectral_cluster(A, 2)).T

for k in range(2, 5):
    kmeans = KMeans(n_clusters=k, random_state=0, n_init="auto").fit(V)
    nx.draw(G, node_color=kmeans.labels_+1, with_labels=True)
    plt.show()
