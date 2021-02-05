def generate_hashtag(s):
    return ('#' + ' '.join(map(str, (str(i)[0].upper() + str(i)[1:].lower() for i in list(s.split())))).replace(' ', '')) \
        if len(s) <= 140 and len(s) != 0 else False


if __name__ == '__main__':
    print(generate_hashtag(s='CodeWars is nice'))
