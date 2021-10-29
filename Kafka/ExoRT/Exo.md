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

Les objectifs de l'exercice sont l'experimentation d'un flux de donnees en temps reel, lire d'une API real time, envoyer vers KAFKA en streaming and lire ensuite depuis KAFKA pour mettre sur une base de donnee pour dashboarding.

# TP - Questions

1. Test the API endpoint to see the change frequency
2. Use the change frequency in your sleep function
3. Write a producer script that calls the API, gets some of the relevant information and sends them to KAFKA
4. Write a consumer script that takes the data from Kafka and writes it to elasticsearch

# Writing to Elastic Search Example

    from elasticsearch import Elasticsearch
    from datetime import datetime

    es = Elasticsearch(["https://elastic:g9tufnez6HKsW74KHxksON5d@my-deployment-51a233.es.eastus2.azure.elastic-cloud.com:9243"])

    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    res = es.index(index="test", document=doc)
    print(res['result'])
    
# Checking Elastic Search

- Installer l'extension ElasticVue sur Chrome ou Firefox
- Connectez vous en utilisant :
- username : elastic
- pwd : g9tufnez6HKsW74KHxksON5d
- host : https://my-deployment-51a233.es.eastus2.azure.elastic-cloud.com:9243
- Allez sue indexes pour trouver votre index
   
