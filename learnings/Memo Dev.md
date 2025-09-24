###### **Terminal de commande avec Gitlab :**



ls (permet de lister tous les fichiers à partir de celui dans lequel on se trouve)

ls -la (même chose mais en + détaillé)



pwd (permet d'afficher la racine du fichier dans lequel on se trouve)



cd "nom du dossier"/"..." (pour changer de dossier)

cd .. (pour revenir en arrière)

cd ../.. (remonte de 2 dossiers etc)

cd ~



python -3.13 (lancer python)

py -3.13 "chemin vers fichier python" (executer un scrip python)



clear (supprime les lignes précédentes pour y voir plus clair)



mkdir "nom du dossier" (créer un dossier)

mkdir ../ "nom du dossier" (créer un dossier dans un dossier supérieur)



rm -r "nom du dossier (supprimer un dosser)



touch "nom du fichier"."extension" (créer un fichier)



code (ouvrir visual studio code)

code "nom d'un fichier" (ouvrir directement le fichier spécifié)

code . (ouvre le fichier dans lequel on se trouve)



###### **Code python :**



print()

print("hello world")

print('hello world')

print('je **m\\'**appelle Théo') -> (\\) anti-slash permet d'annuler la fonction première du caractère



"""je m'appelle Théo""" -> chaine de caractère multilignes



\\n -> retour a la ligne

\\f -> saut de page

\\t -> tabulation horizontale

\\v -> tabulation verticale

\\r -> retour chariot

\\a -> caractère d'appel (BEL)

\\b -> caractère de retour arrière



\\u2764 -> imprime un cœur selon la base de données des **caractères unicodes**



raw string = évite l'interprétation des anti-slash en ajoutant un r devant les guillemets Ex : Print(r"grave/trop cool")



Les nombres entiers : 1 10 100 334 232452 20394203482039 (pas de décimales, possible d'écire 100\_000\_000 pour faciliter la lecture)



Les nombres décimaux ou flotant : 5.34 10.0 (avec python seul le . fonctionne)



Les Booléens : 1 = True 0 = False (possible d'associer avec des nombre entiers Ex : True + 1 = 2 car les bool sont une sous classe des nombres entiers.



>>> issubclass(bool, int)

True



bool("ce que je veux") -> permet de vérifier si la chaine de caractère est vraie ou fausse. Ici c'est true car la chaine de caractère comporte au moins 1 caractère.



Tous les objets ont une valeur qui par défaut est true ou false.



Les types :

* str() ou string() -> Chaîne de caractères
* int() ou integer() -> Nombre entiers
* float() -> Nombre décimaux
* bool() ou boolean() -> Booléens



On peut réaliser des conversions : str(5) -> "5" ou int("2") -> 2



**Les variables :**



Une variable est un nom que l'on associe a un objet et qui va nous permettre d'acceder plus facilement a cet objet.

On peut également associer une variable pour appeler une autre variable qui est associé a un objet.

On peut avoir 2 variables différentes qui pointent vers le même objet.

Si on associe une variable a un autre objet, celle-ci pointe le nouvel objet et l'ancien objet disparait et se supprime de la mémoire (Garbage Collector).

Chaque variable occupent de la mémoire. Pour connaitre la place qu'elle prends on peut utiliser la fonction id() qui va nous retourner un numéro d'identification de la variable sous forme d'un nombre entier.



Les différentes affectations de variables : 



* Affectations simples -> nom = objet Ex : a = 5
* Affectations parallèles -> nom, nom = objet, objet Ex :  a, b = 5, 8 ou a, b = b, a pour faire une inversion d'assignation d'objet
* Affectations multiples -> nom = nom = nom = objet Ex :  a = b = c = 5 (toujours finir par l'objet)



single tone = objet unique, comme True ou False, ou les nombres compris entre -5 et 256 inclus, ou les chaines de caractères qui sont en dessous d'un certain nombre de caractères.



small integral caching ?



Règles des variables :



* Ne peut pas commencer par un chiffre
* Ne peut pas contenir d'espace
* Ne peut contenir que des caractères alphanumériques (A-z, 0-9) et le tiret du bas (\_)
* Certains mots sont réservés (print, True, break...)
* Sensible à la casse : prenom ≠ Prenom



Convention de nommage : que des minuscules, ainsi que chaque mots/nombres séparés par un (\_)



Comment changer le type d'une variable : En utilisant les fonctions types str(), int() etc..

>>> a = 5

>>> b = "10"

>>> b = int(b)

>>> print(a + b)

15



Les raisons :

* Pour utiliser les opérateurs mathématiques sur une variable
* Pour faire des comparaisons entre plusieurs variables



Python est un langage fortement typé : 50 ≠ "50"

On n'a pas besoin d'indiquer le type d'une variable lors de sa définition.

On peut changer le type d'une variable n'importe quand.

Pour réaliser certaines opérations, on doit convertir les variables d'un type à un autre.



Pour connaitre le type d'une variable : print(type())

>>> a = 10

>>> print(type(a))

<class 'int'>



Fonction input() : Permet a l'utilisateur de choisir un nombre qui sera associé a une variable

>>> nombre = input("Entrez un nombre: ")

Entrez un nombre: 5

5



**Manipuler les chaînes de caractères :**



Changer la casse (lettres maj et min)

* "Bonjour".upper() -> "BONJOUR"
* "Bonjour".lower() -> "bonjour"
* "bonjour tout le monde".capitalize() -> "Bonjour tout le monde"
* "bonjour tout le monde".title() -> "Bonjour Tout Le Monde"



Remplacer des éléments, méthode .replace()

"bonjour".replace("jou", "soir") -> "bonsoir"

"bonjour bonjour".replace("jour", "soir") -> "bonsoir bonsoir"

"bonjour bonjour".replace(" ", "") -> bonjourbonjour

"bonjour bonjour".replace(" ", "").replace("jour", "soir") -> "bonsoirbonsoir"



Remplacer des éléments, méthode .strip()

* "  bonjour  ".strip(" ujor") -> "bon"
* "  bonjour  ".rstrip(" ujor") -> "  bon" 
* "  bonjour  ".lstrip(" ujor") -> "bonjour  "



Séparer et joindre, .split() .join()

* "1, 2, 3, 4, 5".split(", ) -> \["1", "2", "3", "4", "5"]
* ", ".join("1, 2, 3, 4, 5".split(", ")) -> "1, 2, 3, 4, 5"
* ".".join("1, 2, 3, 4, 5".split(", ")) -> "1.2.3.4.5"



Remplir avec des 0, .zfill()

* "9".zfill(4) -> "0009"



Rechercher dans une chaine de caractère, .is

* "bonjour".islower() -> True
* "Bonjour".islower() -> False
* "49584".isdigit() -> True
* "34AI3".isdigit() -> False



Compter les occurrences .count()

"Bonjour le jour".count("jour") -> 2

"Bonjour le jour".count(" jour") -> 1



Trouver une chaine de caractère .find() .index()

"Bonjour le jour".find("jour") -> 3 (représente le 3ème caractère, on compte le 0 en python donc 0 = B, 1 = o, 2 = n, 3 = j)

"Bonjour le jour".index("jour") -> 3 (en cas de non présence de la chaine de caractère, .index retourne une erreur, alors que .find retourne -1, c'est l'unique différence entre ces 2 fonctions.



















