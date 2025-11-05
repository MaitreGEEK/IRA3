def afficher_trains(trains)->str: 
    if not trains:
        return "❌ Désolé il n'y a plus de trains disponible."
    else :
        message = "=== LISTE DES TRAINS DISPONIBLES ==="
        for code_trajet, infos in trains.items():
            places_total = infos['places_total']
            places_restantes = infos['places_restantes']
            nombre_passagers = len(infos['passagers'])

            message += f"\n{code_trajet} \nPlaces : {places_restantes} restantes / {places_total} total \nPassagers inscrits : {nombre_passagers}"

            if places_restantes == 0:
                message += "\nCOMPLET"
            elif places_restantes <= places_total * 0.2:
                message += "\nPeu de places restantes."
            else:
                message += "\nPlaces disponibles."
        return message