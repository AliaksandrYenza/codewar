


def q_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return q_sort(less) + [pivot] + q_sort(greater)


if __name__ == '__main__':
    arr = [i for i in range(0,101)]
    print(q_sort(arr))


    