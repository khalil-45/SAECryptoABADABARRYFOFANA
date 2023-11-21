# 1ère partie :


# Fonction qui tente de retrouver la clé utilisée pour chiffrer le message en testant toutes les possibilités de clé
def cassage_brutal(message_chiffre,taille_cle1,taille_cle2):
    """Fonction qui tente de retrouver la clé utilisée pour chiffrer le message en testant toutes les possibilités de clé

    Args:
        message_chiffre (str): Message chiffré
        taille_cle1 (int): Taille de la première clé
        taille_cle2 (int): Taille de la deuxième clé
    """
    
    message_len = len(message_chiffre)
    
    # Test toutes les clés possibles pour la taille de clé 1
    for i in range(10 ** taille_cle1):
        key1 = str(i).zfill(taille_cle1)  # Crée une clé de la bonne taille
        
        # Applique la clé sur le message pour le déchiffrer
        decrypted_message = ""
        for j in range(message_len):
            key_char = int(key1[j % taille_cle1])
            decrypted_char = chr((ord(message_chiffre[j]) - key_char) % 256)
            decrypted_message += decrypted_char
        
        # Affiche le message déchiffré si son contenu semble être du texte
        if all(31 < ord(c) < 127 or c in "\n\t" for c in decrypted_message):
            print(f"Clé trouvée pour taille_cle1 {taille_cle1}: {key1}")
            print(f"Message déchiffré : {decrypted_message}")
            return key1
    
    # Test toutes les clés possibles pour la taille de clé 2
    for i in range(10 ** taille_cle2):
        key2 = str(i).zfill(taille_cle2)  # Crée une clé de la bonne taille
        
        # Applique la clé sur le message pour le déchiffrer
        decrypted_message = ""
        for j in range(message_len):
            key_char = int(key2[j % taille_cle2])
            decrypted_char = chr((ord(message_chiffre[j]) - key_char) % 256)
            decrypted_message += decrypted_char
        
        # Affiche le message déchiffré si son contenu semble être du texte
        if all(31 < ord(c) < 127 or c in "\n\t" for c in decrypted_message):
            print(f"Clé trouvée pour taille_cle2 {taille_cle2}: {key2}")
            print(f"Message déchiffré : {decrypted_message}")
            return key2
    
    print("Clé non trouvée.")
    return None


def cassage_astucieux(message_chiffre, longueur_cle_max):
    """Fonction qui tente de retrouver la clé utilisée pour chiffrer le message en testant toutes les possibilités de clé

    Args:
        message_chiffre (str): Message chiffré
        longueur_cle_max (int): Longueur maximale de la clé
    """
    message_len = len(message_chiffre)
    
    # Boucle sur les différentes longueurs de clé possibles
    for taille_cle in range(1, longueur_cle_max + 1):
        cle = ''
        for i in range(taille_cle):
            key_char = None
            max_count = 0
            
            # Compter les occurrences des caractères à une distance de la taille de clé
            for j in range(i, message_len, taille_cle):
                count = 1
                for k in range(j + taille_cle, message_len, taille_cle):
                    if message_chiffre[j:j + taille_cle] == message_chiffre[k:k + taille_cle]:
                        count += 1
                
                # Garder le caractère le plus fréquent pour cette position de la clé
                if count > max_count:
                    max_count = count
                    key_char = message_chiffre[j:j + taille_cle]
            
            # Ajouter le caractère le plus fréquent à la clé
            cle += key_char if key_char else ' '
        
        # Déchiffrer le message avec la clé trouvée
        decrypted_message = ''
        for i in range(message_len):
            key_char = cle[i % taille_cle]
            decrypted_char = chr((ord(message_chiffre[i]) - ord(key_char)) % 256)
            decrypted_message += decrypted_char
        
        print(f"Tentative avec taille de clé {taille_cle}: Clé trouvée : {cle}")
        print(f"Message déchiffré : {decrypted_message}\n")
        
    
message_1 = """Arsène Lupin parmi nous! l'insaisissable cambrioleur dont on racontait les prouesses dans tous les journaux depuis des mois! l'énigmatique personnage avec qui le vieux Ganimard, notre meilleur policier, avait engagé ce duel à mort dont les péripéties se déroulaient de façon si
pittoresque! Arsène Lupin, le fantaisiste gentleman qui n'opère que
dans les châteaux et les salons, et qui, une nuit, où il avait pénétré
chez le baron Schormann, en était parti les mains vides et avait
laissé sa carte, ornée de cette formule: «Arsène Lupin,
gentleman-cambrioleur, reviendra quand les meubles seront
authentiques». Arsène Lupin, l'homme aux mille déguisements: tour à
tour chauffeur, ténor, bookmaker, fils de famille, adolescent,
vieillard, commis-voyageur marseillais, médecin russe, torero
espagnol!"""

message_2 = """LETTRE I
USBEK À SON AMI RUSTAN.
À Ispahan.

Nous n’avons séjourné qu’un jour à Com. Lorsque nous
eûmes fait nos dévotions sur le tombeau de la vierge qui a
mis au monde douze prophètes, nous nous remîmes en
chemin, et hier, vingt-cinquième jour de notre départ
d’Ispahan, nous arrivâmes à Tauris.
Rica et moi sommes peut-être les premiers parmi les
Persans que l’envie de savoir ait fait sortir de leur pays, et
qui aient renoncé aux douceurs d’une vie tranquille pour
aller chercher laborieusement la sagesse.
Nous sommes nés dans un royaume florissant ; mais nous
n’avons pas cru que ses bornes fussent celles de nos
connoissances, et que la lumière orientale dût seule nous
éclairer.
Mande-moi ce que l’on dit de notre voyage ; ne me flatte
point : je ne compte pas sur un grand nombre
d’approbateurs. Adresse ta lettre à Erzeron, où je
séjournerai quelque temps. Adieu, mon cher Rustan. Sois
assuré qu’en quelque lieu du monde où je sois, tu as un ami
fidèle.
De Tauris, le 15 de la lune de Saphar, 1711."""


print(cassage_brutal(message_1, 3, 4))
print(cassage_astucieux(message_1, 4))