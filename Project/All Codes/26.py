from random import random
import networkx as ntx
import matplotlib.pyplot as plt

p=0.34
N=100

def gen_graph(n, p) -> ntx.Graph:
	G=ntx.empty_graph(n)
	for i in range(n):
		for j in range(i):
			if random()<p:
				G.add_edge(i, j)
	return G

def simul(n):
	G=gen_graph(n, p)
	return sum(list(ntx.triangles(G).values()))//3

def mean_simul(n):
	results=[]
	for i in range(N):
		res=simul(n)
		if res!=None:
			results.append(res)
	
	return sum(results)/len(results)


x=range(10, 101, 10)
y=[mean_simul(n) for n in x]

# print(y)

plt.plot(x, y, color='red')
plt.show()


