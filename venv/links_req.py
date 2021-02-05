import re
import requests


if __name__ == '__main__':

    links = ["https://stepic.org/media/attachments/lesson/24472/sample1.html",
            "https://stepic.org/media/attachments/lesson/24472/sample2.html"]
    for url in re.findall(r'<a href=\"(.*)\"', requests.get(links[0]).text):
        if  links[1] in re.findall(r'<a href=\"(.*)\"', requests.get(url).text) :
            print('Yes')
