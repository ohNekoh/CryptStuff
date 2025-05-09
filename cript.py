import random
import string

# PREFISSI PER IL RICONOSCIMENTO DELLE LETTERE
#
# NB: Questi codici DEVONO essere cambiati se c'è la volontà di sfruttare il codice
# Per comodità è limitato a 14 lettere, può essere esteso facilmente senza ripercussioni



token = input("Inserisci il token: ")
try:
    prefix_map = {
        1: token[0:3],
        2: token[3:6],
        3: token[6:9],
        4: token[9:12],
        5: token[12:15],
        6: token[15:18],
        7: token[18:21],
        8: token[21:24],
        9: token[24:27],
        10: token[27:30],
        11: token[30:33],
        12: token[33:36],
        13: token[36:39],
        14: token[39:42],
    }
except IndexError as ex:
    print("Token invalido.")

# queste variabili gestiscono il livello di intensità (punto a come min e punto b come max)
# possono essere personalizzate da qui, oppure è possibile modificare la quantità direttamente dall'IF chiamato dopo l'input lenght_hide
lvl_1_a = 5
lvl_1_b = 10
lvl_2_a = 50
lvl_2_b = 100
lvl_3_a = 100
lvl_3_b = 500
lvl_4_a = 500
lvl_4_b = 1000
lvl_5_a = 1000
lvl_5_b = 2000
lvl_default_a = lvl_3_a
lvl_default_b = lvl_3_b


# Funzione per mettere roba a caso tra le lettere del messaggio
def random_trash(length):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length)) 


# Inserisce il messaggio in mezzo a tutti i caratteri casuali con i prefissi sopra, dopodichè salva nel file
def encrypt_message():
    message = input("Inserisci il messaggio da criptare: ")
    output_path = input("Inserisci il nome del file in cui inserire il messaggio (es: Messaggio.txt): ")
    print("Nota bene: Un livello maggiore d'intensità renderà il messaggio ancora più difficile da decifrare, ma sarà più pesante in memoria")
    lenght_hide = int(input("Inserire il livello di intensità (1|5) [Default: 3]: "))
    if lenght_hide == 1:
        lenght_1 = lvl_1_a
        lenght_2 = lvl_1_b
    elif lenght_hide == 2:
        lenght_1 = lvl_2_a
        lenght_2 = lvl_2_b
    elif lenght_hide == 3:
        lenght_1 = lvl_3_a
        lenght_2 = lvl_3_b
    elif lenght_hide == 4:
        lenght_1 = lvl_4_a
        lenght_2 = lvl_4_b
    elif lenght_hide == 5:
        lenght_1 = lvl_5_a
        lenght_2 = lvl_5_b
    else:
        lenght_1 = lvl_default_a
        lenght_2 = lvl_default_b

    encrypted_message = ""
    for word in message.split():
        for i, char in enumerate(word, start=1):
            prefix = prefix_map.get(i, "TOGHR")
            random_chars_before = random_trash(random.randint(lenght_1, lenght_2))
            encrypted_message += f"{random_chars_before}{prefix}{char}"

        encrypted_message += random_trash(random.randint(lenght_1, lenght_2))
    
    with open(output_path, 'w') as file:
        file.write(encrypted_message)
    
    print(f"Messaggio salvato in: {output_path}")
    print(f"""
Messaggio:
          
          {encrypted_message}""")

encrypt_message()
