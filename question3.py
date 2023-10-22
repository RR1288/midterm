def make_tuple(a, b, c):
    return tuple([a, b, c])

def reverse_tuple(seq):
    seq_list = list(seq)
    rev_list = []
    while len(seq_list) > 0:
        rev_list.append(seq_list.pop())
    return tuple(rev_list)



def main():
    tup = make_tuple(1,  2, 3)
    print(tup)
    rev_tup = reverse_tuple((1,2,3))
    print(rev_tup)
    rev_tup = reverse_tuple("Hola")
    print(rev_tup)
    rev_tup = reverse_tuple(range(20))
    print(rev_tup)

if __name__  == "__main__":
    main()