from collections import Counter 
def isSubset( a1, a2, n, m): 
    if m == len(set(a2)): 
        if set(a2) <= set(a1): 
            return ('Yes') 
        else:  
            return ('No') 
    count_hash_a2 = Counter(a2) 
    count_hash_a1 = Counter(a1) 
    for item, freq in count_hash_a2.items(): 
        if freq > 1: 
            if count_hash_a1[item] < freq: 
                return ('No') 
    return ('Yes')      