
# 1ère partie :

def encrypt_text(text : str, key1 : int):
    """
    Fonction qui prend en argument un texte et deux clés et qui renvoie le texte chiffré quelque soit la taille du texte.

    Args:
        text: Le texte à chiffrer.
        key1: La première clé de chiffrement.
        key2: La deuxième clé de chiffrement.

    Returns:
        Le texte chiffré.
    """

    # Convertir le texte en minuscules

    text = text.lower()

    # Créer une liste pour stocker le texte chiffré

    ciphered_text = []

    # Chiffrer chaque lettre du texte

    for letter in text:
        # Convertir la lettre en nombre

        letter_number = ord(letter) - 97

        # Chiffrer la lettre

        ciphered_letter = (letter_number + key1) % 26

        # Ajouter la lettre chiffrée à la liste

        ciphered_text.append(chr(ciphered_letter + 97))

    # Convertir la liste en chaîne de caractères

    ciphered_text = ''.join(ciphered_text)

    # Retourner le texte chiffré

    return ciphered_text
    

    





def cassage_brutal(message_clair : str, message_chiffre : str):
    """
    Méthode qui tente de retrouver les clés utilisées pour chiffrer un message en testant toutes les possibilités.

    Args:
        message_clair: Le message clair.
        message_chiffre: Le message chiffré.

    Returns:
        Les clés utilisées pour chiffrer le message, ou None si le message ne peut pas être déchiffré.
    """

    # Convertir le message clair et le message chiffré en minuscules

    message_clair = message_clair.lower()
    message_chiffre = message_chiffre.lower()

    # Créer une liste pour stocker les clés

    keys = []

    # Tester toutes les possibilités

    for key1 in range(1,2025):
        # Chiffrer le message clair avec la clé actuelle

        message_chiffre_test = encrypt_text(message_clair, key1)

        # Vérifier si le message chiffré est égal au message chiffré test

        if message_chiffre_test == message_chiffre:
            # Ajouter la clé à la liste

            keys.append(key1)

    # Retourner les clés si elles ont été trouvées, sinon None

    if len(keys) > 0:
        return keys
    else:
        return None
    
    















   
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        text = ' '.join(lines)
    return text

file_path = 'arsene_lupin_extrait.txt'

# Example usage
message_clair = read_file(file_path)
message_chiffre = encrypt_text(message_clair, 990)
print(message_chiffre)
clés = cassage_brutal(message_clair, message_chiffre)

print(clés)























    




