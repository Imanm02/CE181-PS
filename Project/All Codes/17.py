from random import random

n=1000
p=0.0034
m=3000
N=10
def simul():
	edges=0
	for i in range(n):
		for j in range(i):
			if random()<p:
				edges+=1
	return edges

average=0
for i in range(N):
	average+=simul()
average/=N
print(average)