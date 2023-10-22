def swapSort(list):
    swap = True
    while swap:
        swap = False
        for i in range(1, len(list)):
            if list[i] < list[i-1]:
                swap = True
                temp = list[i]
                list[i] = list[i-1]
                list[i-1] = temp

def main():
    list = [5,4,3,6,1]
    print(list)
    swapSort(list)
    print(list)

if __name__  == "__main__":
    main()