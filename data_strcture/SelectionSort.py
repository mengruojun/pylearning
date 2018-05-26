def swap(lyst, i, j):
    """Exchange the times"""
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


def selectionSort(lyst):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            if (lyst[j] < lyst[minIndex]):
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i)
        i += 1


if __name__ == '__main__':
    print(selectionSort(list(range(99, 1))))
