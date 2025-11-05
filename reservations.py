def annuler_reservation(trains)->str:
    trajet:str = input("Entrez le code du trajet à annuler (ex: TUN-PAR) : ").upper()
    if trajet not in trains:
        return "❌ Trajet introuvable."

    nom:str = input("Entrez le nom du passager à supprimer : ").lower()

    if nom not in trains[trajet]['passagers']:
        return f"❌ Le passager {nom.title()} n’a pas de réservation sur le trajet {trajet}."
    else:
        trains[trajet]['passagers'].remove(nom)
        trains[trajet]['places_restantes'] += 1
        return f"✅ Réservation de {nom.title()} sur le trajet {trajet} annulée avec succès."

def afficher_passagers(trains)->str:
    trajet:str = input("Entrez le code du trajet (ex: TUN-PAR) : ").upper()
    if trajet not in trains:
        return "❌ Ce trajet n’existe pas."

    passagers:str = sorted(trains[trajet]['passagers'])
    if not passagers:
        return f"Aucun passager n’est encore enregistré sur le trajet {trajet}."
    else:
        message = f"🧳 Liste des passagers pour {trajet} :"
        for p in passagers:
            message+= f"\n - {p}"
        return message
