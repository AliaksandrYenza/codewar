def mod_checker(x, mod=0):
    return lambda y : y % x == mod



if __name__ == "__main__":
    mod_3 = mod_checker(3)

    print(mod_3(3))  # True
    print(mod_3(4))  # False

    mod_3_1 = mod_checker(3, 1)
    print(mod_3_1(4))  # True

    aa = lambda y : y % 3 == 0
    print(aa(3))
