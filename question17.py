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

def main():
    print(equivalent([1,2,3], range(1, 4)))

main()