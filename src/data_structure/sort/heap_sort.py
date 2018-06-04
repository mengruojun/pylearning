def swap(arry, i, j):
    temp = arry[i]
    arry[i] = arry[j]
    arry[j] = temp


def heapify(arr, i, heap_size):
    """
    heapify the node i, swap it with largest(left, right)
    """
    left_i = i * 2
    right_i = i * 2 + 1

    if left_i < heap_size and arr[left_i] > arr[i]:
        largest_i = left_i
    else:
        largest_i = i

    if right_i < heap_size and arr[right_i] > arr[largest_i]:
        largest_i = right_i

    if largest_i != i:
        swap(arr, largest_i, i)
        heapify(arr, largest_i, heap_size)


def build_max_heap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr))


def heap_sort(input_list):
    build_max_heap(input_list)
    N = len(input_list)

    for i in range(len(input_list)-1, 0, -1):
        swap(input_list, i, 0)
        N = N -1
        heapify(input_list, 0, N)

    return input_list


def main():
    u_list = input("input a list of init\n")
    u_list = list(map(float, u_list.split(",")))
    print(heap_sort(u_list))


if __name__ == '__main__':
    main()
