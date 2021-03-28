# we have field 1680 x 640

def dd(w,h):
    b = max(w,h)
    s = min(w,h)
    print(f'w = {w}, h = {h}')
    if b % s == 0 and b == s:
        print(f' {s} x {s} ')
    else:
        b -= s
        dd(b,s)

if __name__ == '__main__':
    h = 1680
    w = 640
    dd(h,w)

