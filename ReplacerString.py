# https://stepik.org/lesson/24469/step/6?unit=6775

s, a, b = (input() for _ in range(3))


def f(s, a, b, counter=0):
    if a in b and a in s:
        return 'Impossible'
    if s == s.replace(a, b):
        return counter
    else:
        counter += 1
        s = s.replace(a, b)
        return f(s, a, b, counter)


if __name__ == "__main__":
    print(f(s, a, b))
