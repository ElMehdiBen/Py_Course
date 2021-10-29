# Exercice Kafka de Messaging

- Chacun de vous va avoir son propre TOPIC, Mehdi par exemple pour moi

- L'objectif de l'exercice est de creer un script de boite de messagerie capable de communiquer avec chacun de vous sur son propre TOPIC

Astuce 1 : Producer et Consumer sur le meme fichier

- Producer va commencer juste par envoyer un first message a un random

- Ce random aura sur son fichier un Consumer qui est en listening sur son propre TOPIC

- Une fois qu'on recoit un message sur notre TOPIC, on repond au meme sender avec un message sur input

## Demande : Resoudre l'exercice en groupe, le resultat est un seul fichier de code qui doit marcher sur n'importe quel machine en changeant uniquement votre nom

Illustration : https://github.com/ElMehdiBen/Py_Course/blob/main/Kafka/ExoRT/Screenshot%202021-10-29%20at%2012.35.11.png

Astuce 2 : earliest vous prend le tout depuis le debut, donc pour reprendre sur votre TOPIC, pensez a le vider / supprimer avec :

    from kafka import KafkaAdminClient

    Admin = KafkaAdminClient(bootstrap_servers = ['209.188.7.148:9092'])
    Admin.delete_topics(["Mehdi"])
    
Help : 
1. On vide le TOPIC
2. On envoi un message a quelqu'un de random
3. On commence a listener sur notre TOPIC
4. Si jamais on recoit un message, on repond au meme sender en ecrivant un message sur input
5. En Gros, c'est de la communication deux a deux sur des channels prives
6. Tres tres bon courage !!
