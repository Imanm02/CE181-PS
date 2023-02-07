
def get_z0(n,k):
    result = list()
    for i in range(int(k)):
        for j in range(int(n/k)):
            result.append(i+1)
    # print("z0 is:", result)
    return np.array(result)

# Q7
def z_fit(A, realz, z0=get_z0(n, k),):
    dlist = list()
    # z0 = get_z0(n, k)
    if len(z0) != n:
        # print("FAAALSE!")
        pass
    T = 5
    bestL = 1e9
    for t in range(T):
        initial_L = Liklyhood(A, z0)
        bestL = initial_L
        MaxDelta = 0
        best = (0,0)
        for i in range(n):
            for j in range(n):
                temp = z0[i]
                z0[i] = z0[j]
                z0[j] = temp
                delta = initial_L - Liklyhood(A, z0)
                if delta > MaxDelta:
                    MaxDelta = delta
                    best = (i,j)
                    bestL = initial_L - delta
                temp = z0[i]
                z0[i] = z0[j]
                z0[j] = temp
        if best[0]==0:
            print("not completed")
            break
        temp = z0[best[0]]
        z0[best[0]] = z0[best[1]]
        z0[best[1]] = temp
        dlist.append(min_hamming_distance(z0, realz, k))
    return bestL, z0, dlist

A, z0 = create_A()
bestL, z, dlist = z_fit(A, z0)
dlist