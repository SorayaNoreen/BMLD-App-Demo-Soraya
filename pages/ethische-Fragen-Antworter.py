import random

def ethische_antwort():
    antworten = [
        "Es ist wichtig, die Würde und Rechte jedes Einzelnen zu respektieren.",
        "Wir sollten immer das Wohl der Gemeinschaft im Auge behalten.",
        "Ethisches Verhalten bedeutet, fair und gerecht zu handeln.",
        "Transparenz und Ehrlichkeit sind grundlegende ethische Prinzipien.",
        "Wir müssen Verantwortung für unsere Handlungen übernehmen."
    ]
    return random.choice(antworten)

# Beispiel für die Verwendung der Funktion
if __name__ == "__main__":
    aussage = "Wie sollten wir in dieser Situation handeln?"
    print(f"Aussage: {aussage}")
    print(f"Ethische Antwort: {ethische_antwort()}")