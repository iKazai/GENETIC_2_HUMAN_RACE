# GENETIC_2_HUMAN_RACE

## 🚀 Introduction

Ce projet implémente un **algorithme génétique (AG)** en Python pur afin de simuler l'évolution d'une population de "coureurs" dans le but d'atteindre des performances optimales.

L'objectif est d'explorer les mécanismes de sélection, de croisement et de mutation pour faire converger une population initialement aléatoire vers un individu (coureur) possédant les meilleures caractéristiques pour la course.

**Aucune bibliothèque externe complexe n'est utilisée** ; le projet s'appuie uniquement sur des modules Python natifs et l'implémentation manuelle des concepts de l'algorithme génétique (sélection, *crossover*, mutation).

-----

## ⚙️ Concept de l'Algorithme Génétique

Le processus itératif se déroule comme suit :

1.  **Initialisation :** Création d'une population de 100 coureurs avec des paramètres génétiques aléatoires.
2.  **Évaluation (Fitness) :** Chaque coureur "participe" à une course, et sa vitesse est calculée en fonction de ses paramètres. Cette vitesse sert de valeur de *fitness*.
3.  **Sélection :** Les coureurs les plus performants sont sélectionnés pour la reproduction.
4.  **Croisement (*Crossover*) :** Les gènes des parents sélectionnés sont combinés pour créer une nouvelle génération de coureurs.
5.  **Mutation :** Des modifications aléatoires mineures sont appliquées aux gènes de la nouvelle population pour introduire de la diversité génétique.
6.  **Remplacement :** La nouvelle population remplace l'ancienne.
7.  **Itération :** Les étapes 2 à 6 sont répétées jusqu'à ce qu'un critère d'arrêt (nombre suffisant d'itérations, *fitness* satisfaisante) soit atteint.

-----

## 🏃 Structure du Coureur (Gènes)

Chaque coureur est défini par un ensemble de gènes qui influencent sa performance :

| Gène | Description | Plage de Valeurs (Exemple) | Influence sur la Vitesse |
| :--- | :--- | :--- | :--- |
| **Mollet (Utilisation/Taille)** | Pondération de l'utilisation des muscles du mollet (taille relative du muscle). | $[0.0, 1.0]$ | **Forte** |
| **Cuisse (Utilisation/Taille)** | Pondération de l'utilisation des muscles de la cuisse (taille relative du muscle). | $[0.0, 1.0]$ | **Très Forte** |
| **Taille** | Taille totale du coureur. | $[1.50, 2.10]$ mètres | **Modérée** |
| **Poids** | Poids total du coureur. | $[50.0, 120.0]$ kg | **Inverse** (Plus le poids est élevé, plus l'influence est négative) |

Ces paramètres sont encodés et manipulés comme les "gènes" dans l'AG.

-----

## 📂 Structure du Projet

Le projet sera organisé de manière modulaire pour séparer les responsabilités de l'algorithme génétique et de la simulation de course.

```
GENETIC_2_HUMAN_RACE/
├── src/
│   ├── __init__.py
│   ├── **runner.py** # Définit la classe Coureur (ses gènes et sa structure)
│   ├── **race_simulation.py** # Contient la fonction de Fitness (calcul de la vitesse/performance)
│   ├── **genetic_core.py** # Implémente les fonctions AG (sélection, crossover, mutation, etc.)
│   └── **main.py** # Point d'entrée, lance l'algorithme et gère les boucles d'itération
├── tests/
│   └── ...
├── .gitignore
└── README.md
```

-----

## 🛠️ Installation et Lancement

Ce projet nécessite uniquement **Python 3.x**.

### 1\. Cloner le Repository

```bash
git clone https://github.com/votre_utilisateur/GENETIC_2_HUMAN_RACE.git
cd GENETIC_2_HUMAN_RACE
```

### 2\. Lancement

Exécutez le script principal pour démarrer l'algorithme génétique :

```bash
python src/main.py
```

Le programme affichera la meilleure performance de coureur trouvée à chaque génération.

-----

## 📈 Critères et Heuristiques (À Définir)

  * **Fonction de Fitness (Race Simulation) :** La formule exacte pour le calcul de la vitesse en fonction des gènes doit être définie dans `race_simulation.py`. Elle est cruciale.
  * **Sélection :** Méthode de sélection (ex: Roulette Wheel, Tournoi, Troncature, etc.).
  * **Croisement (*Crossover*) :** Technique de croisement (ex: Point unique, Deux points, Uniforme, etc.).
  * **Mutation :** Taux et amplitude de la mutation.

-----

## 🤝 Contribution

Toutes les contributions sont les bienvenues, surtout pour l'affinage des heuristiques de l'algorithme génétique \!

1.  *Fork* le projet.
2.  Créez une branche de fonctionnalité (`git checkout -b feature/AmazingFeature`).
3.  *Commit* vos changements (`git commit -m 'Add some AmazingFeature'`).
4.  *Push* vers la branche (`git push origin feature/AmazingFeature`).
5.  Ouvrez une *Pull Request*.

-----

## 📄 Licence

Distribué sous la Licence **MIT**. Voir `LICENSE` pour plus d'informations.