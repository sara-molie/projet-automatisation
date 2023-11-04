from create import *
from verif import *

#menu central
def menu():
    for i in range (10):
        print("\n")  
    print("----------------------------")
    print("Select an option :")
    print("1. Créer un automate")
    print("2. Modifier un AEF")
    print("3. Supprimer un  AEF")
    print("4. Verification")
    print("5. Ameliorer l'AEF")
    print("6. Exit")
    print("----------------------------")

    option = input("Faire votre choix>> ")
    if option == "1":
        create()
    elif option == "2":
        modifier()
    elif option == "3":
        supprimer()
    elif option == "4":
        verif()
    elif option == "5":
        improve()
    elif option == "6":
        print("Goodbye !")
        exit
    else:
        print("Choix invalide. Choisir une option valide (1-6).")

# menu pour acceder a toutes les verifications
def verif():
    for i in range (10):
        print("\n")
        
    print("#######################")
    print("Select an option de vérification :")
    print("1. Si un mot est reconnu")
    print("2. Si un automate est complet")
    print("3. Si un automate est deterministe")
    print("4. Si tous les cycles sont unitaires")
    print("5. L'equivalence entre 2 automates")
    print("6. Retour")
    print("########################")

    option = input("Faire votre choix>> ")
    if option == "1":
        mot(automate, mot)
    elif option == "2":
        complet(csv_file_path)
    elif option == "3":
        deterministe()
    elif option == "4":
        unitaire()
    elif option == "5":
        equivalence()
    elif option == "6":
        menu()
        exit
    else:
        print("Choix invalide. Choisir une option valide (1-6).")

#menu pour acceder aux améliorations possibles
def improve():

    for i in range (10):
        print("\n")

    print("|||||||||||||||||||||||||||")
    print("Select an option pour améliorer l'AEF :")
    print("1. Rendre un automate complet")
    print("2. Rendre un automate deterministe")
    print("3. Rendre un automate émondé")
    print("4. Rendre un automate minimal")
    print("5. Retour")
    print("|||||||||||||||||||||||||||")

    option = input("Faire botre choix>> ")
    if option == "1":
        AEF_complet()
    elif option == "2":
        AEF_deterministe()
    elif option == "3":
        emonde()
    elif option == "4":
        minimal()
    elif option == "5":
        menu()
    else:
        print("Choix invalide. Choisir une option valide (1-5).")


