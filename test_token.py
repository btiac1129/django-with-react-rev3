import requests # pip install requests

# TOKEN = '2510279efb225800e99a6c34a72820123ca20c58'
JWT_TOKEN = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2Vy"
    "bmFtZSI6InVzZXIyIiwiZXhwIjoxNjE0NTE5NjYwLCJlbWFpbCI6IiIsIm9ya"
    "WdfaWF0IjoxNjE0NTE5MzYwfQ.PWA5l_ITu4YBY1VUlejXDh5HAmH2cs6XyorpwOOcwzU"
)

headers = {
    # 'Authorization': f'Token {TOKEN}'
    'Authorization': f'JWT {JWT_TOKEN}', # JWT 인증
}

res = requests.get('http://localhost:8000/post/1/', headers=headers)
print(res.json())