def berechne_kalorien(alter, gewicht, groesse, geschlecht, aktivitaetslevel):
    # Berechnung des Grundumsatzes (BMR) basierend auf Geschlecht
    if geschlecht == 'Männlich':
        bmr = 88.362 + (13.397 * gewicht) + (4.799 * groesse) - (5.677 * alter)
    else:
        bmr = 447.593 + (9.247 * gewicht) + (3.098 * groesse) - (4.330 * alter)
    
    # Anpassung des BMR basierend auf dem Aktivitätslevel
    if aktivitaetslevel == 'Wenig aktiv':
        kalorien = bmr * 1.2
    elif aktivitaetslevel == 'Leicht aktiv':
        kalorien = bmr * 1.375
    elif aktivitaetslevel == 'Mäßig aktiv':
        kalorien = bmr * 1.55
    elif aktivitaetslevel == 'Sehr aktiv':
        kalorien = bmr * 1.725
    else:
        kalorien = bmr * 1.9
    
    return kalorien