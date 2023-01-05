# Import libraries
from flask import Flask, jsonify, request
import quests_model as quests
import cards_model as cards
import collections_model as collections
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return 'Hearthstone Server'

#######################################################
# QUESTS
# ##################################################### 
# retourne toutes les quêtes
@app.route('/quests', methods=['GET'])
def getAllQuest():
    response_json = []
    data = quests.get_all_quests()
    for quest in data:
        respons = {
            'id': quest[0],
            'name': quest[1],
            'unit': quest[2],
            'description': quest[3]
        }
        response_json.append(respons)
    return response_json

@app.route('/quests/<quest_id>', methods=['GET'])
def getQuest(quest_id):
    response_json = []
    data = quests.get_quest(quest_id)
    for quest in data:
        respons = {
            'id': quest[0],
            'name': quest[1],
            'unit': quest[2],
            'description': quest[3]
        }
        response_json.append(respons)
    return response_json
#######################################################
# CARDS
# ##################################################### 
# Récupération de toutes les cartes existantes
@app.route('/cards', methods=['GET'])
def getCards():
    data = cards.get_all_cards()
    response_json = []
    for card in data:
        respons = {
            'id': card[0],
            'name': card[1],
            'cardSet,': card[2],
            'type': card[3],
            'text': card[4],
            'playerClass': card[5],
            'mechanics': card[6].decode("utf-8"),
            'rarity': card[7],
            'cost': card[8],
            'attack': card[9],
            'health': card[10],
            'img': card[11],
            'durability': card[12],
            'imgGold': card[13],
            'armor': card[14],
        }
        response_json.append(respons)
    return response_json

# Récupération des cartes selon le type
@app.route('/cards/type/<type_card>', methods=['GET'])
def getCardByType(type_card) :
    response_json = []
    data = cards.get_Card_Type(type_card)
    for card in data :
        response = {
            'id': card[0],
            'name': card[1],
            'cardSet,': card[2],
            'type': card[3],
            'text': card[4],
            'playerClass': card[5],
            'mechanics': card[6].decode("utf-8"),
            'rarity': card[7],
            'cost': card[8],
            'attack': card[9],
            'health': card[10],
            'img': card[11],
            'durability': card[12],
            'imgGold': card[13],
            'armor': card[14],
        }
        response_json.append(response)
    return response_json

# Récupération d'une carte spécifique selon l'ID
@app.route('/cards/<card_id>', methods=['GET'])
def collectionCard(card_id):
    response_json = []
    data = cards.get_Card(card_id)
    for card in data:
        respons = {
            'id': card[0],
            'name': card[1],
            'cardSet,': card[2],
            'type': card[3],
            'text': card[4],
            'playerClass': card[5],
            'mechanics': card[6].decode("utf-8"),
            'rarity': card[7],
            'cost': card[8],
            'attack': card[9],
            'health': card[10],
            'img': card[11],
            'durability': card[12],
            'imgGold': card[13],
            'armor': card[14],
        }
        response_json.append(respons)
    return response_json

#######################################################
# COLLECTIONS
# ##################################################### 
# Récupération de toutes les cartes existantes
@app.route('/collection', methods=['GET'])
def Collection():
    return collections.get_Collection()

# Récupération de l'ID de toutes les cartes possédés par le joueur donné
@app.route('/usercollection/<player_id>', methods=['GET'])
def userCollection(player_id):
    return collections.get_playerCollection(player_id)

#######################################################
# REWARDS
# ##################################################### 

if __name__ == '__main__':
    try:
        app.run(port=5000, debug=True)
    except:
        print("Server error")
