# https://stepik.org/lesson/24476/step/3?unit=6781

import requests

def tmpl_create(num):
    return 'http://numbersapi.com/{num}/math?json=true'.format(num= str(num))

filename = 'api_nums/dataset_24476_3 (4).txt'

if __name__ == '__main__':
    with open(filename, 'r+') as from_file, open('api_nums/res.txt', 'w') as to_file:
        for num in from_file:
            num = num.strip()
            url = tmpl_create(num)
            res = requests.get(url= url)
            if res.json()['found'] == True:
                to_file.write('Interesting\n')
            else:
                to_file.write('Boring\n')


