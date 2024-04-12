## Rapport sur le Travail Pratique de Git

### **Introduction :**
Le travail pratique avait pour objectif de familiariser les étudiants avec l'utilisation de Git et GitHub, ainsi que de mettre en pratique les concepts de gestion de versions, de branches et d'intégration continue.

#### **1. Initialisation du Projet :**
- Description : Cette étape consistait à créer un nouveau dépôt sur GitHub, à le cloner localement, à ajouter des fichiers au projet et à les pousser vers le dépôt distant.
- Détails des étapes :
  - Création d'un nouveau dépôt sur GitHub avec un README.md et un modèle .gitignore pour Python.
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/39edecd2-19a1-4542-aaf0-fde8634f5738)
    
  - Clonage du dépôt localement avec la commande `git clone`.
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/dd7f93f5-707f-4869-adc4-2fc668f6b81b)

  - Ajout des fichiers `calculator.py`, `main.py` et `test_calculator.py` au projet.
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/00a61b43-da2b-4526-9a2b-ba92f64f066b)

  - Validation des changements avec `git add` et `git commit`.
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/6f471710-c7d8-4d34-a6ba-8a73310424e5)

  - Poussée des modifications vers le dépôt distant avec `git push`.

    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/a3198ba6-f0da-4aa2-8f3b-558943f4a8ff)

- Vérification : Vérifier que les fichiers ont été correctement ajoutés au dépôt distant sur GitHub.
  
  ![image](https://github.com/DumeM2b/tp-git/assets/163656850/0a85ba8c-5444-4692-8ba3-705cf91d03ac)
  ![image](https://github.com/DumeM2b/tp-git/assets/163656850/21ce74d6-9563-470e-9317-3bbdea44771a)



#### **2. Les Branches :**
- Description : Cette section consistait à mettre en place des fonctionnalités de calculatrice en Python en utilisant des branches Git pour chaque opération (addition, soustraction, division).
- Détails des étapes :
  - Création d'une branche dédiée pour chaque fonctionnalité avec `git checkout -b nom_de_la_branche`.
    Addition
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/23abc4d6-a072-4db7-8491-58974fe10ace)

    Soustraction
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/f3dc867a-5f75-4071-addf-1e83da141ffb)

    Division
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/f13b6dad-d683-4387-8f3a-cbe87de67128)
    

  - Implémentation de la fonctionnalité dans le fichier correspondant.
    Addition
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/fcbaa9d3-3c08-4b30-8c9e-4f7f0d958eda)

    Soustraction
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/988f3268-45e1-4bb6-b0eb-1dcc4a63576d)

    Division
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/42ab147f-f584-487e-84eb-010c828710ae)


  - Ajout, validation et poussée des modifications vers le dépôt distant.
    Addition
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/01d9220d-8ae5-4b7c-aa9b-a35d1e1386d4)

    Soustraction
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/1c751a8b-4bec-4170-ac59-79e09c774d57)

    Division
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/592287b6-8c85-4bd3-a858-d8e1b1e35f45)


  - Création d'une pull request sur GitHub pour fusionner les modifications dans la branche principale.
    Addition
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/6378f153-6228-439c-96a2-22c76f97d1a0)

    Soustraction
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/5c533028-8280-4225-bcc8-8b9b8a2a7554)

    Division
    
    ![image](https://github.com/DumeM2b/tp-git/assets/163656850/8655b025-ee63-4a5b-a746-456258851a16)


- Vérification : Vérifier que les modifications sont bien fusionnées dans la branche principale sur GitHub.

### **3 - Pipeline d'Intégration Continue :**

Cette partie du travail pratique visait à mettre en place un pipeline d'intégration continue (CI) qui comprend deux étapes essentielles : l'exécution automatique d'un linter pour vérifier le respect des conventions de développement, et l'exécution automatique de tests unitaires pour garantir le bon fonctionnement du code.

## **3.1 Configuration du Linter :**

Pour cette étape, nous avons utilisé pylint comme outil de linter pour contrôler que les conventions de développement sont bien respectées, notamment le style du code. Voici les étapes que nous avons suivies :

1. **Installation de pylint :** Nous avons installé pylint localement en utilisant la commande `pip install pylint`.

2. **Configuration de GitHub Actions :** GitHub fournit un template pré-configuré pour exécuter pylint automatiquement à chaque modification du projet. Nous avons configuré cela en accédant à l'onglet Actions sur GitHub, en recherchant pylint, puis en cliquant sur configure.
   
   ![image](https://github.com/DumeM2b/tp-git/assets/163656850/1692bcd1-ef03-4ace-a419-fffbcb6b9558)

4. **Validation :** Après avoir configuré pylint, nous avons récupéré les modifications distantes dans notre IDE en utilisant la commande `git pull origin main`. Ensuite, nous avons effectué une modification mineure dans notre projet et poussé ces modifications vers le dépôt distant pour vérifier que le pipeline se déclenchait correctement.

   ![image](https://github.com/DumeM2b/tp-git/assets/163656850/90e73b87-6514-4ce2-bd4a-74f796bf9f9e)


## **3.2 Implémentation de Tests Unitaires :**

Dans cette étape, nous avons implémenté des tests unitaires simples pour vérifier le bon fonctionnement des fonctionnalités de notre calculatrice en Python. Voici les étapes que nous avons suivies :

1. **Installation de pytest :** Nous avons installé pytest localement en utilisant la commande `pip install pytest`.

2. **Implémentation des tests unitaires :** Dans le fichier `test_calculator.py`, nous avons implémenté des tests pour chaque fonctionnalité de la calculatrice. Par exemple, pour tester l'addition, nous avons écrit un test qui vérifie si l'addition de deux nombres renvoie le résultat attendu.

   ![image](https://github.com/DumeM2b/tp-git/assets/163656850/73918e6d-6b2c-4fea-badd-4143b1beff1f)


4. **Exécution des tests :** Nous avons exécuté les tests unitaires en utilisant la commande `pytest` dans notre terminal, et nous avons vérifié que les tests se sont exécutés avec succès.

   ![image](https://github.com/DumeM2b/tp-git/assets/163656850/5c2363a5-e203-4dad-b0c7-0b53abdf086d)


## **3.3 Exécution Automatique des Tests Unitaires :**

Dans cette dernière étape, nous avons automatisé l'exécution des tests unitaires à chaque modification du code en mettant à jour notre fichier de configuration de pipeline. Voici les étapes que nous avons suivies :

1. **Renommage du fichier de configuration :** Nous avons renommé le fichier `.github/workflows/pylint.yml` en `.github/workflows/ci.yml` pour refléter les modifications apportées au pipeline.

  ![image](https://github.com/DumeM2b/tp-git/assets/163656850/c1f3071d-1261-4cb2-87e2-c65071f2d890)

2. **Mise à jour de la configuration :** Dans le fichier `ci.yml`, nous avons ajouté une étape pour installer pytest en mettant à jour le step Install dependencies. Ensuite, nous avons créé un nouveau step Execute unit test pour exécuter les tests unitaires en utilisant la commande `pytest`.

  ![image](https://github.com/DumeM2b/tp-git/assets/163656850/03075af7-520f-43c5-a8f4-6f6d03bc2c4e)

3. **Validation :** Après avoir poussé nos modifications vers le dépôt distant, nous avons vérifié que les tests unitaires s'exécutaient automatiquement à chaque modification du code en effectuant une modification mineure et en vérifiant que le pipeline se déclenchait correctement.


## **Conclusion :**
En conclusion, ce travail pratique a permis de mettre en pratique les concepts fondamentaux de Git et GitHub, ainsi que de comprendre l'importance de l'intégration continue dans le processus de développement logiciel. Il a également fourni une expérience concrète dans la gestion de versions et la collaboration sur des projets de programmation.

