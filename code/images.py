# pylint: disable=E0401

from PIL import Image

def extract_key(img_with_key):
    """ Fonction qui permet d'extraire la clé cachée dans une image

    Args:
        img_with_key (str): Chemin vers l'image contenant la clé

    Returns:
        str: Clé extraite
    """    
    # Ouvrir les images avec Pillow
    with_key = Image.open(img_with_key)

    # Extraire la clé cachée dans l'image
    extracted_key = ""
    for x in range(64): 
            pixel2 = with_key.getpixel((x, 0)) # Récupérer le pixel de l'image
            extracted_key+= str(pixel2%2)  # Ajouter le bit de poids faible du pixel à la clé extraite  
    return extracted_key             
                
# Appel de la fonction pour extraire la clé
extracted_key = extract_key("rossignol2.bmp")
print("Clé extraite :", extracted_key)


