"""Ce module est le point d'entrée de l'application."""
#pylint: disable=E0401, E0611, W0611,W0718
import random
import threading
from code.programme import double_encrypt, cassage_brutal, cassage_astucieux,\
    encrypt_text,decrypt_text
from colorama import Fore, Style


def read_file(file_path):
    """Fonction qui lit un fichier et retourne son contenu.
    
    Args:
    file_path (str): Chemin du fichier à lire.

    Returns:
    text (str): Contenu du fichier.
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
            text = ' '.join(lines)
        print("Le fichier à été lu avec succès\n")
        return text
    except Exception:
        return file_path


def worker(func, message_clair, message_chiffre):
    """Fonction qui exécute une fonction avec des arguments.

    Args:
        func (): Fonction à exécuter.
        message_clair (str): le message
        message_chiffre (str): le message chiffré
    """
    print("\nLes clés utilisées sont : ", func(message_clair, message_chiffre),
          "\n")


def main():
    """
    Fonction principale de l'application.
    """
    while True:
        choix = choose_option()
        if choix == "1":
            message_clair = read_file(
                input("\nEntrez le chemin du fichier ou un texte : "))
            print("\nLe message crypté est : ",
                  encrypt_text(get_key_input(), message_clair), "\n")
        elif choix == "2":
            message_chiffre = read_file(
                input("\nEntrez le chemin du fichier ou un texte : "))
            print("\nLe message décrypté est : ",
                  decrypt_text(get_key_input(), message_chiffre), "\n")
        elif choix == "3":
            print("\n1 - Cassage brutal\n2 - Cassage astucieux\n")
            option = input("\nEntrez l'option à choisir : {1 / 2} : ")
            if option == "1":
                trouver_cle("cassage_brutal")
            elif option == "2":
                trouver_cle("cassage_astucieux")
        elif choix == "4":
            break
        else:
            print("\nVeuillez entrer une option valide\n")


def choose_option():
    """
    Demande à l'utilisateur de choisir une option.

    Returns:
    option (str): Option choisie.
    """
    while True:
        print(
            "\n1 - Chiffrer un message\n2 - Casser un message\
            \n3 - Trouver les clés utilisées\n4 - Quitter\n"
        )
        option = input("\nEntrez l'option à choisir : {1 / 2 / 3 / 4} : ")
        if option in ["1", "2", "3", "4"]:
            return option
        print("\nOption inconnue\n")
        print("Veuillez choisir une option valide")


def trouver_cle(fonc):
    """
    Trouve les clés utilisées pour chiffrer un message.

    Args:
    fonc (function): Fonction de cassage à exécuter.
    """
    option_dispo = {
        "cle aléatoire": "desactivé",
        "cle manuelle": "activé",
        "crypter le message": "desactivé",
    }
    while True:
        print("Voici la liste des options disponibles : ")
        afficher_options(option_dispo)
        key1, key2 = generate_random_keys(
        ) if option_dispo["cle aléatoire"] == "activé" else get_keys_input()
        message_clair = read_file(
            input("\nEntrez le chemin du fichier ou un texte : "))
        while True:
            rep = input("Voulez vous entrer le message chiffré ? \n PS : Nous pouvons crypter le message nous-même vous n'avez pas à le rentrer entièrement\n   (O/N) : ")
            if rep == "O":
                message_chiffre = read_file(
                    input("\nEntrez le chemin du fichier ou un texte : "))
                break
            if rep == "N":
                message_chiffre = double_encrypt(key1, key2, message_clair)
                break

            print("\nVeuillez entrer une réponse valide\n")

        run_cassage_with_threads(fonc, message_clair, message_chiffre)
        run_cassage_without_threads(fonc, message_clair, message_chiffre)
        break


def get_key_input():
    """
    Demande à l'utilisateur d'entrer une clé.

    Returns:
    key (int): Clé.
    """
    while True:
        try:
            key = int(input("\nEntrez la clé : "))
            return key
        except ValueError:
            print("\nVeuillez entrer un nombre entier\n")


def get_keys_input():
    """
    Demande à l'utilisateur d'entrer deux clés.

    Returns:
    key1 (int): Première clé.
    key2 (int): Deuxième clé.
    """
    while True:
        try:
            key1 = int(input("\nEntrez la première clé : "))
            key2 = int(input("\nEntrez la deuxième clé : "))
            print("\nLes clés utilisées sont : ", key1, key2, "\n")
            return key1, key2
        except ValueError:
            print("\nVeuillez entrer des nombres entiers\n")


def afficher_options(option_dispo):
    """
    Affiche les options disponibles.

    Args:
    option_dispo (dict): Dictionnaire contenant les options disponibles.
    """
    print("\n" + Fore.GREEN + "Vert : activé\n")
    print(Fore.RED + "Rouge : désactivé\n")
    print(Style.RESET_ALL)
    while True:
        print("\nVeuillez choisir l'option crypter le message lorsque vous avez fini de choisir\
              l'option pour les clés\n")
        for nb, option in enumerate(option_dispo):
            if option_dispo[option] == "activé":
                print(Fore.GREEN + str(nb + 1) + " - " + option)
            else:
                print(Fore.RED + str(nb + 1) + " - " + option)
        print(Style.RESET_ALL)
        option = input("\nEntrez l'option à choisir : ")
        if option in [str(nb + 1) for nb in range(len(option_dispo))
                      ]:  #Si l'option est valide
            option_dispo = activer_option(option, option_dispo)
        else:
            print("\nVeuillez entrer une option valide\n")
        if option_dispo["crypter le message"] == "activé":
            return option_dispo


def activer_option(option, option_dispo):
    """
    Active une option.

    Args:
    option (str): Option à activer.
    option_dispo (dict): Dictionnaire contenant les options disponibles.

    Returns:
    option_dispo (dict): Dictionnaire contenant les options disponibles.
    """
    option = int(option)
    if option == 1:
        option_dispo["cle aléatoire"] = "activé"
        option_dispo["cle manuelle"] = "desactivé"
    elif option == 2:
        option_dispo["cle manuelle"] = "activé"
        option_dispo["cle aléatoire"] = "desactivé"
    elif option == 3:
        option_dispo["crypter le message"] = "activé"
    return option_dispo


def generate_random_keys():
    """
    Génère deux clés aléatoires.

    Returns:
    key1 (int): Première clé aléatoire.
    key2 (int): Deuxième clé aléatoire.
    """
    key1 = random.randint(1, 256)
    key2 = random.randint(1, 256)
    print("\nLes clés utilisées sont : ", key1, key2, "\n")
    return key1, key2


def run_cassage_with_threads(fonc, mess_clair, mess_chiffre):
    """
    Exécute la fonction de cassage avec des threads.

    Args:
    fonc (function): Fonction de cassage à exécuter.
    mess_clair (str): Message clair.
    mess_chiffre (str): Message chiffré.
    """
    print("\nAvec threads : ")
    thread = threading.Thread(target=worker,
                              args=(globals()[fonc], mess_clair, mess_chiffre))
    thread.start()
    thread.join()


def run_cassage_without_threads(fonc, mess_clair, mess_chiffre):
    """
    Exécute la fonction de cassage sans utiliser de threads.

    Args:
    fonc (function): Fonction de cassage à exécuter.
    mess_clair (str): Message clair.
    mess_chiffre (str): Message chiffré.
    """
    print("\nSans threads : ")
    keys = globals()[fonc](mess_clair, mess_chiffre)
    print("\nLes clés utilisées sont : ", keys, "\n")


if __name__ == "__main__":
    main()
