# https://www.codewars.com/kata/541c8630095125aba6000c00/python


def digital_root(n):
    while len(str(n)) != 1:
        n = sum([int(n[i]) for i in range(len(str(n)))])
    print(n)
    return n

def listing(n):
    return  sum([int(n[i]) for i in range(len(str(n)))])

if __name__ == '__main__':
    print(digital_root(n = 111) == 3 )
