import random


def theSmallest(arr, low, high):
    mid = (low + high) //2
    print(f' low = {low}, mid = {mid}, high = {high}')
    guess = arr[mid]
    if guess == item:
        print(item)
        # return item
    if guess > item:
        theSmallest(arr, low, mid - 1)
    elif guess < item:
        theSmallest(arr, mid + 1, high)
    else:
        pass


if __name__ == '__main__':
    arr = [i for i in range(101)]
    item = random.randint(0,100)
    print(f'our item = {item}')
    a = theSmallest(arr, 0, len(arr))
    print(a)