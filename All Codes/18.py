from random import random
import matplotlib.pyplot as plt

n=1000
p=0.00016
N=10

def simul():
	deg=[0]*n
	for i in range(n):
		for j in range(i):
			if random()<p:
				deg[i]+=1
				deg[j]+=1
	L=sum(deg)/n
	res=0
	for i in range(n):
		if (deg[i]<L):
			res+=1
	return res

results=[simul() for i in range(N)]
average=sum(results)/N
print(average)


deg=[0]*n
for i in range(n):
	for j in range(i):
		if random()<p:
			deg[i]+=1
			deg[j]+=1
plt.hist(deg)
plt.show()

