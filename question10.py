def sort_key(a):
    return a%2 == 0

def odds_before_evens(a_list):
    a_list.sort(key=sort_key)

def splice(a, b):
    for i in range(len(b)):
        a.append(b[i])

def main():
    l = [3,4,1,2,5]
    b = ['a', 'b']
    print(l)
    odds_before_evens(l)
    print(l)

    splice(l, b)
    print(l)


main()