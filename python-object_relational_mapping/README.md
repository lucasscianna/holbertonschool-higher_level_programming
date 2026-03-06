# Python - Object-Relational Mapping (ORM)

## 📖 Description
Ce projet marque la transition entre la manipulation de bases de données via des requêtes SQL brutes et l'utilisation d'un **ORM (Object-Relational Mapper)**. 

L'objectif est d'apprendre à connecter Python à MySQL de deux manières différentes :
1.  **MySQLdb** : Utilisation d'un driver pour exécuter du SQL directement depuis Python.
2.  **SQLAlchemy** : Utilisation d'une couche d'abstraction pour manipuler la base de données comme s'il s'agissait d'objets Python (POO).

## 🎯 Objectifs d'apprentissage
À la fin de ce projet, vous serez capable d'expliquer :
* Comment se connecter à une base de données MySQL depuis un script Python.
* Comment exécuter des requêtes `SELECT` et `INSERT` via Python.
* Le concept d'**ORM** et ses avantages (indépendance du stockage, abstraction).
* Comment mapper une classe Python à une table MySQL.

---

## 💻 Configuration Requise
* **Système d'exploitation** : Ubuntu 20.04 LTS
* **Langage** : Python 3.8.5
* **Base de données** : MySQL 8.0
* **Style de code** : `pycodestyle` (version 2.7.*)

### Dépendances MySQL & Python
Pour exécuter les scripts de ce projet, vous devez installer les modules suivants :

```bash
# Installation des dépendances système pour MySQL
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev

# Installation du module MySQLdb (mysqlclient)
sudo pip3 install mysqlclient==2.0.3

# Installation de SQLAlchemy
sudo pip3 install SQLAlchemy==1.4.22