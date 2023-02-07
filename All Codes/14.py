import random
from math import ceil
from sklearn.datasets import fetch_california_housing
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def second_smallest_index(arr):
    import math
    first = second = math.inf
    i_first = i_second = 0

    for i in range(0, len(arr)):
        if arr[i] < first:
            second = first
            i_second = i_first
            first = arr[i]
            i_first = i
        elif arr[i] < second and arr[i] != first:
            second = arr[i]
            i_second = i
    return i_second


def cluster(n):
    p = 0.1
    q = 0.01
    a_array = [[0] * n for _ in range(n)]
    w_array = [[0] * n for _ in range(n)]
    real_clusters = np.random.choice([-1, 1], size=(n,), p=[0.5, 0.5])

    for j in range(n):
        for i in range(n):
            if real_clusters[i] == real_clusters[j]:
                w = p
                a = random.choices([0, 1], weights=(1 - p, p))[0]
            else:
                w = q
                a = random.choices([0, 1], weights=(1 - q, q))[0]
            w_array[i][j] = w
            a_array[i][j] = a

    A = np.matrix(a_array)
    W = np.matrix(w_array)
    discovered_clusters_a = discover_clusters(A, n)
    discovered_clusters_w = discover_clusters(W, n)
    a_errors = min(
        sum(discovered_clusters_a[i] != real_clusters[i] for i in range(n)),
        sum(discovered_clusters_a[i] == real_clusters[i] for i in range(n))
    )
    w_errors = min(
        sum(discovered_clusters_w[i] != real_clusters[i] for i in range(n)),
        sum(discovered_clusters_w[i] == real_clusters[i] for i in range(n))
    )
    print("A errors: ", a_errors)
    print("W errors: ", w_errors)


def discover_clusters(ma, n):
    degree = np.zeros(len(ma))
    row_sum = ma.sum(axis=1)
    for j in range(n):
        degree[j] = row_sum[j, 0]
    D = np.diag(degree)
    L = D - ma
    w, v = np.linalg.eig(L)
    u2 = v[:, second_smallest_index(w)]
    discovered_clusters = [ceil(x.real) * 2 - 1 for x in u2]
    return discovered_clusters

california_housing = fetch_california_housing(as_frame=True)
med_incs = np.array(california_housing.data[:]['MedInc']).reshape(-1, 1)
kmeans = KMeans(n_clusters=3, random_state=0, max_iter=1000, n_init="auto").fit(med_incs)
labels = kmeans.labels_
colors = [label + 100 for label in labels]
df = pd.DataFrame(data=california_housing.data, columns=california_housing.feature_names)
df.plot(kind='scatter', x='Latitude', y='Longitude', color=colors, alpha=0.5)
plt.savefig('number14_figure.png')