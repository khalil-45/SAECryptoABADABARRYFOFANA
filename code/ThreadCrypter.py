import threading
import timeit
import random

class MyThread(threading.Thread):
    def __init__(self, func, message_clair, message_chiffre):
        threading.Thread.__init__(self)
        self.func = func
        self.message_clair = message_clair
        self.message_chiffre = message_chiffre
        
    def run(self):
        print("\nLes clés utilisées sont : ", self.func(self.message_clair, self.message_chiffre), "\n")
        print("temps d'execution : ", timeit.timeit(lambda: self.func(self.message_clair, self.message_chiffre), number=1))