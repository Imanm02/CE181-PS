from random import random
import networkx as ntx

N=100
n=50
p=0.34

def gen_graph(n, p) -> ntx.Graph:
	G=ntx.empty_graph(n)
	for i in range(n):
		for j in range(i):
			if random()<p:
				G.add_edge(i, j)
	return G

def simul():
	G=gen_graph(n, p)
	return ntx.diameter(G)

results=[simul() for i in range(N)]
average=sum(results)/N
print(average)


