import re

# PREFISSI LETTERE (DEV'ESSERE COMBACIANTE CON I PREFISSI DEL PRIMO CODICE)
prefix_map = {
    1: "UTdIO",
    2: "IROES",
    3: "ARIOD",
    4: "ITOR",
    5: "IORE",
    6: "IYTRW",
    7: "OTPET",
    8: "ITHKF",
    9: "JGEKW",
    10: "JFKETO",
    11: "FIOEW",
    12: "TEODF",
    13: "RORPE",
    14: "IROFS",
}
prefix_list = list(prefix_map.values()) + ["EXTRA"] # aggiunge il prefisso extra per le parole che superano i 14 caratteri (non dev'essere per forza EXTRA, ma dei caratteri casuali come per le altre lettere)

def decrypt_message():
    input_path = input("Inserisci il file del messaggio da decifrare (Se il txt è fuori dalla cartella del file .py va specificata la path): ")

    with open(input_path, 'r') as file:
        encrypted_message = file.read()
    
    # Trova tutte le lettere del messaggio originale basate sui prefissi
    pattern = f"({'|'.join(map(re.escape, prefix_list))})(.)"
    matches = re.findall(pattern, encrypted_message)
    
    original_message = []
    current_word = []
    current_letter_index = 1

    for match in matches:
        prefix, letter = match

        # se trova il primo prefisso viene contata come nuova parola
        if prefix == "UTdIO":
            if current_word:  # Se c'è già una parola, aggiungila al messaggio
                original_message.append("".join(current_word))
            current_word = []  # Resetta la parola corrente

        # Aggiungi la lettera alla parola corrente
        current_word.append(letter)

        # Controlla se siamo oltre la 14° lettera o se il prefisso è EXTRA
        if prefix == "EXTRA" or current_letter_index == 14:
            current_letter_index = 0  # Resetta l'indice delle lettere
        
        current_letter_index += 1

    # Aggiungi l'ultima parola se presente
    if current_word:
        original_message.append("".join(current_word))

    # Ricostruisci il messaggio con spazi
    final_message = " ".join(original_message)
    print(f"Messaggio decriptato: {final_message}")

decrypt_message()
