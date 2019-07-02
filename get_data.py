import json
import urllib.request

with open('get_data.json', 'w') as file:
    url = "http://127.0.0.1:8000/dots/?format=json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    json.dump(data, file)
