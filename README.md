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
1. L'utilisation de clés AES de 256 bits est généralement considérée comme une amélioration de la sécurité, cela peut poser des défis potentiels en termes de performances et de compatibilité. Évaluer les compromis entre sécurité, performance et exigences du système est essentiel pour déterminer si ce changement pose un problème significatif pour Eve.

2. Le temps d'exécution de l'algorithme de chiffrement AES dépend de plusieurs facteurs, notamment la taille de la clé, le mode de chiffrement et le matériel utilisé. Dans le cas d'AES-256, le temps d'exécution dépend de la taille de la clé (256 bits), du mode de chiffrement (CBC) et du matériel utilisé (CPU, GPU, FPGA, etc.). Si on compare le chiffrement AES avec le chiffrement SDES, il est plus rapide que SDES que ce soit sur de petites clés ou de grandes clés car sa conception a été optimisée pour une large gamme de tailles de clés, et il est largement implémenté matériellement et logiciellement, ce qui lui confère des performances plus rapides même avec des clés plus grandes. SDES dans son cas, se dégradent considérablement lorsqu'il est utilisé avec des clés plus grandes, tandis que AES maintient généralement de bonnes performances même avec des clés plus grandes en raison de son approche plus moderne et de ses optimisations.

Temps d'exécution de l'algorithme de chiffrement AES obtenu : 4.654099939216394e-05 s

** Configuration de l'ordinateur Macbbok air M2 ** :
  - Processeur : Apple M2 (8 cœurs, 16 threads)
  - RAM : 8 Go
  - GPU : Apple M2
  - Système d'exploitation : macOS Sonoma 14.0

Temps d'exécution de l'algorithme de déchiffrement AES obtenu avec la même configuration en moyenne : 2.795899945340352e-05

Temps d'exécution de l'algorithme de chiffrement SDES obtenu avec la même configuration en moyenne : 0.0007921660007923492 s

3. 
### Estimation du temps de cassage d'AES-256 :

- **Configuration de l'ordinateur** :
  - Processeur : Intel Core i7-11700K (8 cœurs, 16 threads)
  - RAM : 16 Go
  - GPU : NVIDIA RTX 3070
  - Système d'exploitation : Windows 10

- **Complexité de l'algorithme de cassage** : Supposons une attaque par force brute exhaustive.
- **Longueur de la clé AES** : Clé de 256 bits

La clé AES-256 a une longueur de 256 bits, ce qui signifie qu'il y a \(2^{256}\) combinaisons possibles pour la clé.

En supposant un taux de test de clés de l'ordre de plusieurs milliards de clés par seconde (ce qui est assez optimiste pour une attaque par force brute), calculons le temps approximatif nécessaire pour tester toutes les combinaisons possibles de clés :


Nombre de combinaisons possibles pour la clé = 2^{256}


Si nous testons, par exemple, 1 milliard (1 x \(10^9\)) de clés par seconde :


Nombre de secondes nécessaires = Nombre de combinaisons possibles\Nombre de clés testées par seconde



Temps nécessaire = 2^{256} / 1 * 10^9


Calculons :


Temps nécessaire = 2^{256} / (1 * 10^9) = 1.1579 * 10^{60} secondes


En convertissant cela en années :


Temps nécessaire en années :  1.1579 * 10^60 / (60 * 60 * 24 * 365) = 3.6716 * 10^49


Cela dépasse de loin l'âge de l'univers (environ 13,8 milliards d'années).

### Remarque :
C'est une estimation simplifiée et optimiste. En réalité, une attaque par force brute contre AES-256 avec les ressources informatiques actuelles est considérée comme impossible en raison du nombre colossal de combinaisons possibles. Les estimations reposent sur des suppositions sur les capacités de calcul et peuvent varier en fonction de nombreux autres facteurs, y compris les avancées technologiques et les nouvelles méthodes d'attaque.

3. 


## Troisième partie

## Quatrième partie

## Conclusion



## Credits

Nous tenons à remercier tous le personnel de l'IUT d'Orléans pour leur soutien et leur aide dans ce projet. Nous tenons aussi à remercier M. GILLET pour nous avoir confié ce projet, ce qui nous a permis de nous améliorer dans le domaine de la cryptographie. De plus, cela signifie que notre employeur [M. GILLET](noel.gillet@univ-orleans.fr) a confiance en nous et nous le remercions pour cela. 

## License

M. GILLET, M. FOFANA, M. BARRY et M. ABADA -
AKI Team - IUT d'Orléans

<p align="right">(<a href="#le-projet">back to top</a>)</p>
