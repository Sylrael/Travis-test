# Projet Big Data : Bitcoin

## User Story 1 : Cours du Bitcoin

### Diagramme Architecture

![Diagram Architecture](https://image.noelshack.com/fichiers/2018/13/4/1522356305-diagram-architecture-v1-0-1.png)

### Récupération des données de l'API
- CoinDesk API
- Données en temps réel
- Données historiques
- Python

### Insertion des données brutes dans un gestionnaire de messages
- Kafka

### Traitement des données
- Traitement des données historiques
- Traitement des données en temps réel

### Insertion des données dans une base de données
- Elastic Search
- Données temps réel
- Java
- Données historiques
- Python

### Visualisation des données
- Kibana
- Visualisation des cours du bitcoin
- Dashboard

### Machine Learning
- MLlib Spark
- Naive Bayes
- Bag of words

#### Annexes

#### Spécifications
Packages python:
- requests
- spark
- kafka
- elasticsearch

#### Notes
- Elastic Search : host, port, données : date, rate
- Kafka : broker, topic, offset management
- Machine Learning : nltk, nltk.download('corpus'), nltk.download()
- Kibana : import/export, configuration : restreindre accès aux options : barre de recherche, filtre date, onglets

- Travis : add java language (pb : build jar, copy file)
- Ansible : playbook (run scripts and jar)
