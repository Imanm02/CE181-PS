for LItem, ZItem in zip(LList, ZList):
    if LItem == realL:
        print("found a perfect Z", ZItem)
        print("min hamming distance is", min_hamming_distance(ZItem, z, k))