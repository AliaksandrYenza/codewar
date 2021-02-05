import re
import sys

if __name__ == '__main__':
    pattern = r'(z.{3}z)'
    for line in sys.stdin:
        line = line.rstrip()
        if re.search(pattern, line):
            print(line)
    #
    # pattern = r'((cat).*){2,}'
    # for line in sys.stdin:
    #     line = line.rstrip()
    #     if re.search(pattern, line):
    #         print(line)
