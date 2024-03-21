from Joueur import Joueur
class MenuJoueur:
    def __init__(self, client_mongo):
        self.joueur = Joueur(client_mongo)

    def afficher_menu(self):
        print("Menu Joueur :")
        print("1. Afficher tous les joueurs")
        print("2. Trouver un joueur par pseudo")
        print("3. Ajouter un joueur")
        print("4. Supprimer un joueur par pseudo")
        print("5. Modifier le nom d'un joueur par pseudo")
        print("6. Quitter")

    def executer(self):
        while True:
            self.afficher_menu()
            choix = input("Entrez votre choix (1-6): ")

            if choix == "1":
                joueurs = self.joueur.afficher_joueurs()
                print("Liste des joueurs :")
                for joueur in joueurs:
                    print(joueur)
            elif choix == "2":
                pseudo = input("Entrez le pseudo du joueur : ")
                joueur = self.joueur.trouver_joueur_par_pseudo(pseudo)
                if joueur:
                    print("Joueur trouvé :")
                    print(joueur)
                else:
                    print(f"Aucun joueur trouvé avec le pseudo '{pseudo}'")
            elif choix == "3":
                pseudo = input("Entrez le pseudo du joueur : ")
                nom = input("Entrez le nom du joueur : ")
                prenom = input("Entrez le prénom du joueur : ")
                date_de_naissance = input("Entrez la date de naissance du joueur : ")
                sexe = input("Entrez le sexe du joueur : ")
                resultat, status_code = self.joueur.ajouter_joueur(pseudo, nom, prenom, date_de_naissance, sexe)
                print(resultat)
            elif choix == "4":
                pseudo = input("Entrez le pseudo du joueur à supprimer : ")
                resultat = self.joueur.supprimer_joueur_par_pseudo(pseudo)
                print(resultat)
            elif choix == "5":
                pseudo = input("Entrez le pseudo du joueur à modifier : ")
                nouveau_nom = input("Entrez le nouveau nom du joueur : ")
                resultat = self.joueur.modifier_nom_joueur_par_pseudo(pseudo, nouveau_nom)
                print(resultat)
            elif choix == "6":
                print("Merci d'avoir utilisé le menu Joueur ! Au revoir !")
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 6.")
