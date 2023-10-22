import random

def random_counts(n):
    d = dict()
    
    while len(d) < n+1:
        x = random.randint(0, n)
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    return d

def frequencies(d):
    keys = list(d.keys())
    keys.sort()
    for x in keys:
        print(x, ':', d[x])

def main():
    random.seed(7)
    d = random_counts(10000)
    max = 0
    count = 0
    for x in d:
        count += d[x]
        if d[x] > max:
            max =  d[x]
    print('count:', count)
    print('max:', max)

    l = []

    for x in d:
        if d[x] == max:
            l.append(x)
    
    l.sort()
    print(l)

    frequencies(d)

main()