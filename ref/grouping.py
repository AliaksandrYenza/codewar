import re
if __name__ == '__main__':
    pattern = r"((\w+)-\2)"
    string = "test-test chow-chow"
    duplicates = re.findall(pattern, string)
    print(duplicates)
