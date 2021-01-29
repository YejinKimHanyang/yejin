import requests

#res = requests.get('http://info.sweettracker.co.kr/api/v1/trackingInfo')

URL = 'http://info.sweettracker.co.kr/api/v1/trackingInfo'

params = {'t_key': 'MUwk2l0qX3mP47ZeL2lNUA', 't_invoice': '637344825585', 't_code': '04'}

response = requests.get(URL, params = params)

print(response.status_code)
print(response.text)

