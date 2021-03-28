# https://www.codewars.com/kata/5545f109004975ea66000086/train/python
# 1) n =   3, x = 1, y = 3 =>  true because   3 is divisible by 1 and 3
# 2) n =  12, x = 2, y = 6 =>  true because  12 is divisible by 2 and 6
# 3) n = 100, x = 5, y = 3 => false because 100 is not divisible by 3
# Create a function that checks if a number n
# is divisible by two numbers x AND y.
# All inputs are positive, non-zero digits.

def is_divisible(n,x,y):
    return f'true because {n} is divisible by {x} and {y}' if n%x == n%y == 0 \
        else f'false because {n} is not divisible by {x} and {y}'


print(is_divisible(12,2,6))