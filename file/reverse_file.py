# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def ans(first):
    with open(first) as f1:
        f1_lines = f1.read().splitlines()

    with open('result.txt', 'w') as f2:
        for line in f1_lines[::-1]:
            f2.write('%s\n' % line)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ans('dataset_24465_4.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
