"""Ce module contient les fonctions nécessaires pour le chiffrement et le déchiffrement """
#!/usr/bin/python3
#
# Author: Joao H de A Franco (jhafranco@acm.org)
#
# Description: Simplified DES implementation in Python 3
#
# Date: 2012-02-10
#
# License: Attribution-NonCommercial-ShareAlike 3.0 Unported
#          (CC BY-NC-SA 3.0)
#===========================================================

from time import time
#pylint: disable=C0103,R1705
KeyLength = 10
SubKeyLength = 8
DataLength = 8
FLength = 4

# Tables for initial and final permutations (b1, b2, b3, ... b8)
IPtable = (2, 6, 3, 1, 4, 8, 5, 7)
FPtable = (4, 1, 3, 5, 7, 2, 8, 6)

# Tables for subkey generation (k1, k2, k3, ... k10)
P10table = (3, 5, 2, 7, 4, 10, 1, 9, 8, 6)
P8table = (6, 3, 7, 4, 8, 5, 10, 9)

# Tables for the fk function
EPtable = (4, 1, 2, 3, 2, 3, 4, 1)
S0table = (1, 0, 3, 2, 3, 2, 1, 0, 0, 2, 1, 3, 3, 1, 3, 2)
S1table = (0, 1, 2, 3, 2, 0, 1, 3, 3, 0, 1, 0, 2, 1, 0, 3)
P4table = (2, 4, 3, 1)


def perm(inputByte, permTable):
    """
    Permute le byte d'entrée selon la table de permutation spécifiée.

    Args:
        inputByte (int): Le byte d'entrée à permuter.
        permTable (tuple): La table de permutation spécifiée.

    Returns:
        int: Le byte de sortie après permutation.
    """
    outputByte = 0
    for index, elem in enumerate(permTable):
        if index >= elem:
            # Décalage à droite si l'index est supérieur ou égal à l'élément de permutation
            outputByte |= (inputByte & (128 >>
                                        (elem - 1))) >> (index - (elem - 1))
        else:
            # Décalage à gauche si l'index est inférieur à l'élément de permutation
            outputByte |= (inputByte & (128 >>
                                        (elem - 1))) << ((elem - 1) - index)
    return outputByte


def ip(inputByte):
    """
    Effectue la permutation initiale sur les données.

    Args:
        inputByte (int): Le byte d'entrée à permuter.

    Returns:
        int: Le byte de sortie après permutation.
    """
    return perm(inputByte, IPtable)


def fp(inputByte):
    """
    Effectue la permutation finale sur les données.

    Args:
        inputByte (int): Le byte d'entrée à permuter.

    Returns:
        int: Le byte de sortie après permutation.
    """
    return perm(inputByte, FPtable)


def swapNibbles(inputByte):
    """
    Échange les deux nibbles des données.

    Args:
        inputByte (int): Le byte d'entrée à permuter.

    Returns:
        int: Le byte de sortie après échange des nibbles.
    """
    return (inputByte << 4 | inputByte >> 4) & 0xff


def keyGen(key):
    """Génère les deux sous-clés requises à partir de la clé donnée.

    Args:
        key (int): La clé d'entrée.

    Returns:
        tuple: Un tuple contenant les deux sous-clés générées.
    """

    def leftShift(keyBitList):
        """Effectue une rotation circulaire vers la gauche sur les cinq premiers bits.

        Args:
            keyBitList (list): La liste des bits de la clé.

        Returns:
            list: La liste des bits après la rotation.
        """
        shiftedKey = [None] * KeyLength
        shiftedKey[0:9] = keyBitList[1:10]
        shiftedKey[4] = keyBitList[0]
        shiftedKey[9] = keyBitList[5]
        return shiftedKey

    # Convertit la clé d'entrée (entier) en une liste de chiffres binaires
    keyList = [(key & 1 << i) >> i for i in reversed(range(KeyLength))]
    permKeyList = [None] * KeyLength
    for index, elem in enumerate(P10table):
        permKeyList[index] = keyList[elem - 1]
    shiftedOnceKey = leftShift(permKeyList)
    shiftedTwiceKey = leftShift(leftShift(shiftedOnceKey))
    subKey1 = subKey2 = 0
    for index, elem in enumerate(P8table):
        subKey1 += (128 >> index) * shiftedOnceKey[elem - 1]
        subKey2 += (128 >> index) * shiftedTwiceKey[elem - 1]
    return (subKey1, subKey2)


def fk(subKey, inputData):
    """Applique la fonction Feistel sur les données avec la sous-clé donnée.

    Args:
        subKey (int): La sous-clé utilisée dans la fonction Feistel.
        inputData (int): Les données d'entrée.

    Returns:
        int: Les données après l'application de la fonction Feistel.
    """

    def F(sKey, rightNibble):
        """Applique la fonction F sur le demi-octet de droite avec la sous-clé donnée.

        Args:
            sKey (int): La sous-clé utilisée dans la fonction F.
            rightNibble (int): Le demi-octet de droite.

        Returns:
            int: Le résultat de l'application de la fonction F.
        """
        aux = sKey ^ perm(swapNibbles(rightNibble), EPtable)
        index1 = ((aux & 0x80) >> 4) + ((aux & 0x40) >> 5) + \
                 ((aux & 0x20) >> 5) + ((aux & 0x10) >> 2)
        index2 = ((aux & 0x08) >> 0) + ((aux & 0x04) >> 1) + \
                 ((aux & 0x02) >> 1) + ((aux & 0x01) << 2)
        sboxOutputs = swapNibbles((S0table[index1] << 2) + S1table[index2])
        return perm(sboxOutputs, P4table)

    leftNibble, rightNibble = inputData & 0xf0, inputData & 0x0f
    return (leftNibble ^ F(subKey, rightNibble)) | rightNibble


def encrypt(key, plaintext):
    """Chiffre le texte en clair avec la clé donnée.

    Args:
        key (int): La clé utilisée pour le chiffrement.
        plaintext (int): Le texte en clair à chiffrer.

    Returns:
        int: Le texte chiffré.
    """
    # Applique la fonction Feistel avec la première sous-clé sur les données en utilisant
    # la permutation initiale
    data = fk(keyGen(key)[0], ip(plaintext))
    # Applique la permutation finale et la fonction Feistel avec la deuxième sous-clé
    # sur les données chiffrées
    return fp(fk(keyGen(key)[1], swapNibbles(data)))


def decrypt(key, ciphertext):
    """Déchiffre le texte chiffré avec la clé donnée. (8 bits max)

    Args:
        key (int): La clé utilisée pour le chiffrement.
        ciphertext (int): Le texte chiffré à déchiffrer.

    Returns:
        int: Le texte déchiffré.
    """
    # Applique la fonction Feistel inverse sur les données avec la sous-clé k2
    data = fk(keyGen(key)[1], ip(ciphertext))
    # Applique la permutation finale et la fonction Feistel inverse avec la sous-clé k1
    return fp(fk(keyGen(key)[0], swapNibbles(data)))


def encrypt_text(key, text):
    """
    Chiffre le texte donné avec la clé donnée.

    Args:
        key (int): La clé utilisée pour le chiffrement.
        text (str): Le texte à chiffrer.

    Returns:
        str: Le texte chiffré.
    """
    text_bits = text_to_bits(text)
    bits_encrypter = ''
    # Chiffrement par bloc de 8 bits de tout le texte
    for i in range(0, len(text_bits), 8):
        block = int(text_bits[i:i + 8], 2)
        block_crypter = encrypt(key, block)
        bits_encrypter += format(block_crypter, '08b')
    return bits_to_text(bits_encrypter)


def decrypt_text(key, encrypted_text):
    """
    Déchiffre le texte chiffré avec la clé donnée.

    Args:
        key (int): La clé utilisée pour le déchiffrement.
        encrypted_text (str): Le texte chiffré à déchiffrer.

    Returns:
        str: Le texte déchiffré.
    """
    bits_crypter = text_to_bits(encrypted_text)
    bits_decrypter = ''
    # Déchiffrement par bloc de 8 bits de tout le texte
    for i in range(0, len(bits_crypter), 8):
        block = int(bits_crypter[i:i + 8], 2)
        block_decrypter = decrypt(key, block)
        bits_decrypter += format(block_decrypter, '08b')
    return bits_to_text(bits_decrypter)


def text_to_bits(text):
    """
    Converts a string of text into its binary representation.

    Args:
        text (str): The input text to be converted.

    Returns:
        int: The binary representation of the input text.
    """
    return ''.join(format(ord(char), '08b') for char in text)


def text_to_bin(text):
    """
    Converts a string of text into its binary representation.

    Args:
        text (str): The input text to be converted.

    Returns:
        int: The binary representation of the input text.
    """
    return int(''.join(format(ord(char), '08b') for char in text), 2)


def bits_to_text(bits):
    """
    Convertit une chaîne de bits en texte.

    Args:
        bits (str): La chaîne de bits à convertir.

    Returns:
        str: Le texte correspondant aux bits.
    """
    chars = []
    # Parcours des bits par bloc de 8
    for i in range(0, len(bits), 8):
        byte = bits[i:i + 8]
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)


def double_encrypt(key1, key2, text):
    """
    Effectue un double chiffrement sur un texte en utilisant deux clés.

    Args:
        key1 (int): La première clé de chiffrement.
        key2 (int): La deuxième clé de chiffrement.
        text (str): Le texte à chiffrer.

    Returns:
        str: Le texte chiffré avec les deux clés.
    """
    text_bits = text_to_bits(text)
    encrypted_bits = ''
    # Parcours des blocs de 8 bits du texte
    for i in range(0, len(text_bits), 8):
        block = int(text_bits[i:i + 8], 2)
        # Chiffrement avec la première clé
        encrypted_block = encrypt(key1, block)
        # Chiffrement avec la deuxième clé
        encrypted_block = encrypt(key2, encrypted_block)
        encrypted_bits += format(encrypted_block, '08b')

    # On peut utilisé la fonction encrypt_text() pour chiffrer le texte avec les deux clés
    # encrypted_bits = text_to_bits(encrypt_text(key1, encrypt_text(key2, text)))
    return bits_to_text(encrypted_bits)


def cassage_brutal(message_clair, message_chiffre):
    """Tente de retrouver les clés utilisées pour chiffrer le message en
        testant toutes les possibilités 

    Args:
        message_clair (str) : message clair
        message_chiffre (str) : message chiffré

    Returns:
        tuple : clés utilisées pour chiffrer le message ou None si aucune clé n'a été trouvée
    """
    debut = time()
    message_chiffre_bits = text_to_bits(message_chiffre)
    for i in range(256):
        for j in range(256):
            decrypted_message = ''
            for k in range(0, len(message_chiffre_bits), 8):
                block = int(message_chiffre_bits[k:k + 8], 2)
                decrypted_block = decrypt(i, decrypt(j, block))
                decrypted_message += format(decrypted_block, '08b')
            if bits_to_text(decrypted_message) == message_clair:
                print("Temps d'exécution : ", time() - debut)
                return (i, j)
    return None


def cassage_astucieux(message_clair, message_chiffre):
    """
    Tente de retrouver les clés utilisées pour chiffrer le message 
        en utilisant une approche astucieuse.

    Args:
        message_clair (str): Le message clair.
        message_chiffre (str): Le message chiffré.

    Returns:
        tuple: Les clés utilisées pour chiffrer le message ou None si aucune clé n'a été trouvée.
    """
    debut = time()
    dico_decrypte = {}
    dico_crypte = {}

    # Nous allons utiliser une seule boucle for pour tester les 256 possibilités de clés
    for i in range(1, 256):
        message_clair_crypte = encrypt_text(i, message_clair)
        message_chiffre_decrypte = decrypt_text(i, message_chiffre)

        if message_clair_crypte == message_chiffre_decrypte:
            # Si le message clair chiffré avec la clé i est égal
            #   au message chiffré déchiffré avec la clé i,
            # cela signifie que les clés utilisées sont (i, i)
            print("Temps d'exécution : ", time() - debut)
            return (i, i)

        if message_clair_crypte in dico_decrypte:
            # Si le message clair chiffré avec la clé i est déjà présent
            #   dans le dictionnaire dico_decrypte,
            # cela signifie que les clés utilisées sont (i, dico_decrypte[message_clair_crypte])
            print("Temps d'exécution : ", time() - debut)
            return (i, dico_decrypte[message_clair_crypte])
        else:
            dico_decrypte[message_chiffre_decrypte] = i

        if message_chiffre_decrypte in dico_crypte:
            # Si le message chiffré déchiffré avec la clé i est déjà présent
            #   dans le dictionnaire dico_crypte,
            # cela signifie que les clés utilisées sont (dico_crypte[message_chiffre_decrypte], i)
            print("Temps d'exécution : ", time() - debut)
            return (dico_crypte[message_chiffre_decrypte], i)
        else:
            dico_crypte[message_clair_crypte] = i

    # Si aucune correspondance n'est trouvée,
    # retourner un résultat indiquant que les clés n'ont pas été trouvées
    return None
