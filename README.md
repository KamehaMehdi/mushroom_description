# Mushroom detection

## Concept

Utiliser [un dataset de champignon](https://www.kaggle.com/uciml/mushroom-classification?select=mushrooms.csv) pour créer un modèle, création de modèle qui se fera via un notebook.
Ce modèle permettra, en lui donnant un tableau de caractéristiques, de définir si un champignon avec ces caractéristiques pourrait être, ou non, vénéneux.

## Installation

Il vous faudra, de préférence, utiliser un `python3.7` ou `python3.8`

### Notebook

L'installation du notebook se fait de manière simple grâce à son requirements `notebook_requirements.txt`:

```sh
python3 -m pip install -r notebook_requirements.txt --use-feature=2020-resolver
```

### API

Comme pour le notebook, vous pourrez installer les librairies de l'api grâce au `requirements.txt`

```sh
python3 -m pip install -r requirements.txt --use-feature=2020-resolver
```

## Utilisation

### Notebook

Pour lancer le serveur : `python3 -m jupyter notebook`, il se lancera sur le port 8888 et vous permettra de lancer le notebook.
Sur le notebook, si vous exécutez toutes les étapes vous aurez un fichier `.pkl` en conclusion, c'est à dire un modèle. Libre à vous de modifier et de proposer, par PR vos modifications.

### API

Pour lancer le serveur : `python3 app.py`, il se lancera sur le port 5000 et vous permettra d'accéder à l'IHM mais aussi à l'API.
L'IHM est accéssible à la route `/` ; l'API de vérification est à la route `/results`.

L'API est utilisable de cette manière en envoyant une requête sur la route `/results`, avec en query un tableau de nombre : mushroom=[odeur, forme-du-chapeau, tâches, population, habitat] Où :

* odeur :
  * aucune : 0
  * anis : 1
  * goudron : 2
  * poisson : 3
  * forte : 4
  * moisi : 5
  * amande : 6
  * âcre : 7
  * épicé : 9
* forme-du-chapeau :
  * clôche : 0
  * conique : 1
  * convex : 2
  * plat : 3
  * bouton-au-centre : 4
  * creu : 5
* tâches :
  * sans : 0
  * avec : 1
* population :
  * abondant : 0
  * isolés : 1
  * nombreux : 2
  * éparse : 3
  * sévère : 4
  * solitaire : 5
* habitat :
  * herbus : 0
  * feuillu : 1
  * prairie : 2
  * chemin : 3
  * urbain : 4
  * terrain-isolé : 5
  * forêts : 6

Vous aurez comme réponse soit 1 soit 0, qui correspondent respective à probablement vénéneux et probablement pas vénéneux.
