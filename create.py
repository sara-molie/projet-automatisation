import csv
import os
import pandas as pd


def create():
    print("Tu as choisis 'Créer un AEF'.")
    
    # Demander à l'utilisateur le nom du fichier + le mettre dans le dossier et faire les vérifications
    file_name = input("Entrez le nom du fichier CSV : ")
    csv_folder = "csv"

    if not os.path.exists(csv_folder):  # Vérifie si le dossier csv existe sinon le crée
        os.mkdir(csv_folder)
    csv_file_path = os.path.join(csv_folder, file_name)

    if os.path.exists(csv_file_path):  # Vérifie si le fichier existe
        print("\n\033[91mLe fichier existe déjà. Veuillez choisir un autre nom.\033[0m")
    else:
        with open(csv_file_path, mode='w', newline='') as file:  # Donne l'accès pour créer le fichier
            writer = csv.writer(file)
        print("Le fichier CSV a été créé dans le dossier.")

        # Demander à l'utilisateur l'état initial et l'état final
        initial_state = input("Entrez le seul état initial de l'automate : ")

        # Vérification si l'utilisateur a entré plusieurs valeurs avec ','
        if ',' in initial_state:
            print("\033[91mErreur : Un automate à état fini possède un seul état initial mais peut avoir plusieurs états finaux.\033[0m\n")
            return

        final_state = input("Entrez l'état final de l'automate : ")

        # Demander à l'utilisateur de saisir les transitions sous forme de matrice
        print("\nEntrez les transitions de votre automate sous forme de matrice (séparez les éléments par des espaces) :")
        print("Pour finir mettre 'ok'\n")
        
        transitions = []  # Pour stocker les transitions dans une liste

        #on effectue une boucle tant qu'il n'appuie pas sur ok on continu
        while True:
            transition_input = input()
            if transition_input == 'ok':
                break
            else: #et on regarde la forme 
                transition_data = transition_input.split()
                if len(transition_data) != 3:
                    print("\033[91mErreur : Format de transition invalide.\033[0m")
                else:
                    transitions.append(transition_data)
        
        # Créer un fichier CSV avec le nom spécifié pour enregistrer les données
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Écrire les données dans le fichier CSV
            writer.writerow(['État Initial ', initial_state])
            writer.writerow(['État Final ', final_state])
            writer.writerow([])
            writer.writerow(['Premier etat', 'Deuxieme etat', 'Entrée'])
            for transition in transitions:
                writer.writerow(transition)   
        print("\n")
        print(f"Les données ont été enregistrées dans le fichier {file_name}.")

def modifier():
    print("Tu as choisi 'Modifier un AEF'.")
    
    # Demande à l'utilisateur le nom du fichier CSV à modifier
    #point negatif : il faut se rappeler du nom 

#On peut meme afficher les fichier deja exisants et lui demander de choisir sous forme de menu 
    file_name = input("Entrez le nom du fichier CSV à modifier : ")
    csv_folder = "csv"
    csv_file_path = os.path.join(csv_folder, file_name)

    if not os.path.exists(csv_file_path):  # Vérifier si le fichier existe
        print("\n\033[91mLe fichier n'existe pas. Veuillez choisir un fichier existant.\033[0m")
        return
    
    # Lire le fichier CSV existant
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
    
    # Affiche les données actuelles
    print("\nDonnées actuelles du fichier CSV :")
    #je les separe avec un ' ' sinon il met 2fois ','
    for row in data:
        print(' '.join(row))
    
    # Demande à l'utilisateur de saisir de nouvelles données
    print("\nEntrez les nouvelles données pour le fichier CSV (ou sur Entrée pour garder les valeurs actuelles) :")
    
#ATTENTION JE CROIS QUE POUR LES TRANSITIONS IL SUPPRIME TOUT, IL EN AJOUTE PAS 
# A AMELIORER POUR AJOUTER DES TRANS

    # l'état initial
    new_initial_state = input(f"Nouvel état initial ({data[0][1]}): ") #on le met dans une liste de liste (premiere : etat initial deuxieme : element)
    if new_initial_state: # si on change l'etat alors il prends la nouvelle valeur --> exemple q1 q2 c devient q1 q2 a 
        data[0][1] = new_initial_state
    
    # l'état final
    new_final_state = input(f"Nouvel état final ({data[1][1]}): ") 
    if new_final_state:
        data[1][1] = new_final_state
    

    # les nouvelles transitions
    new_transitions = [] #on le stock toujours dans une liste
    print("\nEntrez les nouvelles transitions ou 'ok' pour terminer :")
    while True:
        transition_input = input()
        if transition_input == 'ok':
            break
        else: # condition pour etre au bon format c'est a dire q1, q1, a , elle verifie la longueur 
            transition_data = transition_input.split()
            if len(transition_data) != 3:
                print("\033[91mErreur : Format de transition invalide.\033[0m")
            else:
                new_transitions.append(transition_data)
    
    if new_transitions:
        data[3:] = new_transitions  # Remplacer les transitions existantes par les nouvelles
    
    # Enregistrer les modifications dans le fichier CSV
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
    
    print("\nLes modifications ont été enregistrées dans le fichier CSV.")
    

#fonction pour supprimer
def supprimer():
    print("Tu as choisi 'Supprimer un fichier'.")
    
    #  le nom du fichier CSV à supprimer
    # toujours la possibilité de coder un menu contenant tous les fichier csv
    file_name = input("Entrez le nom du fichier CSV à supprimer : ")
    csv_folder = "csv"
    csv_file_path = os.path.join(csv_folder, file_name)

    if os.path.exists(csv_file_path):  # Vérifier si le fichier existe
        confirmation = input(f"Êtes-vous sûr de vouloir supprimer le fichier '{file_name}' ? (Oui/Non) : ")
        if confirmation.lower() == 'oui': #condition de verification
            os.remove(csv_file_path)  # Supprimer le fichier
            print(f"Le fichier '{file_name}' a été supprimé.")
        else:
            print(f"Le fichier '{file_name}' n'a pas été supprimé.")
    else:
        print("\n\033[91mLe fichier n'existe pas. Veuillez choisir un fichier existant à supprimer.\033[0m")
