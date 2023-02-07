from random import random

n=3000
p=0.01
N=5

def simul():
	G=[[0]*n for i in range(n)]
	for i in range(n):
		for j in range(i):
			if random()<p:
				G[i][j]=G[j][i]=1
	res1=0
	res2=0
	for v in range(n):
		adj=[]
		for u in range(v):
			if G[u][v]:
				adj.append(u)
		res=0
		for u in adj:
			for w in adj:
				if u<w:
					if G[u][w]:
						res1+=1
					else:
						res2+=1
	return res1, res2

mean1=0
mean2=0
for i in range(N):
	res1, res2 = simul()
	mean1+=res1
	mean2+=res2
mean1/=N
mean2/=N
print(mean1)
print(mean2)

