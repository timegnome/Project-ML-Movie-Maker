import urllib.request
import os
import json

data = {
    "Inputs": {

            "input1":
            {
                "ColumnNames": ["Budget", "Keywords", "Genre", "Vote Average", "Revenue"],
                "Values": [ [ "0", "0", "0", "22", "0" ], [ "0", "0", "3", "0" ], ]
            },
    },
        "GlobalParameters": {

        }
}

body = str.encode(json.dumps(data))
url = os.environ.get('URL', '<URL>')
api_key = os.environ.get('API_KEY', '<API_KEY>')
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