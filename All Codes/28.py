import math
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def P_t(t, A, D):
    P = np.dot(np.linalg.inv(D), A)

    result = P
    for i in range(t - 1):
        result = np.dot(result, P)
    return result


def R_i_j(n, t, A, D, d, i, j):
    result = 0
    P = P_t(t, A, D)
    for k in range(n):
        result += ((P[i][k] - P[j][k]) ** 2) / d[k]
    return math.sqrt(result)


def P_Ci(P, ci, A, k):
    result = 0
    for i in ci:
        result += P[i][k]

    return result / len(ci)


def RC_iC_j(n, t, A, D, d, C1, C2):
    P = P_t(t, A, D)
    result = 0
    for k in range(n):
        result += ((P_Ci(P, C1, A, k) - P_Ci(P, C2, A, k)) ** 2) / d[k]
    return math.sqrt(result)


G = nx.karate_club_graph()
n = len(G.nodes)
t = 2

A = [[0 for i in range(n)] for j in range(n)]

edgesTotal = 0
for i in G.edges:
    edgesTotal += 1
    A[i[0]][i[1]] = 1
    A[i[1]][i[0]] = 1

D = [[0 for i in range(n)] for j in range(n)]
d = []
for i in range(n):
    s = sum(A[i])
    d.append(s)
    D[i][i] = s

C = []
for i in range(n):
    c = []
    c.append(i)
    C.append(c)

diffs = []

edgesIn = []
edgesOut = []

while len(C) > 1:
    first = 0
    second = 0
    minOfDif = 1e7
    for i in range(len(C)):
        for j in range(i):
            r = RC_iC_j(n, t, A, D, d, C[i], C[j])
            if minOfDif > r:
                minOfDif = r
                first = i
                second = j

    edIn = 0
    edOut = 0
    for i in range(len(C)):
        for j in range(len(C[i])):
            for z in range(j):
                if A[j][z] == 1:
                    edIn += 1

    edOut = edgesTotal - edIn

    edgesIn.append(edIn)
    edgesOut.append(edOut)

    cfirst = C.pop(first)
    csecond = C.pop(second)
    C.append(cfirst + csecond)

    r = 0
    for i in range(len(C)):
        for j in range(i):
            r += RC_iC_j(n, t, A, D, d, C[i], C[j])

    diffs.append(r)

    if 2 * edOut <= edIn:
        color_map = []
        for node in G:
            counter = 0
            for i in range(len(C)):
                if counter == 0:
                    for j in C[i]:
                        if j == node and counter == 0:
                            color_map.append(i)
        nx.draw(G, node_color=color_map, with_labels=True)
        plt.show()
        plt.clf()
        break

edIn = 0
edOut = 0
for i in range(len(C)):
    for j in range(len(C[i])):
        for z in range(j):
            if A[j][z] == 1:
                edIn += 1

edOut = edgesTotal - edIn

edgesIn.append(edIn)
edgesOut.append(edOut)

print(edgesIn)
print(edgesOut)