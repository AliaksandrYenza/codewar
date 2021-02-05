# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python

def make_readable(seconds):
    return ('%(h)02d:%(m)02d:%(s)02d' % {"h": (seconds // 3600), "m": ((seconds % 3600) // 60),
                                            "s": ((seconds % 3600) % 60)})
    # Do something


# make_readable(86399), "23:59:59")
# make_readable(359999), "99:59:59")

if __name__ == '__main__':
    print(make_readable(359999))
