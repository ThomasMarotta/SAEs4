from Tournoi import Tournoi
class MenuTournoi:
    def __init__(self, client_mongo):
        self.tournoi_manager = Tournoi(client_mongo)

    def afficher_menu(self):
        print("Menu Tournoi :")
        print("1. Afficher tous les tournois")
        print("2. Trouver un tournoi par son nom")
        print("3. Ajouter un tournoi")
        print("4. Ajouter un match à un tournoi")
        print("5. Afficher les matchs d'un joueur")
        print("6. Supprimer un tournoi par le nom")
        print("7. Supprimer un match")
        print("8. Modifier le nom d'un tournoi")
        print("9. Modifier un participant d'un match")
        print("10. Quitter")

    def executer(self):
        while True:
            self.afficher_menu()
            choix = input("Entrez votre choix (1-9): ")

            if choix == "1":
               liste_tournoi =  self.tournoi_manager.afficher_tournois()
               for tournoi in liste_tournoi:
                   print(tournoi)

            elif choix == "2":
                nom_tournoi = input("Entrez le nom du tournoi : ")
                tournoi = self.tournoi_manager.trouver_tournoi_par_nom(nom_tournoi)
                print(tournoi)
            elif choix == "3":
                nom_tournoi = input("Entrez le nom du tournoi : ")
                if self.tournoi_manager.trouver_tournoi_par_nom(nom_tournoi):
                    print("Un tournoi avec ce nom existe déjà.")
                else:
                    participants = input("Entrez la liste des participants (séparés par des virgules) : ")
                    resultat, status_code = self.tournoi_manager.ajouter_tournoi(nom_tournoi, participants)
                    print(resultat)
            elif choix == "4":
                nom_tournoi = input("Entrez le nom du tournoi : ")
                id_match = input("Entrez l'ID du match : ")
                joueur1 = input("Entrez le nom du joueur 1 : ")
                joueur2 = input("Entrez le nom du joueur 2 : ")
                score_joueur1 = int(input(f"Entrez le score de {joueur1} : "))
                score_joueur2 = int(input(f"Entrez le score de {joueur2} : "))
                temps_de_partie = input("Entrez le temps de partie : ")

                resultat = self.tournoi_manager.ajouter_match(self, nom_tournoi, id_match, joueur1, joueur2, score_joueur1, score_joueur2, temps_de_partie)
                print(resultat)
            elif choix == "5":
                pseudo = input("Entrez le pseudo du joueur : ")
                matchs = self.tournoi_manager.afficher_match_par_pseudo(pseudo)
                for match in matchs:
                    print(match)
            elif choix == "6":
                nom_tournoi = input("Entrez le nom du tournoi à supprimer : ")
                resultat = self.tournoi_manager.supprimer_tournoi_par_id(nom_tournoi)
                print(resultat)
            elif choix == "7":
                nom_tournoi = input("Entrez le nom du tournoi : ")
                id_match = input("Entrez l'ID du match à supprimer : ")
                resultat = self.tournoi_manager.supprimer_match(nom_tournoi, id_match)
                print(resultat)
            elif choix == "8":
                nom_tournoi = input("Entrez le nom du tournoi : ")
                nouveau_nom = input("Entrez le nouveau nom du tournoi : ")
                resultat = self.tournoi_manager.modifier_nom_tournoi(nom_tournoi, nouveau_nom)
                print(resultat)
            elif choix == "9":
                nom_tournoi = input("Entrez le nom du tournoi : ")
                id_match = input("Entrez l'ID du match : ")
                pseudo_a_changer = input("Entrez le pseudo du participant à changer : ")
                nouveau_participant = input("Entrez le nouveau participant : ")
                resultat = self.tournoi_manager.modifier_participant_match(nom_tournoi, id_match, pseudo_a_changer,
                                                                           nouveau_participant)
                print(resultat)
            elif choix == "10":
                print("Merci d'avoir utilisé le menu Tournoi ! Au revoir !")
                break
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 9.")
