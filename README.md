# Table of contents / Table de matières :
1. [ Description (English). ](#en)
2. [ Description (Français). ](#fr)


<a name="en"></a>
# Description [English]

This project aims to investigate interpolation and integration methods for analyzing airfoil data. It consists of three main parts:

- Interpolation: Focuses on the Cubic Spline method applied to the goe05k airfoil data, aiming to obtain a smooth curve representing the airfoil shape.
- Integration: Compares various methods including trapezoidal rule, Simpson rule, Romberg method, and epsilon-integration, to calculate the integral of a given function. The goal is to identify the most suitable method for our specific application.
- Application: Applies the studied interpolation and integration methods to the airfoil data to generate a pressure map and analyze air particle trajectories around the airfoil.

Through this project, we aim to deepen our understanding of interpolation and integration techniques and their practical applications in airfoil analysis. The results obtained will contribute to our knowledge of airfoil aerodynamics, providing valuable insights for further research and development in the field.


## Repository Organization

The project code is located in the `src` directory. For each section,
there is a corresponding code file named using its section number.
For example, the code for section 1 is in the file `part1.py`.
The directory also contains various test files belonging to the different
sections. For example, the tests for section 1 are in the file `test1.py`.

In the `sections` directory, you can find the different latex files
belonging to the different sections included in the `report.tex` file.


## Makefile

The Makefile has several targets. By running the `make test` command,
you can run tests on all sections. The `make` command generates the report,
and to get details on the report compilation, one needs to run the
`make verbose` command.



<a name="fr"></a>
# Description [Français]

Ce projet vise à étudier les méthodes d'interpolation et d'intégration pour l'analyse des données d'aile. Il se compose de trois parties principales :

- Interpolation : se concentre sur la méthode des splines cubiques appliquée aux données de l'aile goe05k, dans le but d'obtenir une courbe lisse représentant la forme de l'aile.
- Intégration : compare différentes méthodes, dont la règle du trapèze, la règle de Simpson, la méthode de Romberg et l'intégration epsilon, pour calculer l'intégrale d'une fonction donnée. L'objectif est d'identifier la méthode la plus adaptée à notre application spécifique.
- Application : applique les méthodes d'interpolation et d'intégration étudiées aux données de l'aile pour générer une carte de pression et analyser les trajectoires des particules d'air autour de l'aile.

À travers ce projet, nous visons à approfondir notre compréhension des techniques d'interpolation et d'intégration et de leurs applications pratiques dans l'analyse des ailes. Les résultats obtenus contribueront à notre connaissance de l'aérodynamique des ailes, fournissant des informations précieuses pour de futures recherches et développements dans ce domaine.

## Organisation du dépôt

Le code du projet se trouve dans le répertoire `src`. Pour chaque section,
il existe un fichier de code correspondant portant le numéro de la section.
Par exemple, le code de la section 1 se trouve dans le fichier `part1.py`.
Le répertoire contient également divers fichiers de test appartenant aux différentes
sections. Par exemple, les tests pour la section 1 se trouvent dans le fichier `test1.py`.

Dans le répertoire `sections`, vous pouvez trouver les différents fichiers LaTeX
appartenant aux différentes sections incluses dans le fichier `report.tex`.

## Makefile

Le Makefile possède plusieurs cibles. En exécutant la commande `make test`,
vous pouvez exécuter les tests sur toutes les sections. La commande make génère le rapport,
et pour obtenir des détails sur la compilation du rapport, il faut exécuter la
commande make verbose.
