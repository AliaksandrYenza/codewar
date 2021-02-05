# https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python



def namelist(names):
    size = len(names)
    res = ""
    a = iter(list(range(size)))
    for i in a:
        next = i +1
        res += names[i]['name']
        if i == size-2 and next +1 == size:
            res += ' & '
        elif i + 1 != size and next  < size:
            res += ', '
        else:
            pass
    return (res)




if __name__ == '__main__':
    namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
    namelist([ {'name': 'Bart'}, {'name': 'Lisa'}])
    namelist([ {'name': 'Bart'}])
    namelist([ ])


