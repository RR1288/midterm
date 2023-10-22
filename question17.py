import random

def random_search(a_list, value):
    idxs = list(range(len(a_list)))
    found = False
    while not found and len(idxs) > 0:
        rand_idx = random.randint(0, len(idxs)-1)
        if(a_list[idxs[rand_idx]] == value):
            found == True
            return idxs[rand_idx]
        else:
            idxs.pop(rand_idx)
    return None       

def equivalent(seqA, seqB):
    s = set(seqA)
    
    for i in range(len(seqB)):
        s.add(seqB[i])

    for x in s:
        if x not in seqA:
            return False
    for x in s:
        if x not in seqB:
            return False     
    return True

def disjoint(setA, setB):
    for x in setA:
        if x in setB:
            return False
    return True

def union(setA, setB):
    #union is a_set + b_set, they look for intersection
    s = set()
    for x in setA:
        if x in setB:
            s.add(x)
    if len(s) == 0:
        return None
    return s


def main():
    print(union([1,2,3], range(4, 6)))

main()