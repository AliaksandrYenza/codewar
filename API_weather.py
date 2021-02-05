API_key = '56fb69e79920804069a8306f9b3f205a'
call = 'http://api.openweathermap.org/data/2.5/weather'

import requests

params = {
    'q': 'Minsk',
    'appid': API_key,
    'units': 'metric'
}

res = requests.get(call, params= params)
print(res.status_code)
print(res.headers['Content-Type'])
data = res.json()
tmpl = f'In the {params["q"]} temp is {data["main"]["temp"]}'
print(tmpl)
