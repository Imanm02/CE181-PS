def permutation(lst):
    if len(lst) == 0:
        return []
 
    if len(lst) == 1:
        return [lst]
 
    l = [] # empty list that will store current permutation
 
    for i in range(len(lst)):
       m = lst[i]
 
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l


def hamming_distance(a:np.array,b:np.array):
    return int(np.linalg.norm(a - b,ord=0))
    
def get_class_of_vector(a:np.array, n:int):
    nlist = list(range(1,n+1))
    aClass = list()
    for p in permutation(nlist):
        aCopy = a.copy()
        for i,v in enumerate(aCopy):
            aCopy[i] = p[v-1]
        aClass.append(aCopy)
    return aClass

def min_hamming_distance(a:np.array, b:np.array, k:int): # k table counts
    aClass = get_class_of_vector(a, k)  
    return min(list([ hamming_distance(x,b) for x in aClass]))
        
print(min_hamming_distance(a, b, 2))