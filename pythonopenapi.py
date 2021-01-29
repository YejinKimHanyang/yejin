import requests
import pprint

headers = {
    'X-Naver-Client-Id': 'worldculture123',
    'X-Naver-Client-Secret': ''

}
payload = {
    'query': '파이션',
    'display': '10'
}

url = 'https://openapi.naver.com/v1/search/blog.json'

res = requests.get(url, headers= headers, params=payload)

pprint.pprint(res.json())