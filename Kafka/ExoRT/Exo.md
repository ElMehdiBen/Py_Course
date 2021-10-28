# Real Time API Example

Source : https://rapidapi.com/Coinranking/api/coinranking1/

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

1. Test the API endpoint to see the change frequency
2. Use the change frequency in your sleep function
3. Write a producer script that calls the API, gets some of the relevant information and sends them to KAFKA
4. Write a consumer script that takes the data from Kafka and writes it to elasticsearch
