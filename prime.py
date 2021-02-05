import itertools


def primes():
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                pass
            else:
                yield n



if __name__ == '__main__':
    print(list(itertools.takewhile(lambda x : x <= 31, primes())))

