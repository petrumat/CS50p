import requests, json
from sys import argv, exit

if len(argv) > 3:
    exit("Too many arguments")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + argv[1])

# print(json.dumps(response.json(), indent=2))

o = response.json()

for result in o["results"]:
    print(result["trackName"])