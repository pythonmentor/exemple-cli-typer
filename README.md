# Exemple de structure pour une application CLI avec Typer

Cet exemple montre comment structurer une application en ligne de
commande (CLI) utilisant la bibliothèque typer pour gérer les 
arguments, options et commandes reçues par le programme lorsqu'il 
est lancé depuis le terminal.

## Installation des dépendances

Le projet exemple utilise pipenv pour gérer les dépendances de l'application.
Si pipenv n'est pas installé sur votre ordinateur, vous pouvez l'installer 

avec pip:
```
$ pip install --user pipenv
```

avec pipx:
```
$ pipx install pipenv
```

Une fois pipenv installé sur votre ordinateur, il vous suffit de créer un répertoire .venv
vide à la racine du projet, puis d'exécuter la commande `pipenv install` (également depuis)
la racine du projet. Vous pouvez ensuite activer l'environnement virtuel simplement avec `pipenv shell`.

La documentation de l'application est disponible en exécutant la commande:
```
$ python -m epicevents --help
```