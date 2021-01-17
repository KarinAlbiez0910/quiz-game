import requests
import html

parameters = {
    'amount': 10,
    'type' : 'boolean'

}

response = requests.get('https://opentdb.com/api.php', params=parameters)
response.raise_for_status()

data = response.json()

data = data['results']

for item in data:
    item["question"] = html.unescape(item["question"])

question_data = data







