import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    files={
        'text': open('test.txt', 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)



rJson = r.json()
print (rJson)
print (rJson.get("output_url"))