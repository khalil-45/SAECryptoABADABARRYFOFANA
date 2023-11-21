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

![Alt text](images/4k_crypto.jpg)
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

- En supposant que RSA soit utilisé correctement, Eve peut-elle espérer en venir à bout ? En vous appuyant sur
votre cours, justifiez votre réponse :  

   Si la mise en œuvre de RSA est correcte et utilise des clés suffisamment longues, il serait extrêmement difficile pour Eve de déchiffrer les messages en attaquant directement RSA pour récupérer la clé de session. RSA repose sur le problème de factorisation des grands nombres, qui est difficile à résoudre pour de grandes clés.

  Cependant, si Eve parvient à compromettre soit la génération des clés RSA, soit la manière dont la clé de session est échangée entre Alice et Bob, alors elle pourrait potentiellement accéder aux communications. 
  
  Donc, en supposant que RSA soit utilisé correctement, la sécurité du système repose sur la robustesse de la génération et de l'échange de la clé de session. Si ces étapes sont bien sécurisées, il serait extrêmement difficile pour Eve de déchiffrer les messages et de découvrir le secret d'Alice et Bob.

- En quoi l’algorithme SDES est-il peu sécurisé? Vous justifierez votre réponse en analysant le nombre d’essai
nécessaire à une méthode “force brute” pour retrouver la clé :  

    L'algorithme SDES est peu sécurisé car il est possible de retrouver la clé en utilisant une méthode de force brute. En effet, la clé est composée de 10 bits. Il est donc possible (ou du moins ) de tester toutes les combinaisons possibles. Il y a donc 2^10 combinaisons possibles. Il faut donc 1024 essais pour retrouver la clé.

- Est-ce que double SDES est-il vraiment plus sur? Quelle(s) information(s) supplémentaire(s) Eve doit-elle
récupérer afin de pouvoir espérer venir à bout du double DES plus rapidement qu’avec un algorithme brutal?
Décrivez cette méthode astucieuse et précisez le nombre d’essai pour trouver la clé : 

    Double SDES est plus sûr que SDES car il est impossible de retrouver la clé en utilisant une méthode de force brute. En effet, la clé est composée de 20 bits. Il est donc impossible de tester toutes les combinaisons possibles. Il faut donc 2^20 essais pour retrouver la clé. Il faut donc 1048576 essais pour retrouver la clé.

## Deuxième partie

## Troisième partie

## Quatrième partie

## Conclusion



## Credits

Nous tenons à remercier tous le personnel de l'IUT d'Orléans pour leur soutien et leur aide dans ce projet. Nous tenons aussi à remercier M. GILLET pour nous avoir confié ce projet, ce qui nous a permis de nous améliorer dans le domaine de la cryptographie. De plus, cela signifie que notre employeur [M. GILLET](noel.gillet@univ-orleans.fr) a confiance en nous et nous le remercions pour cela. 

## License

M. GILLET, M. FOFANA, M. BARRY et M. ABADA -
AKI Team - IUT d'Orléans

<p align="right">(<a href="#le-projet">back to top</a>)</p>
