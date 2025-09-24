mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."
mdp_correct = "Inscription terminée."

if len(mdp) == 0 :
     print(mdp_trop_court.upper())
elif len(mdp) < 8 :
     print(mdp_trop_court.capitalize())
elif mdp.isdigit() :
     print("ERREUR : Votre mdp ne contient que des chiffres.")
elif not "a" <= mdp <= "z":
     print("ERREUR : Il manque des minuscules.")
elif mdp.isalnum :
     print("ERREUR : Il manque un caractère spéclial.")
else :
     print(mdp_correct)

