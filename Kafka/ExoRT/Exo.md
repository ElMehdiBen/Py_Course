# Real Time API Example

import requests

url = "https://coinranking1.p.rapidapi.com/coin/1"
(OR "https://coinranking1.p.rapidapi.com/coins")

headers = {
    'x-rapidapi-host': "coinranking1.p.rapidapi.com",
    'x-rapidapi-key': "f99779c96bmshd8fbf40fea4d618p12a843jsn0ca45c3d0d29"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

=======================================================

# TP - Objectives


# TP - Questions
