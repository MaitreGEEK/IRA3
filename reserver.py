def reserver_place(trains:dict)->str|tuple:
    nom:str = input("Entrez le nom du passager:\n")
    code:str = input("Entrez le code du trajet:\n")
    code = code.upper() 
    if (code not in trains): return "❌ Le train n'existe pas"
    train:dict = trains[code]
    if (train['places_restantes'] <= 0): return "❌ Le train n'a plus de places"
    if nom.lower() in train['passagers']: return "❌ Vous ne pouvez pas réserver deux fois pour le même train"
    train['passagers'].add(nom.lower())
    train['places_restantes'] -= 1
    ticket:tuple = (nom.lower(), code.upper(), train['places_total'] - train['places_restantes'])
    return ticket
    #return f"✅ Réservation effectuée pour le train {code.upper()} pour {nom.title()}"