# import http.client
import requests

# conn = http.client.HTTPConnection("www.google.com")
# conn.request("GET", "/")
# response = conn.getresponse()
# print(response)

# conn_poke = http.client.HTTPSConnection("pokeapi.co")
# conn_poke.request("GET", "/api/v2/pokemon/1")
# response = conn_poke.getresponse()
# print(response.status)

req = requests.get("https://pokeapi.co/api/v2/pokemon/1")
print(req.status_code)
# print(req.text)