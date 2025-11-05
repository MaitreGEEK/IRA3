def afficher_trains_complets(trains)->str:
    complets:[] = [trajet for trajet, infos in trains.items() if infos['places_restantes'] == 0]
    if not complets:
        return "❌ Aucun train complet."
    else:
        message = "--- Trains complets ---"
        for trajet in complets:
            message += f"\n{trajet} est complet, ({trains[trajet]['places_total']} places réservées)"
        return message
