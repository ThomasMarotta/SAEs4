from flask import Blueprint, jsonify, request
from bson import json_util

matches_joueur = Blueprint('joueurs', __name__)


def configure_matches_joueur(joueur_instance):
    @matches_joueur.route('/listeJoueurs', methods=['GET'])
    def get_joueur():
        joueurs_cursor = joueur_instance.afficher_joueurs()
        joueurs = [json_util.dumps(joueur) for joueur in joueurs_cursor]

        return jsonify(joueurs)

    @matches_joueur.route('/details&Pseudo=<string:pseudo>', methods=['GET'])
    def get_joueur_connu_par_un_pseudo(pseudo):
        joueur = joueur_instance.trouver_joueur_par_pseudo(pseudo)
        if joueur:
            return jsonify(json_util.dumps(joueur))
        else:
            return jsonify({"message": f"Aucun joueur trouvé avec le pseudo '{pseudo}'"}), 404

    @matches_joueur.route('/ajouterJoueur',methods=['POST'])
    def ajouter_joueur():
        resultat = joueur_instance.ajouter_joueur(request.form.get('pseudo'), request.form.get('nom'), request.form.get('prenom'), request.form.get('dateDeNaissance'), request.form.get('sexe'))
        return jsonify(resultat)

    @matches_joueur.route('/Supprimer&Pseudo=<string:pseudo>', methods=['GET'])
    def supprimer_leJoueur(pseudo):
        resultat = joueur_instance.supprimer_joueur_par_pseudo(pseudo)

        return jsonify(resultat)

    @matches_joueur.route('/modifierJoueur',methods=['POST'])
    def modifier_leJoueur():
        resultat =joueur_instance.modifier_nom_joueur_par_pseudo(request.form.get('pseudoAct'),request.form.get('pseudoNew'))

        return jsonify(resultat)


