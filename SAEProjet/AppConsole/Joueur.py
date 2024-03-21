class Joueur:
    def __init__(self, client_mongo):
        self.client_mongo = client_mongo
        self.joueurs_collection = client_mongo.get_joueurs_collection()

    def afficher_joueurs(self):
        joueurs = list(self.joueurs_collection.find())
        return joueurs

    def trouver_joueur_par_pseudo(self, pseudo):
        joueur = self.joueurs_collection.find_one({"Pseudo": pseudo})
        return joueur

    def ajouter_joueur(self, pseudo, nom, prenom, date_de_naissance, sexe):
        if not (pseudo and nom and prenom and date_de_naissance and sexe):
            return {"message": "Veuillez fournir toutes les données du joueur"}, 400

        if self.joueurs_collection.count_documents({"Pseudo": pseudo}) > 0:
            return {"message": "Un joueur avec ce pseudo existe déjà"}, 409

        joueur = {
            "Pseudo": pseudo,
            "nom": nom,
            "prenom": prenom,
            "dateDeNaissance": date_de_naissance,
            "sexe": sexe
        }

        resultat = self.joueurs_collection.insert_one(joueur)

        if resultat.inserted_id:
            return {"message": "Joueur ajouté avec succès", "id": str(resultat.inserted_id)}, 201
        else:
            return {"message": "Erreur lors de l'ajout du joueur"}, 500

    def supprimer_joueur_par_pseudo(self, pseudo):
        deleted = self.joueurs_collection.delete_one({"Pseudo": pseudo})

        if deleted.deleted_count > 0:
            return {"message": "Document supprimé avec succès"}, 201
        else:
            return {"message": "Aucun document n'a été supprimé"}, 500

    def modifier_nom_joueur_par_pseudo(self, pseudo, nouveau_nom):
        if not (pseudo and nouveau_nom):
            return {"message": "Veuillez fournir toutes les données pour cette operation"}, 400

        if self.joueurs_collection.count_documents({"Pseudo": nouveau_nom}) > 0:
            return {"message": "Un joueur avec ce pseudo existe déjà"}, 409

        result = self.joueurs_collection.update_one(
            {"Pseudo": pseudo},
            {"$set": {"Pseudo": nouveau_nom}}
        )

        if result.modified_count > 0:
            return {"message": "Joueur modifié avec succès"}
        else:
            return {"message": "Aucun joueur n'a été modifié"}
