def merge_sort(lyst):
    if len(lyst) == 1:
        return lyst

    l1 = lyst[0: len(lyst) // 2]
    l2 = lyst[len(lyst) // 2:]

    l1 = merge_sort(l1)
    l2 = merge_sort(l2)

    result = []
    i, j = 0, 0
    while True:
        if i >= len(l1) and j >= len(l2):
            break

        if i >= len(l1) and j < len(l2):
            result.append(l2[j])
            j += 1
            continue

        if j >= len(l2) and i < len(l1):
            result.append(l1[i])
            i += 1
            continue

        if l1[i] <= l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    return result


def main():
    u_list = input("input a list of init\n")
    u_list = list(map(float, u_list.split(",")))
    print(merge_sort(u_list))


if __name__ == '__main__':
    main()
