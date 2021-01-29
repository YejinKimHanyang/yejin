import requests
import json

base_url: str = 'http://info.sweettracker.co.kr'
api_url: str = '/api/v1/companylist'

api_params: dict = {
    't_key': 'MUwk2l0qX3mP47ZeL2lNUA' #secret key
}

res = requests.get(base_url+api_url, params = api_params)
data = json.loads(res.text)

print(type(res.text))
print(type(data))

#print(res)
print(res.text)
print('\n')
print(data)