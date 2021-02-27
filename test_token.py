import requests # pip install requests

TOKEN = '2510279efb225800e99a6c34a72820123ca20c58'

headers = {
    'Authorization': f'Token {TOKEN}'
}

res = requests.get('http://localhost:8000/post/1/', headers=headers)
print(res.json())