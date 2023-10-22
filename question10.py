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

def fizz_bubzz_list():
    l = [x for x in range(1, 101) if x%3==0 or x%5==0]
    print(l)

def multiples(seq, n):
    l = [x for x in range(len(seq)) if x%n==0]
    print(l)

def only_vowels(a_string):
    l = [x for x in a_string if x in ('a', 'e', 'i', 'o', 'u')]
    print(l)

def main():
    only_vowels("Humpty Dumpty sat on a wall eating his curds and whey")



main()