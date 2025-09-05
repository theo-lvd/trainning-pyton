continuer = "o"
while continuer == "o" :
    print("On continue !")
    choix = input("Voulez_vous continuer ? o/n ")
    if choix != "o" :
        choix = input("Vous êtes sur ? o/n ")
        if choix == "o" :
            break

#Solution plus simple mais plus opti qui fonctionne aussi :

continuer = "o"
while continuer == "o" :
    continuer = input("Voulez_vous continuer ? o/n ")