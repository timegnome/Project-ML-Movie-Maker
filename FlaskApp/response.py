import urllib.request
import os
import json

data = {
    "Inputs": {

            "input1":
            {
                "ColumnNames": ["Adult", "Genres", "Id", "Imdb Id", "Keywords", "Production Companies", "Production Countries", "Release Date", "Year", "Tagline", "Title", "Budget", "Popularity", "Runtime", "Vote Average", "Vote Count", "New Key", "Worldwide", "Domestic", "Foreign", "Maded_Profit", "Percent_Profit", "Good_Movie"],
                "Values": [ [ "0", "value", "0", "value", "value", "value", "value", "", "0", "value", "value", "0", "0", "0", "0", "0", "value", "0", "0", "0", "0", "value", "value" ], [ "0", "value", "0", "value", "value", "value", "value", "", "0", "value", "value", "0", "0", "0", "0", "0", "value", "0", "0", "0", "0", "value", "value" ], ]
                },
    },
        "GlobalParameters": {

        }
}

body = str.encode(json.dumps(data))
url = os.environ.get('URL', '<URL>')
api_key = os.environ.get('API_KEY', 'wkpEZmoIM5mUsyfoHuaqKg3zAef/t0fKA8lo8JX0Z6woAq2PnTFfSkMGGb0Xr/Suzw3PwZ4T2ikkWrTqhpNuYQ==')
headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}


req = urllib.request.Request(url, body, headers)
print(req)
try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)

except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    print(error.info())

    print(json.loads(error.read()))