import json

import requests

client_id = 'db311cfe37ec4bc74a61'
client_secret = 'ba1d22427d386b0b79ce4403c063b2ec'
filename = 'api_artsy/dataset_24476_4 (3).txt'

if __name__ == '__main__':
    res = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                        data={
                            "client_id": client_id,
                            "client_secret": client_secret
                        })
    d = json.loads(res.text)
    token = d['token']
    headers = {
        'xapp_token': token
    }

    art = []
    with open(filename, 'r+', encoding='utf8') as r_file:
        for artist in r_file:
            artist = artist.strip()
            url = "https://api.artsy.net/api/artists/{}".format(artist)
            res = requests.get(url, params=headers)
            res.decode = 'utf-8'
            artist_data = json.loads(res.text)
            art.append({'name': artist_data['sortable_name'], 'birthday': artist_data['birthday']})

    for a in sorted(art, key=lambda x: (int(x['birthday']), x['name'])):
        # w_file.write(a['name']+'\n')
        print(a['name'])