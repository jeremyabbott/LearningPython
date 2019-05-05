import requests

response = requests.get("https://httpbin.org/ip")

print('Your ip is {0}'.format(response.json()['origin']))