import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
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

def conductivity(A, z, s):
    cs = 0
    ms = 0
    for i in range(len(A)):
        if z[i] == s:
            for j in range(len(A)):
                if A[i][j] == 1:
                    if z[j] == s:
                        ms += 1
                    else:
                        cs += 1
    return cs / (ms + cs)


def mean_conductivity(A, z):
    sum = 0
    counter = 0
    for i in range(np.min(z), np.max(z) + 1):
        sum += conductivity(A, z, i)
        counter += 1

    return sum / counter


if __name__ == "__main__":
    G = nx.karate_club_graph()
    n = len(G.nodes)

    A = [[0 for i in range(n)] for j in range(n)]
    for i in G.edges:
        A[i[0]][i[1]] = 1
        A[i[1]][i[0]] = 1

    V = np.array(spectral_cluster(A, 2)).T

    conductivities = []
    for k in range(2, 11):
        kmeans = KMeans(n_clusters=k, random_state=0, n_init="auto").fit(V)
        conductivities.append(mean_conductivity(A, kmeans.labels_ + 1))

    plt.plot(range(2, 11), conductivities)
    plt.xlabel("clusters count")
    plt.ylabel("mean conductivity")
    plt.show()
