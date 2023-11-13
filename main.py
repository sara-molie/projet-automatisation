from menu import *
from create import *
from verif2 import *

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
        modifier2()
    elif option == "3":
        supprimer()
    elif option == "4":
        verif()
    elif option == "5":
        improve()
    elif option == "6":
        print("Goodbye !")
        exit()
    else:
        print("Choix invalide. Choisir une option valide (1-6).")
    
    
if __name__ == "__main__":
    menu()