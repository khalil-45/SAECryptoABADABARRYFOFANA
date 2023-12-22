import unittest
import random
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(os.path.join(ROOT, 'code'))

from programme import double_encrypt, cassage_astucieux, cassage_brutal, read_file


class TestCrypto(unittest.TestCase):

    def test_cassage_brutal(self):
        key1, key2 = 234, 86
        message_clair = "test"
        message_chiffre = double_encrypt(key1, key2, message_clair)

        self.assertEqual(cassage_brutal(message_clair, message_chiffre),
                         (key1, key2))

    def test_cassage_astucieux(self):
        key1, key2 = 234, 86
        message_clair = "test"
        message_chiffre = double_encrypt(key1, key2, message_clair)

        self.assertEqual(cassage_astucieux(message_clair, message_chiffre),
                         (key1, key2))

    def test_random_brutal(self):
        key1, key2 = random.randint(1, 256), random.randint(1, 256)
        nom_fichier = "arsene_lupin.txt"
        message_clair = read_file(nom_fichier)
        message_chiffrer = double_encrypt(key1, key2, message_clair)

        self.assertEqual(cassage_brutal(message_clair, message_chiffrer),
                         (key1, key2))

    def test_random_asstucieux(self):
        key1, key2 = random.randint(1, 256), random.randint(1, 256)
        nom_fichier = "arsene_lupin.txt"
        message_clair = read_file(nom_fichier)
        message_chiffrer = double_encrypt(key1, key2, message_clair)

        self.assertEqual(cassage_astucieux(message_clair, message_chiffrer),
                         (key1, key2))


if __name__ == '__main__':
    unittest.main()
