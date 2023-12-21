from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.asymmetric import rsa
import os
import programme as prog
import timeit


def encrypt_AES(message,key):
    """ Fonction qui permet de chiffrer un message avec AES-256 en mode CBC 

    Args:
        message (str): Message à chiffrer
        key (bytes): Clé de session

    Returns:
        tuple: Vecteur d'initialisation et message chiffré
    """    
    iv = os.urandom(16)  # Pour AES, le vecteur d'initialisation a une taille de 16 octets (128 bits)
    
    # Création d'un objet AES avec mode CBC et le vecteur d'initialisation
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    
    # Création d'un objet de remplissage (padding)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    
    # Remplissage du message pour qu'il soit un multiple de la taille du bloc
    padded_data = padder.update(message) + padder.finalize()
    
    # Chiffrement du message avec AES-CBC
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    return iv, ciphertext

def decrypt_AES(vecteur, message_chiffre, key):
    """ Fonction qui permet de déchiffrer un message chiffré avec AES-256 en mode CBC

    Args:
        vecteur (str): Vecteur d'initialisation
        message_chiffre (bytes): Message chiffré
        key (bytes): Clé de session

    Returns:
        bytes: Message déchiffré
    """    
    # Création d'un objet AES avec mode CBC et le vecteur d'initialisation
    cipher = Cipher(algorithms.AES(key), modes.CBC(vecteur), backend=default_backend())
    
    # Décryptage du message avec AES-CBC
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(message_chiffre) + decryptor.finalize()
    
    # Suppression du padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    
    return data










message_AES = b"Bonjour, ceci est un message secret !"
message_SDES = "Bonjour, ceci est un message secret !"

# Génération d'une clé AES aléatoire de 256 bits
key = os.urandom(32)  # Pour AES, une clé de 256 bits correspond à 32 octets


# Chiffrement du message avec AES
iv, ciphertext = encrypt_AES(message_AES, key)

# Affichage du message chiffré et du vecteur d'initialisation (pour le déchiffrement ultérieur)
print("Message chiffré avec AES :", ciphertext)
print("Vecteur d'initialisation utilisé :", iv)
print("Message chiffré avec SDES :", prog.double_encrypt(prog.keyGen(10)[0], prog.keyGen(10)[1], message_SDES))
# Déchiffrement du message avec AES
print("Message déchiffré avec AES :", decrypt_AES(iv, ciphertext, key))


# Temps d'exécution du chiffrement et du déchiffrement avec SDES
time_sdes = timeit.timeit(lambda: prog.double_encrypt(prog.keyGen(10)[0], prog.keyGen(10)[1], message_SDES), number=1)
print("Temps d'exécution du double chiffrement avec SDES :", time_sdes)

# Temps d'exécution du chiffrement et du déchiffrement avec AES
time_aes = timeit.timeit(lambda: encrypt_AES(message_AES, key), number=1)
print("Temps d'exécution du chiffrement avec AES :", time_aes)

# Exemple d'utilisation de timeit avec une fonction de déchiffrement AES
time_aes_decrypt = timeit.timeit(lambda: decrypt_AES(iv, ciphertext, key), number=1)
print("Temps d'exécution du déchiffrement avec AES :", time_aes_decrypt)
