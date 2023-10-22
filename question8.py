def make_list(a, b, c):
    return [a, b, c]

def nth_list(seq, n):
    l = list(seq)
    list_to_return = []
    for i in range(n - 1, len(l),  n):
        list_to_return.append(l[i])
    return list_to_return


def main():
    l = make_list(1,2,3)
    print(l)

    l = nth_list(range(1,  11), 2)
    print(l)
    l = nth_list("Hahahahahaha", 2)
    print(l)

main()