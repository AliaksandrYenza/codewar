from math import sqrt


def n_fib(n):
    n_number = round( (1 / (sqrt(5))) * (( ((1 + sqrt(5)) / 2) ** n ) - ( ((1 - sqrt(5)) / 2) ** n ) )  )
    return (str(n_number))[-1]


if __name__ == '__main__':
    n = int(input('n='))
    assert ( int(n_fib(n-1)) + int(n_fib(n-2))) == int(n_fib(n))
    print(n_fib(n))

