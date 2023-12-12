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
from sys import exit
from time import time
import timeit
 
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
    """Permute input byte according to permutation table"""
    outputByte = 0
    for index, elem in enumerate(permTable):
        if index >= elem:
            outputByte |= (inputByte & (128 >> (elem - 1))) >> (index - (elem - 1))
        else:
            outputByte |= (inputByte & (128 >> (elem - 1))) << ((elem - 1) - index)
    return outputByte
 
def ip(inputByte):
    """Perform the initial permutation on data"""
    return perm(inputByte, IPtable)
 
def fp(inputByte):
    """Perform the final permutation on data"""
    return perm(inputByte, FPtable)
 
def swapNibbles(inputByte):
    """Swap the two nibbles of data"""
    return (inputByte << 4 | inputByte >> 4) & 0xff
 
def keyGen(key):
    """Generate the two required subkeys"""
    def leftShift(keyBitList):
        """Perform a circular left shift on the first and second five bits"""
        shiftedKey = [None] * KeyLength
        shiftedKey[0:9] = keyBitList[1:10]
        shiftedKey[4] = keyBitList[0]
        shiftedKey[9] = keyBitList[5]
        return shiftedKey
 
    # Converts input key (integer) into a list of binary digits
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
    """Apply Feistel function on data with given subkey"""
    def F(sKey, rightNibble):
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
    """Encrypt plaintext with given key"""
    data = fk(keyGen(key)[0], ip(plaintext))
    return fp(fk(keyGen(key)[1], swapNibbles(data)))
 
def decrypt(key, ciphertext):
    """Decrypt ciphertext with given key"""
    data = fk(keyGen(key)[1], ip(ciphertext))
    return fp(fk(keyGen(key)[0], swapNibbles(data)))  

def text_to_bits(text):
    return ''.join(format(ord(i), '08b') for i in text)

def bits_to_text(bits):
    chars = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        text = ' '.join(lines)
    return text

def double_encrypt(key1, key2, text):
    text_bits = text_to_bits(text)
    encrypted_bits = ''
    for i in range(0, len(text_bits), 8):
        block = int(text_bits[i:i+8], 2)
        encrypted_block = encrypt(key1, block)
        encrypted_block = encrypt(key2, encrypted_block)
        encrypted_bits += format(encrypted_block, '08b')
    return bits_to_text(encrypted_bits)

def cassage_brutal(message_clair, message_chiffre):
    """Tente de retrouver les clés utilisées pour chiffrer le message en testant toutes les possibilités 

    Args:
        message_clair (str) : message clair
        message_chiffre (str) : message chiffré

    Returns:
        tuple : clés utilisées pour chiffrer le message ou None si aucune clé n'a été trouvée
    """    
    message_chiffre_bits = text_to_bits(message_chiffre)
    for i in range(256):
        for j in range(256):
            decrypted_message = ''
            for k in range(0, len(message_chiffre_bits), 8):
                block = int(message_chiffre_bits[k:k+8], 2)
                decrypted_block = decrypt(i, decrypt(j, block))
                decrypted_message += format(decrypted_block, '08b')
            if bits_to_text(decrypted_message) == message_clair:
                return (i, j)
    return None



def cassage_astucieux(message_clair, message_chiffre):
    """Permet de tester moins de possibilité de clés et ainsi réduire le temps d’exécution du cassage.

    Args:
        message_clair (str) : message clair
        message_chiffre (str) : message chiffré

    Returns:
        tuple : clés utilisées pour chiffrer le message
    """

    message_chiffre_bits = text_to_bits(message_chiffre)
    l= 0
    r = 255
    
    for i in [ord('e'), ord('a'), ord('s'), ord('i'), ord('t')]:
        for j in [ord('e'), ord('a'), ord('s'), ord('i'), ord('t')]:
            decrypted_message = ''
            for k in range(0, len(message_chiffre_bits), 8):
                block = int(message_chiffre_bits[k:k+8], 2)
                decrypted_block = decrypt(i, decrypt(j, block))
                decrypted_message += format(decrypted_block, '08b')
            if bits_to_text(decrypted_message) == message_clair:
                return (i, j)
            
    if l == r:
        return None
    elif l + 1 == r:
        return None
    else:
        mid = (l + r) // 2
    
    for i in range(l, mid):
        for j in range(l, mid):
            decrypted_message = ''
            for k in range(0, len(message_chiffre_bits), 8):
                block = int(message_chiffre_bits[k:k+8], 2)
                decrypted_block = decrypt(i, decrypt(j, block))
                decrypted_message += format(decrypted_block, '08b')
            if bits_to_text(decrypted_message) == message_clair:
                return (i, j)
    return None

          
                
        
    

    


       
    
    
    

def main():
    
    fic = input("Entrez le nom du fichier à chiffrer ou bien du texte : ")
    mess_clair = read_file(fic)
    mess_chiffre = double_encrypt(1, 30, mess_clair)
    fonc = input("Entrez le nom de la fonction de cassage à utiliser : ")
    if fonc == "cassage_brutal":
        print("Les clés utilisées sont : ", cassage_brutal(mess_clair, mess_chiffre))
        print("temps d'execution : ", timeit.timeit(lambda: cassage_brutal(mess_clair, mess_chiffre), number=1))
    elif fonc == "cassage_astucieux":
        print("Les clés utilisées sont : ", cassage_astucieux(mess_clair, mess_chiffre))
        print("temps d'execution : ", timeit.timeit(lambda: cassage_astucieux(mess_clair, mess_chiffre), number=1))
        
    else:
        print("Fonction de cassage inconnue") 
        
        
if __name__ == "__main__":
    main()           
        
        
    
    
    







file_path = 'arsene_lupin_extrait.txt'
message_clair = read_file(file_path)
message_chiffre = double_encrypt(10, 100, message_clair)
message_dechiffre = cassage_brutal(message_clair, message_chiffre)
print(message_chiffre)
print(message_dechiffre)