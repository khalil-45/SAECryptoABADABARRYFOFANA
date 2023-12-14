<h1 align="center">
  <br>
  <a href="https://www.univ-orleans.fr/fr/iut-orleans"><img src="https://th.bing.com/th/id/OIP.xT34StZ6xa8FAOOTWYdZFwHaB1?pid=ImgDet&rs=1" alt="IUT d'Orléans" width="200"></a>
  <br>
  Team de décryptage AKI
  <br>
</h1>

<h4 align="center">Équipe de décryptage initiée par M. Gillet composé de M. FOFANA, M. BARRY et M. ABADA.</h4>

<p align="center">
  <a href='./sujet_etu.pdf'>
    <img src="images/THE_PROJECT_1.png"
         alt="Le projet" width = 150>
  </a>

<p align="center">
  <a href="#le-projet">Le Projet</a> •
  <a href="#première-partie">La Première Partie</a> •
  <a href="#deuxième-partie">La Deuxième Partie</a> •
  <a href="#troisième-partie">La Troisième Partie</a> •
  <a href="#conclusion">Conclusion</a> •
  <a href="#license">License</a>
</p>

![Alt text](images/hacker.gif)
** **
## Le Projet

* Contexte
  - M. GILLET nous appelle une deuxième fois suite à notre merveilleuse réussite avec la première mission qu'il nous a attribué.
  - Alice et Bob, deux tourtereaux qui s'aiment passionnément, vivent un amour secret depuis des années. Comment arrivent-t-ils à garder ce secret ? L'échang de message chiffrés. Ils utilisent un protocole se nommant PlutotBonneConfidentialité dont il peut être résumer ainsi : 
    - A l’aide d’un protocole cryptographique asymétrique, ils s’échangent une clé de session. Cette clé servira à
    chiffrer les communications futures.
    - Une fois cette clé choisie et échangée, le chiffrement des messages s’opère grâce à un protocole cryptographique
    symétrique. Ils peuvent ainsi communiquer en toute liberté !
  
  - Eve, la meilleure amie d'Alice, souhaite réveler au grand jour leur histoire et veut donc déchiffrer leur communication.
* Notre employeur nous a donc aider en structurant 4 parties. La première est un peu pour tâter le terrain, comprendre le sujet. La deuxième est le développement d'un protocol expérimental permettant de mettre en évidence la différence de sécurité entre les deux
protocoles AES et RSA. La troisième est l'analyse des messages envoyés par Alice et Bob. Enfin, la dernière et quatrième partie, concerne la réponse à plusieurs questions afin d'aller plus loin dans le travail.

## Première partie
* **RSA** est un protocole de cryptographie asymétrique qui est considéré comme sûr lorsqu'il est utilisé correctement. Cela signifie que si Alice et Bob utilisent des clés de taille suffisante et suivent les bonnes pratiques (par exemple, ne pas réutiliser les clés, garder les clés privées en sécurité), alors Eve ne devrait pas être en mesure de déchiffrer les messages chiffrés avec RSA.
**Cependant**, il est important de noter que la sécurité de RSA repose sur la difficulté de la factorisation des grands nombres premiers. Si Eve avait accès à une puissance de calcul suffisante (par exemple, un ordinateur quantique), elle pourrait théoriquement factoriser les clés RSA et déchiffrer les messages. Mais pour l'instant, avec la technologie actuelle, cela reste largement hors de portée.
**En conclusion**, si RSA est utilisé correctement, Eve ne devrait pas être en mesure de déchiffrer les communications entre Alice et Bob. Cependant, la sécurité en informatique est un domaine en constante évolution et il est important de rester informé des dernières avancées et menaces.

* L’algorithme SDES (Simplified Data Encryption Standard) est considéré comme peu sécurisé en raison de la taille relativement courte de sa clé. En effet, SDES utilise une clé de 10 bits, ce qui signifie qu’il y a 2^10, soit 1024 clés possibles.
Dans le contexte d’une attaque par force brute, un attaquant essaierait toutes les combinaisons possibles jusqu’à trouver la bonne clé. Avec seulement 1024 clés possibles, un ordinateur moderne pourrait essayer toutes ces combinaisons en un temps très court, rendant l’algorithme vulnérable à ce type d’attaque.
De plus, SDES est un algorithme de chiffrement symétrique, ce qui signifie que la même clé est utilisée pour le chiffrement et le déchiffrement. Si la clé est découverte lors d’une attaque par force brute, l’attaquant aurait alors accès à toutes les données chiffrées avec cette clé.
Pour ces raisons, SDES n’est pas considéré comme un algorithme de chiffrement sécurisé pour protéger des informations sensibles dans un environnement où les attaques par force brute sont possibles. Des algorithmes de chiffrement plus robustes, tels que l’AES (Advanced Encryption Standard), sont recommandés pour une meilleure sécurité.

* Le Double DES est une technique de chiffrement qui utilise deux instances de DES sur le même texte en clair. Dans les deux instances, il utilise des clés différentes pour chiffrer le texte en clair. Cependant, bien que le Double DES utilise une clé de 112 bits, il n’offre qu’un niveau de sécurité de 2^56 et non de 2^112. C'est à cause de l'attaque “rencontre au milieu” qui peut être utilisée pour percer le Double DES.
Dans une attaque de rencontre au milieu, l'attaquant utilise toutes les clés possibles pour crypter le texte en clair et stocker les résultats. Ensuite, il utilise toutes les clés disponibles pour déchiffrer le texte qui a été chiffré. L'attaquant a trouvé les deux clés si l'une des valeurs de déchiffrement correspondait à l'une des valeurs de chiffrement stockées. 
Le nombre d’essais pour trouver la clé dans une attaque de rencontre au milieu est de 2^56, ce qui est beaucoup moins que les 2^112 essais nécessaires pour une attaque par force brute sur une clé de 112 bits. C’est pourquoi le Double DES n’offre pas un niveau de sécurité beaucoup plus élevé que le DES simple, malgré l’utilisation d’une clé deux fois plus longue.

## Deuxième partie
1. Oui, c'est un problème. L'augmentation de la taille de la clé de l'algorithme de chiffrement à 256 bits rend la méthode de force brute pratiquement impossible. 
La force brute consiste à essayer toutes les combinaisons possibles de clés jusqu'à ce que la bonne soit trouvée. Avec une clé de 256 bits, il y a 2^256 combinaisons possibles. C'est un nombre extrêmement grand qui dépasse largement la capacité de calcul actuelle. Même avec les ordinateurs les plus puissants, cela prendrait des milliards d'années pour essayer toutes les combinaisons.
De plus, l'AES (Advanced Encryption Standard) est un algorithme de chiffrement plus complexe et plus sûr que le SDES. Il est largement utilisé dans le monde entier pour protéger les informations sensibles. Il est conçu pour résister à toutes les attaques connues lorsqu'il est correctement mis en œuvre.
Donc, oui, le passage à l'AES avec des clés de 256 bits est un problème pour Eve si elle veut casser le chiffrement par force brute.

2. 
```python
import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Double SDES
key1 = get_random_bytes(8)
key2 = get_random_bytes(8)
message = "Your message here"

start = time.time()
encrypted_message = double_encrypt(key1, key2, message)
decrypted_message = double_decrypt(key1, key2, encrypted_message)
end = time.time()

print(f"Double SDES took {end - start} seconds.")

# AES
key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_EAX)
message = b'Your message here'

start = time.time()
ciphertext, tag = cipher.encrypt_and_digest(message)
cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted_message = cipher.decrypt_and_verify(ciphertext, tag)
end = time.time()

print(f"AES took {end - start} seconds.")
```
## Troisième partie

## Quatrième partie
1. Ce n'est clairement pas une bonne pratique. AES est un algorithme de chiffrement symétrique, ce qui signifie que la même clé est utilisée pour le chiffrement et le déchiffrement. Si la clé est compromise, l'attaquant peut déchiffrer toutes les données chiffrées avec cette clé. 
Afin de respecter la bonne pratique, les deux personnes pratiquant l'AES se doivent de changer régulièrement de clé, pour garder une sécurité élevée. De plus, il est préférable d'utiliser des clés fortes.
Pour une sécurité optimale, ces bonnes pratiques sont nécessaire pour réduire l'impact si une clé venait à être compromise.

2. 

3. 

4. Plusieurs réseaux sociaux utilisent le chiffrement de bout en bout, notamment Google RCS, WhatsApp et Telegram.

## Conclusion



## Credits

Nous tenons à remercier tous le personnel de l'IUT d'Orléans pour leur soutien et leur aide dans ce projet. Nous tenons aussi à remercier M. GILLET pour nous avoir confié ce projet, ce qui nous a permis de nous améliorer dans le domaine de la cryptographie. De plus, cela signifie que notre employeur [M. GILLET](noel.gillet@univ-orleans.fr) a confiance en nous et nous le remercions pour cela. 

## License

M. GILLET, M. FOFANA, M. BARRY et M. ABADA -
AKI Team - IUT d'Orléans

<p align="right">(<a href="#le-projet">back to top</a>)</p>
