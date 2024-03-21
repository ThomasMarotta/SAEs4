from flask import Flask
from flask_cors import CORS
from joueur_route import configure_matches_joueur, matches_joueur
from tournoi_route import configure_matches_tournoi, matches_tournoi
from Client2Mongo import ClientMongo
from AppConsole.Joueur import Joueur
from AppConsole.Tournoi import Tournoi

app = Flask(__name__)
cors = CORS(app)

client_mongo = ClientMongo()
client_mongo.connect()

joueur_instance = Joueur(client_mongo)
tournoi_instance = Tournoi(client_mongo)
configure_matches_joueur(joueur_instance)
configure_matches_tournoi(tournoi_instance)

app.register_blueprint(matches_tournoi, url_prefix='/tournoi')
app.register_blueprint(matches_joueur, url_prefix='/joueurs')


@app.route('/')
def hello_world():
    return 'hello World'


if __name__ == '__main__':
    app.run(debug=True)
