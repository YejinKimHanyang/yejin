import requests
import json

#res = requests.get('http://info.sweettracker.co.kr/api/.../tracking/5')
#if res.status_code != 200:
#    raise ApiError('GET / tracking/ {}'.format(res.status_code))
#for 

#print(res.text)

with open("mola.json", "r", encoding='UTF8') as read_file:
    data = json.load(read_file)
print(data)
