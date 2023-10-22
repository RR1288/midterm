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

def main():
    for i in range(21):
        print(random_search(range(21), i))

main()