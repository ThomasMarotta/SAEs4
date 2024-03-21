from bson.objectid import ObjectId
class Tournoi:
    def __init__(self, client_mongo):
        self.client_mongo = client_mongo
        self.tournois_collection = self.client_mongo.get_tournoi_collection()

    def afficher_tournois(self):
        tournois = list(self.tournois_collection.find())
        return tournois
    def trouver_tournoi_par_nom(self, nom):
        tournoi = self.tournois_collection.find_one({"nom": nom})
        return tournoi

    def ajouter_tournoi(self, nom_tournoi, participants):
        if self.tournois_collection.count_documents({"nom": nom_tournoi}) > 0:
            return {"message": "Un tournoi avec ce nom existe déjà"}, 409

        participants.split(',')
        tournoi = {
            "nom": nom_tournoi,
            "participants": participants,
            "matchs": []
        }

        resultat = self.tournois_collection.insert_one(tournoi)

        if resultat.inserted_id:
            return {"message": "Tournoi ajouté avec succès", "id": str(resultat.inserted_id)}, 201
        else:
            return {"message": "Erreur lors de l'ajout du tournoi"}, 500

    def ajouter_match(self, nom_tournoi, id_match, joueur1, joueur2, score_joueur1, score_joueur2, temps_de_partie):
        match = {
            "_id": id_match,
            "joueur1": joueur1,
            "joueur2": joueur2,
            "scoreJ1": score_joueur1,
            "scoreJ2": score_joueur2,
            "tempsDePartie": temps_de_partie
        }
        tournoi = self.tournois_collection.find_one({"nom": nom_tournoi})
        if not tournoi:
            return {"message": "Aucun tournoi trouvé avec ce nom"}

        participants = tournoi.get("participants", [])
        joueurs = [match["joueur1"], match["joueur2"]]

        for joueur in joueurs:
            if joueur not in participants:
                return {"message": f"Le joueur '{joueur}' n'est pas inscrit dans ce tournoi"}

        result = self.tournois_collection.update_one(
            {"nom": nom_tournoi},
            {"$push": {"matchs": match}}
        )

        if result.modified_count > 0:
            return {"message": "Match ajouté avec succès"}
        else:
            return {"message": "Aucun tournoi modifié"}

    def afficher_match_par_pseudo(self, pseudo):
        matchs = list(self.tournois_collection.find({
            "matchs": {
                "$elemMatch": {
                    "$or": [{"joueur1": pseudo}, {"joueur2": pseudo}]
                }
            }
        }))

        matchs_impliquant_pseudo = []
        for tournoi in matchs:
            for match in tournoi['matchs']:
                if 'joueur1' in match and 'joueur2' in match:
                    if match['joueur1'] == pseudo or match['joueur2'] == pseudo:
                        matchs_impliquant_pseudo.append(match)

        return matchs_impliquant_pseudo

    def supprimer_tournoi_par_id(self, nom):
        result = self.tournois_collection.delete_one({"nom": nom})
        if result.deleted_count > 0:
            return {"message": "Tournoi supprimé avec succès"}
        else:
            return {"message": "Aucun tournoi supprimé"}

    def supprimer_match(self, nom, match_id):
        result = self.tournois_collection.update_one(
            {"nom": nom},
            {"$pull": {"matchs": {"_id": match_id}}}
        )
        if result.modified_count > 0:
            return {"message": "Match supprimé avec succès"}
        else:
            return {"message": "Aucun match supprimé"}

    def modifier_nom_tournoi(self, nom, nouveau_nom):
        result = self.tournois_collection.update_one(
            {"nom":nom},
            {"$set": {"nom": nouveau_nom}}
        )
        if result.modified_count > 0:
            return {"message": "Nom du tournoi modifié avec succès"}
        else:
            return {"message": "Aucun tournoi modifié"}

