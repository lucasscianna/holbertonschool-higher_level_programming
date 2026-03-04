# SQL - More Queries 🗄️🚀

Ce projet est la suite de l'introduction au SQL chez **Holberton School**. On y explore la gestion avancée des bases de données MySQL, notamment les privilèges utilisateurs, les contraintes de table (`PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`), et les requêtes multi-tables.

## 📝 Description

Ce dépôt contient des scripts SQL pour :
- Gérer les utilisateurs et les permissions (`GRANT`, `SHOW GRANTS`).
- Créer des tables avec des contraintes d'intégrité (`NOT NULL`, `DEFAULT`, `UNIQUE`).
- Manipuler des données relationnelles complexes (TV Shows database).
- Utiliser les jointures pour lier plusieurs tables entre elles.

## 🚀 Configuration du serveur

### Installation (Ubuntu 20.04)
Si MySQL n'est pas installé sur votre machine :
```bash
sudo apt update
sudo apt install -y mysql-server
sudo service mysql start