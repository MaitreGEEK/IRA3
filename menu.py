from affichage_trains import  afficher_trains
from afficher_trains_complets import afficher_trains_complets
from reserver import reserver_place
from reservations import annuler_reservation, afficher_passagers

import os

def nettoyer()->None:
    os.system('cls' if os.name == 'nt' else 'clear')

def entree()->None: 
    input("\nAppuyez sur entrée pour continuer...")

def menu(trains:dict)->None:
    while True:
        nettoyer()
        print("\n=== MENU RÉSERVATION TRAIN ===\n1️⃣ Afficher tous les trains et leur disponibilité\n2️⃣ Réserver une place\n3️⃣ Annuler une réservation\n4️⃣ Voir les passagers d’un train\n5️⃣ Voir les trains complets\n0️⃣ Quitter")
        choix:str = input("Votre choix (0-5) : ").strip()
        nettoyer()
        if choix == "1":
            print(afficher_trains(trains))
            entree()
        elif choix == "2":
            ticket:str|tuple = reserver_place(trains)
            if (type(ticket) == tuple): print(f"✅ Réservation effectuée pour le train {ticket[1].upper()} pour {ticket[0].title()}")
            else: print(ticket)
            entree()
        elif choix == "3":
            print(annuler_reservation(trains))
            entree()
        elif choix == "4":
            print(afficher_passagers(trains))
            entree()
        elif choix == "5":
            print(afficher_trains_complets(trains))
            entree()
        elif choix == "0":
            print("Merci d'avoir utilisé le système. Au revoir!")
            break
        else:
            print("Choix invalide, veuillez entrer un chiffre entre 0 et 5.")
            entree()

trains:dict = {
    'TUN-PAR': {'places_total': 5, 'places_restantes': 5, 'passagers': set()},
    'TUN-ROM': {'places_total': 3, 'places_restantes': 3, 'passagers': set()},
    'TUN-MAD': {'places_total': 4, 'places_restantes': 4, 'passagers': set()},
}

menu(trains)
