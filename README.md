# algortihmique-miniprojet-1
Pour lancer le projet il suffit de lancer menu.py
```sh
python3 menu.py
```

# Structure de départ suggérée
Vous pouvez utiliser la structure suivante :
```py
trains = {
    'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set()},
    'TUN-ROM': {'places_total': 3, 'places_restantes': 3, 'passagers': set()},
    'TUN-MAD': {'places_total': 4, 'places_restantes': 4, 'passagers': set()},
}
```


# Fonctionnalités attendues
1️⃣ Afficher les trains
- Afficher chaque trajet avec le nombre total de places et le nombre de places restantes.
- Exemple : TUN-PAR → 3 places restantes / 5

2️⃣ Réserver une place
- Demander le nom du passager et le code du trajet.
- Vérifier si le trajet existe et s’il reste des places.
- Ajouter le passager et diminuer les places restantes.
- Empêcher un même passager de réserver deux fois.
- Afficher un message clair en cas d’erreur ou de succès.

3️⃣ Annuler une réservation
- Supprimer un passager de la liste et augmenter les places restantes.

4️⃣ Afficher les passagers d’un train
- Afficher la liste triée des passagers d’un trajet donné.

5️⃣ Afficher les trains complets
- Lister les trains dont le nombre de places restantes est égal à zéro.

6️⃣ (Bonus) Génération de ticket
- Lors d’une réservation, créer un tuple (nom, trajet, numéro_de_place).


 # Menu principal :
 
=== MENU RÉSERVATION TRAIN ===
1️⃣  Afficher les trains
2️⃣  Réserver une place
3️⃣  Annuler une réservation
4️⃣  Afficher les passagers d’un train
5️⃣  Voir les trains complets
0️⃣  Quitter
