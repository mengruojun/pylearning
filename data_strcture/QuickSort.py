def quickSort(lyst):
    if(len(lyst) <= 1):
        return lyst
    pivot_i = 0
    pivot = lyst[pivot_i]
    small, big = [], []

    for i in range(1, len(lyst)):
        if(lyst[i] < pivot):
            small.append(lyst[i])
        else:
            big.append(lyst[i])

    return quickSort(small) + [pivot] + quickSort(big)


def main():
    u_list = input("input a list of init\n")
    u_list = list(map(int,u_list.split(",")))
    print (quickSort(u_list))

if __name__ == '__main__':
    main()