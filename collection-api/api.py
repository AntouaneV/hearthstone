# Import libraries
import numpy as np
from flask import Flask, jsonify, request
import quests_model as quests
import cards_model as cards
import collections_model as collections
import decks_model as decks


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    quest = quests.get_example()
    for data in quest :
        quest_id = data[0]

    card = cards.get_example()
    for data in card :
        card_id = data[0]

    collection = collections.get_example()
    for data in collection :
        user_id = data[0]

    deck = decks.get_example()
    for data in deck :
        deck_id = data[0]
        deck_user_id = data[1]

    return """<h2>Liste des requêtes API :</h2>
    <h5>Quêtes :</h5>
    <a href="/quests"><b>/quests</b></a> pour avoir toute la liste des quêtes.<br>
    <b>/quests/{quest_id}</b> pour avoir une quête précise. <a href="/quests/""" + str(quest_id) + """">Exemple</a>
    <h5>Cartes :</h5>
    <a href="/cards"><b>/cards</b></a> pour avoir toute la liste des cartes.<br>
    <b>/cards/type/{card_type}</b> pour avoir toute la liste des cartes selon le type. Exemple : <a href="/cards/type/enchantment">Enchantment</a>, <a href="/cards/type/spell">Spell</a>, <a href="/cards/type/hero">Hero</a>, <a href="/cards/type/minion">Minion</a>, <a href="/cards/type/weapon">Weapon</a>, <a href="/cards/type/hero power">Hero Power</a><br>
    <b>/cards/{card_id}</b> pour avoir une carte précise. <a href="/cards/""" + str(card_id) + """">Exemple</a>
    <h5>Collection :</h5>
    <a href="/collection"><b>/collection</b></a> pour avoir toute la liste des collections.<br>
    <b>/usercollection/{user_id}</b> pour avoir la collection complètre d'un joueur. <a href="/usercollection/""" + str(user_id) + """">Exemple</a><br>
    <b>/usercollection/add</b> pour ajouter des cartes à la collection. Il faut envoyer un fichier .json.<br>
    <b>/new_player/{user_id}</b> lors d'un nouveau joueur, on ajoute les cartes de début.
    <h5>Deck :</h5>
    <b>/userdecks/{user_id}</b> pour récupérer tous les decks d'un joueur. <a href="/userdecks/""" + str(deck_user_id) + """">Exemple</a><br>
    <b>/userdecks/{user_id}/{deck_id}</b> pour récupérer un deck en particulier pour un joueur. <a href="/userdecks/""" + str(deck_user_id) + """/""" + str(deck_id) + """">Exemple</a>"""


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

# Récupération de toutes les cartes existantes d'une classe provenant d'un set donné (testing)
@app.route('/cards/<set_id>/<class_id>', methods=['GET'])
def ClassCardsFromSet(set_id, class_id):
    return cards.get_SetClassCards(set_id, class_id)


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
    response_json = []
    data = collections.get_playerCollection(player_id)
    for card in data:
        respons = {
            'user_id': card[0],
            'card_id': card[1],
            'unit': card[2]
        }
        response_json.append(respons)
    return response_json


# POST : Ajout d'une carte à la collection d'un joueur
@app.route('/usercollection/add', methods=['POST'])
def add_cardToCollection():
    request_data = request.get_json()

    userdata = None
    carddata = None
    unitdata = None

    if request_data:
        if 'user_id' in request_data:
            userdata = request_data['user_id']

        if 'card_id' in request_data:
            carddata = request_data['card_id']

        if 'unit' in request_data:
            unitdata = request_data['unit']

    collections.add_CardToCollection(userdata, carddata, unitdata)

    return '''
           User: {}
           Card: {}
           Unit: {}'''.format(userdata, carddata, unitdata)


#POST : SUPPRESSION d'une carte de l'inventaire du joueur
@app.route('/usercollection/remove', methods=['POST'])
def remove_cardToCollection():
    request_data = request.get_json()
    userdata = None
    carddata = None

    if request_data:
        if 'user_id' in request_data:
            userdata = request_data['user_id']

        if 'card_id' in request_data:
            carddata = request_data['card_id']

    collections.remove_CardFromCollection(userdata, carddata)

    return '''
           User: {}
           Card: {}'''.format(userdata, carddata)


# Ajout de toutes les cartes offertes lors d'un nouveau joueur
@app.route('/new_player/<player_id>', methods=['GET'])
def new_player(player_id) :
    free_card = cards.get_card_for_new()
    collections.add_card(player_id, free_card)

    return 'Ajout effectué'

#######################################################
# DECKS
# ##################################################### 
# Récupération de tous les decks de l'utilisateur donné
@app.route('/userdecks/<player_id>', methods=['GET'])
def userDecks(player_id):
    deck_data = decks.get_decks(player_id)
    response_json = []
    for data in deck_data :
        response = {
            'id': data[0],
            'name': data[2],
            'card_1': collectionCard(data[3]),
            'card_2': collectionCard(data[4]),
            'card_3': collectionCard(data[5]),
            'card_4': collectionCard(data[6]),
            'card_5': collectionCard(data[7]),
            'card_6': collectionCard(data[8]),
            'card_7': collectionCard(data[9]),
            'card_8': collectionCard(data[10]),
            'card_9': collectionCard(data[11]),
            'card_10': collectionCard(data[12]),
            'card_11': collectionCard(data[13]),
            'card_12': collectionCard(data[14]),
            'card_13': collectionCard(data[15]),
            'card_14': collectionCard(data[16]),
            'card_15': collectionCard(data[17]),
            'card_16': collectionCard(data[18]),
            'card_17': collectionCard(data[19]),
            'card_18': collectionCard(data[20]),
            'card_19': collectionCard(data[21]),
            'card_20': collectionCard(data[22]),
            'card_21': collectionCard(data[23]),
            'card_22': collectionCard(data[24]),
            'card_23': collectionCard(data[25]),
            'card_24': collectionCard(data[26]),
            'card_25': collectionCard(data[27]),
            'card_26': collectionCard(data[28]),
            'card_27': collectionCard(data[29]),
            'card_28': collectionCard(data[30]),
            'card_29': collectionCard(data[31]),
            'card_30': collectionCard(data[32])
        }
        response_json.append(response)

    return response_json

# Récupération d'un deck précis de l'utilisateur donné
@app.route('/userdecks/<player_id>/<deck_id>', methods=['GET'])
def userDeck(player_id, deck_id):
    deck_data = decks.get_oneUserDeck(player_id, deck_id)
    response_json = []
    for data in deck_data :
        response = {
            'id': data[0],
            'name': data[2],
            'card_1': collectionCard(data[3]),
            'card_2': collectionCard(data[4]),
            'card_3': collectionCard(data[5]),
            'card_4': collectionCard(data[6]),
            'card_5': collectionCard(data[7]),
            'card_6': collectionCard(data[8]),
            'card_7': collectionCard(data[9]),
            'card_8': collectionCard(data[10]),
            'card_9': collectionCard(data[11]),
            'card_10': collectionCard(data[12]),
            'card_11': collectionCard(data[13]),
            'card_12': collectionCard(data[14]),
            'card_13': collectionCard(data[15]),
            'card_14': collectionCard(data[16]),
            'card_15': collectionCard(data[17]),
            'card_16': collectionCard(data[18]),
            'card_17': collectionCard(data[19]),
            'card_18': collectionCard(data[20]),
            'card_19': collectionCard(data[21]),
            'card_20': collectionCard(data[22]),
            'card_21': collectionCard(data[23]),
            'card_22': collectionCard(data[24]),
            'card_23': collectionCard(data[25]),
            'card_24': collectionCard(data[26]),
            'card_25': collectionCard(data[27]),
            'card_26': collectionCard(data[28]),
            'card_27': collectionCard(data[29]),
            'card_28': collectionCard(data[30]),
            'card_29': collectionCard(data[31]),
            'card_30': collectionCard(data[32])
        }
        response_json.append(response)

    return response_json

# POST : Ajout d'un deck à la collection d'un joueur
@app.route('/userdecks/add', methods=['POST'])
def add_DeckToCollection():
    request_data = request.get_json()

    userdata = None
    deckIDdata = None
    deckNamedata = None
    card1data = None
    card2data = None
    card3data = None
    card4data = None
    card5data = None
    card6data = None
    card7data = None
    card8data = None
    card9data = None
    card10data = None
    card11data = None
    card12data = None
    card13data = None
    card14data = None
    card15data = None
    card16data = None
    card17data = None
    card18data = None
    card19data = None
    card20data = None
    card21data = None
    card22data = None
    card23data = None
    card24data = None
    card25data = None
    card26data = None
    card27data = None
    card28data = None
    card29data = None
    card30data = None

    if request_data:
        if 'user_id' in request_data:
            userdata = request_data['user_id']

        if 'id' in request_data:
            deckIDdata = request_data['id']

        if 'name' in request_data:
            deckNamedata = request_data['name']

        if 'card_1' in request_data:
            card1data = request_data['card_1']

        if 'card_2' in request_data:
            card2data = request_data['card_2']            

        if 'card_3' in request_data:
            card3data = request_data['card_3']        
 
        if 'card_4' in request_data:
            card4data = request_data['card_4']        

        if 'card_5' in request_data:
            card5data = request_data['card_5']        
 
        if 'card_6' in request_data:
            card6data = request_data['card_6']        

        if 'card_7' in request_data:
            card7data = request_data['card_7']        

        if 'card_8' in request_data:
            card8data = request_data['card_8']   

        if 'card_9' in request_data:
            card9data = request_data['card_9']        

        if 'card_10' in request_data:
            card10data = request_data['card_10']        

        if 'card_11' in request_data:
            card11data = request_data['card_11']        

        if 'card_12' in request_data:
            card12data = request_data['card_12']        

        if 'card_13' in request_data:
            card13data = request_data['card_13']        

        if 'card_14' in request_data:
            card14data = request_data['card_14']        

        if 'card_15' in request_data:
            card15data = request_data['card_15']        

        if 'card_16' in request_data:
            card16data = request_data['card_16']        

        if 'card_17' in request_data:
            card17data = request_data['card_17']        

        if 'card_18' in request_data:
            card18data = request_data['card_18']        

        if 'card_19' in request_data:
            card19data = request_data['card_19']        

        if 'card_20' in request_data:
            card20data = request_data['card_20']        

        if 'card_21' in request_data:
            card21data = request_data['card_21']        

        if 'card_22' in request_data:
            card22data = request_data['card_22']        

        if 'card_23' in request_data:
            card23data = request_data['card_23']        

        if 'card_24' in request_data:
            card24data = request_data['card_24']        

        if 'card_25' in request_data:
            card25data = request_data['card_25']        

        if 'card_26' in request_data:
            card26data = request_data['card_26']        

        if 'card_27' in request_data:
            card27data = request_data['card_27']        

        if 'card_28' in request_data:
            card28data = request_data['card_28']        

        if 'card_29' in request_data:
            card29data = request_data['card_29']        

        if 'card_30' in request_data:
            card30data = request_data['card_30']        
 
    decks.add_DeckToCollection(userdata, deckNamedata, card1data, card2data, card3data, card4data, card5data, card6data, card7data, card8data, card9data, card10data, card11data, card12data, card13data, card14data, card15data, card16data, card17data, card18data, card19data, card20data, card21data, card22data, card23data, card24data, card25data, card26data, card27data, card28data, card29data, card30data)

    return '''
           User: {}
           Deck ID: {}
           Deck Name: {}
           Cards : {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'''.format(userdata, deckIDdata, deckNamedata, card1data, card2data, card3data, card4data, card5data, card6data, card7data, card8data, card9data, card10data, card11data, card12data, card13data, card14data, card15data, card16data, card17data, card18data, card19data, card20data, card21data, card22data, card23data, card24data, card25data, card26data, card27data, card28data, card29data, card30data)


#######################################################
# REWARDS
# ##################################################### 
if __name__ == '__main__':
    try:
        app.run(port=5000, debug=True)
    except:
        print("Server error")
