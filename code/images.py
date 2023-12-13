# pylint: disable=E0401

from PIL import Image

def extract_key(img_with_key):
    # Ouvrir les images avec Pillow
    with_key = Image.open(img_with_key)

    # Extraire la clé cachée dans l'image
    extracted_key = ""
    for x in range(100):
            pixel2 = with_key.getpixel((x, 0))
            extracted_key+= str(pixel2%2)    
    return extracted_key             
                
# Appel de la fonction pour extraire la clé
extracted_key = extract_key("rossignol2.bmp")
print("Clé extraite :", extracted_key)


