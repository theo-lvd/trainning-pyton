a = b = "" #Définie les variables sur "vide" pour les faire exister

while not (a.isdigit() and b.isdigit()): #Quand a et b ne sont pas digital
    a = input("Entrez un premier nombre :") #Redéfintions de la variable a
    b = input("Entrez un deuxieme nombre :") #Redéfintions de la variable b
    if not (a.isdigit() and b.isdigit()): #Quand a et b ne sont pas digital (suite)
        print("Veuillez entrer deux nombres valides") #Indication d'erreur, retour à la ligne 3 (loop)

print(f"Le résultat de {a} + {b} est égal à {int(a) + int(b)}") #Quand a et b sont digitaux, donner résulat 