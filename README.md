# Python-DataViz

Ce projet est une application de visualisation de données interactives basée sur Dash, Plotly et Python. Elle permet d'analyser les performances des joueurs dans League of Legends en fonction des objectifs pris, des positions et d'autres statistiques clés.

---

## User Guide

### Prérequis
- **Python 3.11.9**
- **Docker** (facultatif, pour une exécution dans un conteneur).

### Installation et Lancement

#### 1. Mise en place de l'environnement virtuel

Créez un environnement virtuel dans le répertoire racine du projet :
```bash
python -m venv .venv
```

Activez l'environnement virtuel :
- PowerShell :
  ```bash
  .venv\Scripts\Activate
  ```
- CMD :
  ```bash
  .venv\Scripts\activate.bat
  ```
- Git Bash :
  ```bash
  source .venv/Scripts/activate
  ```

Installez les dépendances :
```bash
pip install -r requirements.txt
```

Désactivez l'environnement virtuel lorsque vous avez terminé :
```bash
deactivate
```

#### 2. Lancement de l'application

Lancez le serveur Dash localement :
```bash
python main.py
```

Accédez à l'application via votre navigateur web : [http://localhost:8050].

#### 3. Utilisation avec Docker (facultatif)

Pour exécuter l'application via Docker :

1. Construisez l'image Docker :
   ```bash
   docker build -t python-dataviz .
   ```

2. Lancez un conteneur :
   ```bash
   docker run -p 127.0.0.1:8050:8050 python-dataviz
   ```

Accédez à l'application à l'adresse : [http://localhost:8050].

Afin d'utiliser l'application, il faudra saisir le pseudo de joueurs. 
En voici quelques uns:
- Babimee#EUW
- Targamas#5555
- J1HUIV#000
- SAKEN#soloq

---

## Data

### Description des Données
Les données utilisées dans ce projet proviennent de l'API Riot Games. Elles incluent :
- Les statistiques des matchs : objectifs pris (Baron, Dragon, Herald, etc.), positions des joueurs, victoires/défaites etc.
- Les actions des joueurs : pings, mouvements, XP, gold etc.

Les données sont stockées temporairement en mémoire et ne sont pas sauvegardées localement.

### Accès aux Données
- L'application utilise une clé API Riot pour effectuer des requêtes.
- Une librairie (Pyltover) a été crée pour l'occasion afin de pouvoir communiquer simplement avec l'API Riot via des objets python facile à manipuler.
- Lorsque l'utilisateur saisi un pseudo, l'application *fetch* l'ensemble des données du joueurs (les 20 denrières parties) et les stocks en mémoire afin de les ré-utiliser de page en page. Cela permet de ne pas atteindre de rate-limit trop vite.
---

## Developer Guide

### Architecture
L'application est divisée en plusieurs modules pour faciliter l'extensibilité :

```
NASSIM-IMAD-PYTHON-DATAVIZ/
├── assets/               # Fichiers CSS et autres ressources statiques
├── src/                  # Code source principal
│   ├── components/       # Composants réutilisables pour Dash
│   ├── pages/            # Pages individuelles du dashboard
│   ├── utils/            # Fonctions utilitaires et accès API
├── main.py               # Point d'entrée de l'application
├── Dockerfile            # Configuration Docker
├── requirements.txt      # Dépendances Python
├── README.md             # Documentation
```

### Ajouter une Page
1. Créez un fichier dans `src/pages/`, par exemple `nouvelle_page.py`.
2. Ajoutez ``` dash.register_page(__name__, '/' + __name__.split('.')[-1]) ``` afin qu'elle soit détecté automatiquement par dash avec comme lien ```/leNomDuFichier``` 
4. Styliser la div principale
5. Dans le fichier ``` navbar.py ``` ajouter un ``` dcc.link ``` pour permettre l'accès à la page à travers la navbar

### Ajouter un Graphique
1. Créer une variable ``` layout ``` contenant une div avec un id (qui devra être unique) correspondant au graph que la div contiendra.
2. Ajout d'une méthode décoré avec un callback permettant de créer et personnaliser le graph plotly. Utiliser les input et state nécessaires.
3. Utiliser la librairie Pylotver (créée pour le projet) ainsi que les données stocké en mémoire afin de construire un graphique.
4. Retourner le graphique plotly

### Diagramme de l'Architecture

```mermaid
graph TD
    A[Projet: NASSIM-IMAD-PYTHON-DATAVIZ] --> B[assets/]
    B --> B1[styles.css]
    B --> B2[Summoner's_Rift_Minimap.png]
    B --> B3[Summoner's_Rift_Minimap2.png]

    A --> C[src/]
    C --> C1[components/]
    C1 --> C1_1[__init__.py]
    C1 --> C1_2[graph_container.py]
    C1 --> C1_3[header.py]
    C1 --> C1_4[footer.py]
    C1 --> C1_5[input_pseudo.py]
    C1 --> C1_6[navbar.py]
    C1 --> C1_7[page_layout.py]

    C --> C2[pages/]
    C2 --> C2_1[__init__.py]
    C2 --> C2_2[home.py]
    C2 --> C2_4[objectifs.py]
    C2 --> C2_5[pings.py]
    C2 --> C2_6[positions.py]
    C2 --> C2_7[damage.py]
    C2 --> C2_8[golds.py]

    C --> C3[utils/]
    C3 --> C3_1[pyltover/]
    C3_1 --> C3_1_1[__init__.py]
    C3_1 --> C3_1_2[account.py]
    C3_1 --> C3_1_3[enums.py]
    C3_1 --> C3_1_4[match.py]
    C3_1 --> C3_1_5[matchdata.py]
    C3_1 --> C3_1_6[matchtimeline.py]
    C3_1 --> C3_1_7[pyltover.py]
    C3_1 --> C3_1_8[rank.py]
    C3_1 --> C3_1_9[summoner.py]
    C3_1 --> C3_1_10[README.md]
    C3_1 --> C3_2[DTOs/]
    C3_2 --> C3_2_1[__init__.py]

    C3 --> C3_2[graph_utils.py]
    C3 --> C3_3[pyltover_instance.py]

    A --> D[.venv/]
    A --> E[Dockerfile]
    A --> F[.dockerignore]
    A --> G[main.py]
    A --> H[README.md]
    A --> I[requirements.txt]
```

---

## Rapport d'Analyse

### Objectifs Clés
1. Identifier les objectifs ayant le plus d'impact sur le winrate des joueurs.
2. Analyser l'influence des positions des joueurs au cours de la partie.
3. Quantifier l'impact des pings et des actions en jeu sur les résultats des parties.
4. Visualiser l'évolution des Golds (argent en jeu) des joueurs au cours d'une partie.
5. Visualiser la quantité de dégâts effectués par un joueur et la répartition entre dégâts magique et physique.

### Conclusions
- **Atakhan et Baron** : Ces objectifs augmentent significativement le taux de victoire.
- **Positions Stratégiques** : Les joueurs se regroupent autour des timings d'objectif représente un avantage.
- **Coordination à travers les Pings** : Dans le jeu, certains joueurs utilisent parfois les pings (indicateurs visuels) à mauvais escient (se moquer de ses alliés ect.). Les données démontre qu'une communication efficace, saine et mesuré (utilise les bons ping, au bon moment et avec modération) est corrélée à un meilleur taux de victoire.
- **Argent en jeu** : Posséder plus d'argent que le reste des joueurs pendant une partie favorise la victoire, le fait de gagner encore d'avantage d'argent ainsi que les dégâts.
- **Dégats** : Les joueurs infligeant le plus de dégâts inflige souvent un seul type de dégât (physique ou magique).

---

## Copyright

Je déclare sur l’honneur que le code fourni a été produit par moi/nous-mêmes, à l’exception des lignes ci-dessous :

- **Mermaid pour le diagramme d'architecture** : Documentation officielle Mermaid pour générer des diagrammes Markdown.

Toute ligne non déclarée ci-dessus est réputée être produite par l’auteur (ou les auteurs) du projet.

---
