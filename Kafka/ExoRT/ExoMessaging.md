# Exercice Kafka de Messaging

- Chacun de vous va avoir son propre TOPIC, Mehdi par exemple pour moi

- L'objectif de l'exercice est de creer une boite de messagerie capable de communiquer avec chacun de vous sur son propre TOPIC

- Astuce, Producer et Consumer sur le meme fichier

- Producer va commencer juste par envoyer un message a un random

- Ce random aura sur son fichier un Consumer qui est en listening sur son propre TOPIC

- Une fois qu'on recoit un message sur notre TOPIC, on repond au sender

Demande : Resoudre l'exercice en groupe, le resultat est un seul fichier de code qui doit mqrcher sur n'importe quel machine

Link : https://github.com/ElMehdiBen/Py_Course/blob/main/Kafka/ExoRT/Screenshot%202021-10-29%20at%2012.35.11.png

Autre Astuce : earliest vous prend le tout depuis le debut, donc pour reprendre sur votre TOPIC, pensez a le vider / supprimer avec :

    from kafka import KafkaAdminClient

    Admin = KafkaAdminClient(bootstrap_servers = ['209.188.7.148:9092'])
    Admin.delete_topics(["Mehdi"])
