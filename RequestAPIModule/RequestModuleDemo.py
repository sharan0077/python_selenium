import requests


response = requests.get('https://w3schools.com/python/demopage.htm')
print(response.text)
print(response.status_code)
print(response.content)


req = requests.post('https://en.wikipedia.org/w/index.php', data = {'search':'Nanotechnology'})
print(req.text)
print(req.status_code)


