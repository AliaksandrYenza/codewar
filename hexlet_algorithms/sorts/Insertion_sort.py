def insertion_sort(lst):
    for i in range(len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            tmp = lst[j]
            lst[j] = lst[j-1]
            lst[j-1] = tmp
            j -= 1
    print(lst)


if __name__ == '__main__':
    lst = [2,5,8,3,6,9,0]
    insertion_sort(lst)
