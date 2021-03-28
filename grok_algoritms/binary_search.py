import random


def binary_search(low, high, list_s, item):
    while low < high:
        mid = (low + high) // 2
        print(f' low = {low}, mid = {mid}, high = {high}')
        guess = list_s[mid]
        if guess == item or guess + 1 == high == item or guess -1 == low == item:
            return item
        elif guess > item:
            high = mid-1
        elif guess < item:
            low = mid + 1
        continue


if __name__ == '__main__':
    lst = [i for i in range(100)]
    item = random.randint(0,101)
    print(item)

    print(binary_search(0, len(lst), sorted(lst), item))

