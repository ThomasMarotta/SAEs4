from Client2Mongo import ClientMongo
from MenuJoueur import MenuJoueur
from MenuTournoi import MenuTournoi
class Environnement:
    def __init__(self):
        self.client_mongo = ClientMongo()
        self.client_mongo.connect()

    def menu(self):
        print("Que souhaitez-vous faire ?")
        print("1. Accéder aux tournois")
        print("2. Accéder aux joueurs")
        print("3. Quitter")

    def executer(self):
        joueur_instance = MenuJoueur(self.client_mongo)
        tournoi_instance = MenuTournoi(self.client_mongo)
        while True:
            self.menu()
            choix = input("Entrez votre choix (1/2/3): ")

            if choix == "1":
                tournoi_instance.executer()
            elif choix == "2":
                joueur_instance.executer()
            elif choix == "3":
                print("Merci d'avoir utilisé l'environnement TennisMania ! Au revoir !")
                self.client_mongo.close_connection()
                break
            else:
                print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
