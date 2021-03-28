import random
import time

def random_date():
    return str(random.randint(5,8)) + str(random.randint(1,30))


def month_day(day):
    lst_date = list()
    clean_date = list()
    for i in range(day):
        lst_date.append(random_date())
    lst_date = sorted(lst_date)
    for i in lst_date:
        if i[0] == '5':
            clean_date.append(f'May-{i[1:]}')
        elif i[0] == '6':
            clean_date.append(f'June-{i[1:]}')
        elif i[0] == '7':
            clean_date.append(f'Jule-{i[1:]}')
        elif i[0] == '8':
            clean_date.append(f'Aug-{i[1:]}')
    return clean_date


def cre():
    total = 5000
    a_arr = list()
    day = 0
    while total > 0:
        a = random.randint(50, 100)
        day += 1
        # d = random_date()
        a_arr.append(a)
        total -= a
    ch = list()
    m = month_day(day)
    for i in range(len(a_arr)):
        ch.append((m[i], a_arr[i]))
    totals = {}
    for key, value in ch:
        totals[key] = totals.get(key, 0) + value
    tt = 0
    for key, value in ch:
        tt += value
    print('total = ')
    print(tt)
    print(totals)

    for i in sorted(totals.keys(), key=lambda x: (len(x[0]), x[0])):
        print(f'{i} : {totals[i]} \t')

    return a_arr



if __name__ == '__main__':

    (cre())
