
def sort(lst):
    for i in range(len(lst)-1, 1, -1):
        for j in range(0, i-1):
            if lst[j] > lst[j+1]:
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp
    print(lst)


if __name__ == '__main__':
    lst = [3,4,2,9,2,6,5,9]
    sort(lst)