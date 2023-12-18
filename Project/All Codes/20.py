from random import random

n=1000
p=0.003

G=[[0]*n for i in range(n)]
for i in range(n):
	for j in range(i):
		if random()<p:
			G[i][j]=G[j][i]=1

mean=0
for v in range(n):
	adj=[]
	for u in range(v):
		if G[u][v]:
			adj.append(u)
	res=0
	for u in adj:
		for w in adj:
			if u<w and G[u][w]:
				res+=1
	mean+=res

mean/=n
print(mean)


