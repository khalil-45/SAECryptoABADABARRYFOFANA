# pylint: disable=E0401
from scapy.all import *
from cryptography.hazmat.primitives.ciphers import Cipher,algorithms,modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
import images as img
import programme as prog



def decrypt_message(message, key):
    """ Fonction qui permet de déchiffrer un message chiffré avec AES-256 en mode CBC

    Args:
        message (bytes): Message chiffré
        key (bytes): Clé de session

    Returns:
        str: Message déchiffré
    """    
    pad = padding.PKCS7(128).padder()
    unpad = padding.PKCS7(128).unpadder()
    message = pad.update(message) + pad.finalize()
    
    iv = message[:16]  # Vecteur d'initialisation de 16 octets
    message = message[16:]  # Données chiffrées après le vecteur d'initialisation
    decryptor = Cipher(algorithms.AES(key),modes.CBC(iv), backend= default_backend()).decryptor() # Déchiffrement AES-256 en mode CBC
    decrypted_message = decryptor.update(message) + decryptor.finalize() # Déchiffrement du message
    return unpad.update(decrypted_message)



    
def process_packets(packet_file):
    """ Fonction qui permet de lire un fichier de paquets et d'extraire les messages chiffrés

    Args:
        packet_file (str): Chemin vers le fichier de paquets

    Returns:
        list: Liste des messages chiffrés
    """    
    packets = rdpcap(packet_file)
    decrypted_messages = []

    # Filtrer les paquets correspondant au protocole plutotBonneConfidentialite
    for packet in packets:
        if scapy.layers.inet.UDP in packet and packet[scapy.layers.inet.UDP].sport == 9999:
            # Récupérer les données chiffrées
            ciphertext = packet[scapy.layers.inet.UDP].payload
            # Déchiffrer les données et ajouter le message déchiffré à la liste
            decrypted_messages.append(ciphertext.load)

    return decrypted_messages


# Appel de la fonction pour déchiffrer les messages
packet_file = "analyse_trace/trace_sae.cap"
extracted_key_recup = img.extract_key("rossignol2.bmp")
extracted_key_transformation1 = extracted_key_recup + extracted_key_recup + extracted_key_recup + extracted_key_recup # Clé de session pour AES-256 (répétition de la clé de 64 bits 4 fois)
extracted_key_transformation2 = int(extracted_key_transformation1,2) # Conversion de la clé de session en entier
extracted_key_transformation3 = extracted_key_transformation2.to_bytes((extracted_key_transformation2.bit_length()+7) // 8,'big') # Conversion de la clé de session en bytes
session_key = extracted_key_transformation3
decrypt_messages = process_packets(packet_file)

for message in decrypt_messages:
    print(decrypt_message(message,session_key).decode('utf-8')) # Afficher le message déchiffré



    
    


