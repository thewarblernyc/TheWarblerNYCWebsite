import json
F = open("data/publication.json")

data = json.load(F)

print(data['publications'][0]['body'])

F.close()