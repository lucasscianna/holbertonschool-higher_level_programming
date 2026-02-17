## Différence entre HTTP et HTTPS
HTTP est un protocole qui est basé sur un systeme de requête et de réponse .
Une requête contient plusieurs élements :

- Une méthode(GET POST PUT PATCH DELETE)
- URL
- Header
- Body

HTTPS est un protocole presque identique à la différence que les données sont chiffrées avec un certificat SSL/TLS afin de sécuriser les données.

| Aspect   | HTTP        | HTTPS                      |
| -------- | ----------- | -------------------------- |
| Sécurité | Aucune      | Chiffrement + Certificat.  |
| Données  | Texte clair | Chiffrées                  |

## Structure d'une requête et d'une réponse en HTTP

```
Requête (Client → Serveur):
GET /posts HTTP/1.1          ← Méthode + Chemin + Version
Host: jsonplaceholder.typicode.com
User-Agent: Mozilla/5.0
Accept: application/json

[Corps vide pour GET]
```

```
Réponse (Serveur → Client):
HTTP/1.1 200 OK              ← Version + Code + Message
Content-Type: application/json
Content-Length: 1024

[{"id":1,"title":"sunt...","body":"quia..."}]
```
## Méthodes HTTP

- GET sert à récupérer des informations 
- POST sert à ajouter des données
- PUT sert à remplacer une donnée existante 
- PATCH sert à modifier seulement une partie
- DELETE sert à supprimé une donnée

## Codes de statut

| Code | Nom               | Description            | Scénario                                         |
| ---- | ----------------- | ---------------------- | ------------------------------------------------ |
| 200  | OK                | Succès                 | Page/API chargée developer.mozilla​               |
| 201  | Created           | Ressource créée        | Nouvel user après POST developer.mozilla​         |
| 301  | Moved Permanently | Redirection permanente | Ancien site → nouveau domaine developer.mozilla​  |
| 400  | Bad Request       | Requête invalide       | JSON malformé developer.mozilla​                  |
| 401  | Unauthorized      | Auth requise           | Token manquant developer.mozilla​                 |
| 403  | Forbidden         | Pas de droits          | User non admin sur /admin developer.mozilla​      |
| 404  | Not Found         | Ressource inexistante  | URL fausse developer.mozilla​                     |
| 500  | Server Error      | Erreur serveur         | Bug backend/DB developer.mozilla​                 |
