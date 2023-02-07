import numpy as np
import random
from scipy.stats import bernoulli
import networkx
# import networkx

n = 15
k = 3
p = 0.6
q = 0.1
Q = np.arange(k*k, dtype=float).reshape(k,k)
for i in range(k):
    for j in range(k):
        Q[i][j] = p if i==j else q

def create_uniform_z(n,k):
    poeple_at_table = [0 for i in range(k)]
    z = list()
    for i in range(n):
        v = random.randint(1,k)
        while(poeple_at_table[v-1]==n/k): v = random.randint(1, k)
        poeple_at_table[v-1] += 1
        z.append(v)
    return np.array(z)


def create_A():
    z = create_uniform_z(n, k)
    A = np.arange(n*n).reshape(n,n)
    for i in range(n):
        for j in range(n):
            value = int(bernoulli(Q[z[i]-1][z[j]-1]).rvs(1))
            if(i==j): value = 1
            elif(i>j): value = A[j][i]
            A[i][j] = value
    return A,z

for i in range(10):
    A,_ = create_A()
    print(A)