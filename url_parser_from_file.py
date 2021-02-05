import re
import urllib.request
from urllib.parse import urlparse


def inputlink():
    return input()


def get_links(link):
    try:
        with urllib.request.urlopen(link) as f:
            bytes = f.read()
            str_bytes = bytes.decode('utf-8')
        links = re.findall(r'<a.+href=[\'"]([^./][^\'"]*)[\'"]', str_bytes)
    except:
        return []
    else:
        return links


def parse_links(links):
    parsed_uri = urlparse(link)
    res = parsed_uri.netloc
    try:
        return res[:res.index(':')]
    except:
        return res
    else:
        return res[:res.index(':')]


if __name__ == '__main__':
    links = list(map(parse_links,get_links(inputlink())))
    for link in sorted(list(set(links))):
        print(link)

