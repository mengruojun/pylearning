def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    pivot_i = 0
    pivot = input_list[pivot_i]
    small, big = [], []

    for i in range(1, len(input_list)):
        if input_list[i] < pivot:
            small.append(input_list[i])
        else:
            big.append(input_list[i])

    return quick_sort(small) + [pivot] + quick_sort(big)


def main():
    u_list = input("input a list of init\n")
    u_list = list(map(int, u_list.split(",")))
    print(quick_sort(u_list))


if __name__ == '__main__':
    main()
