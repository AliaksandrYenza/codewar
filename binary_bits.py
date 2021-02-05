def counter_d():
    dec = int(input("Plz input: "))
    binary_list = []
    while dec != 0:
        if dec % 2 == 0:
            binary_list.append(0)
        elif dec % 2 == 1:
            binary_list.append(1)
        dec = dec // 2
    return binary_list


def add_binary(a,b):
    return str(bin(a+b))[2:]

if __name__ == '__main__':
    # b_list = counter_d()[::-1]
    # print(''.join([str(elem) for elem in b_list]))
    print(add_binary(2,3))