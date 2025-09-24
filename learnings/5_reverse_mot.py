mot = "Python"
mot_reverse = reversed(mot)

for lettre in mot_reverse :
    print(lettre)

# Plus opti :

for lettre in reversed("Python") :
    print(lettre)