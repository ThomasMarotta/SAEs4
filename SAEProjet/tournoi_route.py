from flask import Blueprint, jsonify, request
from bson import json_util

matches_tournoi = Blueprint('tournoi', __name__)

def configure_matches_tournoi(tournoi_instance):
    @matches_tournoi.route('/listeTournois', methods=['GET'])
    def get_joueur():
        tournoi_cursor = tournoi_instance.afficher_tournois()
        tournoi = [json_util.dumps(tournoi) for tournoi in tournoi_cursor]

        return jsonify(tournoi)

    @matches_tournoi.route('/details&nom=<string:nom>', methods=['GET'])
    def get_joueur_connu_par_un_pseudo(nom):
        #Fonctionne mais a modifier par la suite
        tournoi = tournoi_instance.trouver_tournoi_par_nom(nom)
        if tournoi:
            return jsonify(json_util.dumps(tournoi))
        else:
            return jsonify({"message": f"Aucun tournoi trouvé avec le nom '{nom}'"}), 404


    @matches_tournoi.route('/ajouterTournoi', methods=['POST'])
    def ajout_tournoi():
        resultat = tournoi_instance.ajouter_tournoi(request.form.get('nom_tournoi'), request.form.get('participants'))
        return jsonify(resultat)

    @matches_tournoi.route('/ajouterMatch',methods=['POST'])
    def ajout_match():
        resultat = tournoi_instance.ajouter_match(request.form.get('nom_tournoi'), request.form.get('id_match'), request.form.get('joueur1'), request.form.get('joueur2'),request.form.get('score_joueur1'),request.form.get('score_joueur2') , request.form.get('temps_de_partie'))
        return jsonify(resultat)

    @matches_tournoi.route('/afficherMatchParPseudo&pseudo=<string:pseudo>', methods=['GET'])
    def affiche_match_par_pseudo(pseudo) :
        match = tournoi_instance.afficher_match_par_pseudo(pseudo)
        return jsonify(match)

    @matches_tournoi.route('/supprimerTournoi&idTournoi=<string:id>', methods=['GET'])
    def supprime_tournoi(id):
        resultat = tournoi_instance.supprimer_tournoi_par_id(id)
        return jsonify(resultat)

    @matches_tournoi.route('/supprimerMatch&nom_tournoi=<string:nom>&id_match=<string:id>', methods=['GET'])
    def supprime_match(nom, id):
        resultat = tournoi_instance.supprimer_match(nom, id)
        return jsonify(resultat)

    @matches_tournoi.route('/modifierNomTournoi', methods=['POST'])
    def modifie_nom_tournoi():
        resultat = tournoi_instance.modifier_nom_tournoi(request.form.get('nomAct'), request.form.get('nomNew'))

        return jsonify(resultat)
