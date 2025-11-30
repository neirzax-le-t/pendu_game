# Import d'un mot depuis une liste hebergé sur internet

import random
import requests

url="https://openlexicon.fr/datasets-info/Liste-de-mots-francais-Gutenberg/liste.de.mots.francais.frgut.txt"
reponse=requests.get(url)
liste_mots = reponse.text.splitlines()
liste_joueur=[]

# Mise du compte d'erreurs à 0

erreurs=0
max_erreurs=7
#vérification de si il est composé de caractere valide ou non avec isalpha
while True:
    mot = random.choice(liste_mots).lower()
    if all(c.isalpha() or c in "-'" for c in mot):
        break

char_list = list(mot)

# Affichage de la longueur du mot et des tirets pour aider le joueur
mot_trouve = [c if c in "-'" else "_" for c in char_list]
print("Mot à deviner:"," ".join(mot_trouve))

#Boucle qui permet au joueur de saisir des lettres pour trouver  le mot
while erreurs < max_erreurs:
        joueur=input(str("Veuillez saisir une lettre:")).strip().lower()
        if (not joueur.isalpha()) or (len(joueur) !=1):
            print("Veuillez saisir une lettre")
            continue
        if joueur in liste_joueur:
            print("Vous avez déjà proposé cette lettre")
            continue
        
        liste_joueur.append(joueur)
# Si la la lettre est bien trouvé, l'ajouté à la liste selon le bonne endroit
        if joueur in char_list:
            print("Bonne lettre")
            for i in range(len(char_list)):
                if char_list[i] == joueur:
                    mot_trouve[i]=joueur
                    print("Mot à deviner :", " ".join(mot_trouve))
                    
# Gestion des erreurs
        else:
            erreurs += 1
            print(f"Mauvaise lettre {erreurs}/{max_erreurs}")
        if erreurs == max_erreurs:
            print(f"Vous êtes pendu le mot était {mot}")
# Gestion de la victoire 
        if "_" not in mot_trouve:
            print(f"Félicitations vous avez gagné le mot était {mot}")
            break

            
            
            
