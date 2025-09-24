import time

liste = [] #On initialise la liste

while True :
    print("\nChoissisez parmi les options suivantes :\n")
    print("1: Ajouter un élément à la liste")
    print("2: Retirer un élément à la liste")
    print("3: Afficher la liste")
    print("4: Vider la liste")
    print("5: Quitter\n")
    user_choice = input("\n👉 Votre choix : ")

    if user_choice.isdigit() : # Contrôle du choix de l'utilisateur
        user_choice = int(user_choice)
        
        if user_choice == 1 : # Ajouter un élément
            ad_liste = (input("\nQue voulez vous ajouter ? : "))
            liste.append(ad_liste)
            print(f"\n✅ {ad_liste} a été ajouté !")

        elif user_choice == 2 : # Supprimer un élément
            r_liste = (input("\nQue voulez vous retier ? : "))
            if r_liste in liste :
                liste.remove(r_liste)
                print(f"\n✅ {r_liste} a été retiré de la liste")
            else :
                print(f"\n❌ {r_liste} n'est pas présent dans la liste")

        elif user_choice == 3 : # Afficher la liste
            if liste :
                print("\nVoici votre liste :\n")
                for i, item in enumerate(liste, 1): #Pour faire une liste propre
                    print(f"{i} - {item}")
            else :
                print("\n🤷 Votre liste est vide !")

        elif user_choice == 4 : # Vider la liste
            liste.clear()
            print("\nVotre liste a été rénitilisée !")

        elif user_choice == 5 : # Quitter
            print("\nA bientôt !❤️")
            time.sleep(1)
            break

        else : 
            print("\n❌ Veuillez renter un nombre entre 1 & 5")
    else :
        print("\n❌ Veuillez rentrer un nombre...")

    time.sleep(1)
    print("\n" + "-" * 50)