def theSmallest(arr):
    smallest_v = arr[0]
    smallest_i = 0
    for i in range(1, (len(arr))):
        if arr[i] < smallest_v:
            smallest_i = i
            smallest_v = arr[i]
    return smallest_i

def selectionSort(arr):
    s_arr = []
    for i in range(len(arr)):
        smallest_i = theSmallest(arr)
        s_arr.append(arr.pop(smallest_i))
    return s_arr

if __name__ == '__main__':
    arr = [i for i in range(101)]
    print(selectionSort(arr))