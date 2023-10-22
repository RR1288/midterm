def sort_key(a):
    return a%2 == 0

def odds_before_evens(a_list):
    a_list.sort(key=sort_key)

def splice(a, b):
    for i in range(len(b)):
        a.append(b[i])

def scramble(a_string):
    l = []
    for i in range(len(a_string)):
        l.append(a_string[i:i+1])
    backwards = ''
    for i in range(len(l)):
        a = (l[len(l)-i - 1:len(l)-i])
        backwards += a[0]
    print(backwards)
    return backwards


def main():
    l = [3,4,1,2,5]
    b = ['a', 'b']
    print(l)
    odds_before_evens(l)
    print(l)

    splice(l, b)
    print(l)

    l = 'This is a scramble test'
    l = scramble(l)
    l = scramble(l)



main()