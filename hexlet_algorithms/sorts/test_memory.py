def b_sort(lst):
    print('bubble sort')
    print(lst)
    for i in range(len(lst), 1, -1):
        for j in range(0, i - 1):
            if lst[j] > lst[j + 1]:
                tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = tmp
    print(lst)
    print('---------------')


def insertion_sort(lst):
    print('insertion sort')
    print(lst)
    for i in range(len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j - 1]:
            tmp = lst[j]
            lst[j] = lst[j - 1]
            lst[j - 1] = tmp
            j -= 1
    print(lst)
    print('----------------')


def binary_search(lst, l, r, x):
    if l <= r:
        mid = (r + l) // 2
        if lst[mid] == x:
            print(lst[mid])
            return mid
        elif lst[mid] > x:
            return binary_search(lst, l, mid - 1, x)
        else:
            return binary_search(lst, mid + 1, r, x)
    else:
        return -1


if __name__ == '__main__':
    lst = [2, 5, 8, 3, 0, 4, 6, 7, 10]

    # b_sort(lst)

    # insertion_sort(lst)

    # a = binary_search(lst, 0, len(lst)-1, 10)
    # if a != -1:
    #     print('index is' ,str(a))

