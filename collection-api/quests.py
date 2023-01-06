from dbConnect import connectDB
from quests_model import get_all_quests
from collections_model import isCardObtained
from cards_model import get_Card
import schedule
import time

class Quests:
    def __init__(self, quest_name, quest_amount, reward, reward_amount, card_id):
        self.quest_name = quest_name
        self.quest_amount = quest_amount
        self.reward = reward
        self.reward_amount = reward_amount
        self.card_id = card_id

    def is_reward_card(self):
        if self.reward == 6:
            return True
        else:
            return False

class User:
    def __init__(self,pseudo,nb_won,nb_played,nb_turns,xp,gold,arcane_dust):
        self.pseudo = pseudo
        self.nb_won = nb_won
        self.nb_played = nb_played
        self.nb_turns = nb_turns
        self.damage_dealt = 0
        self.spells_cast = 0
        self.xp = xp
        self.gold = gold
        self.arcane_dust = arcane_dust
        self.quests = []
        self.cards = []
    
    def add_quest(self, quest):
        self.quests.append(quest)
        return

user = User('Fanfrelin',0,2,11,300,100,2)

#Récupère toute les quêtes avec leur récompenses respectives
def get_all_quests_rewards() :
    db = connectDB()
    mySql_select_query = """SELECT `quests`.name AS name_quest, `quests`.unit AS quest_requirement, `quests`.description AS quest_description, `rewards`.item AS reward_item, `rewards`.unit AS nb_reward, `rewards`.card_id FROM `quests` LEFT JOIN `quest_rewards` ON `quests`.id = `quest_rewards`.quest_id LEFT JOIN `rewards` ON `quest_rewards`.reward_id = `rewards`.id"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query)
    records = cursor.fetchall()
    return records


#Fonction affectant 3 nouvelles quêtes pour un nouvel utilisateur

def affect_quests(user1):
    if len(user1.quests) == 0:
        for i in range(3):
            quest_tmp = Quests(get_all_quests_rewards()[i][0],get_all_quests_rewards()[i][1],get_all_quests_rewards()[i][3],get_all_quests_rewards()[i][4],None)
            user1.add_quest(quest_tmp)

def mission_complete(user1):
    if len(user1.quests) != 0 :
        for q in user1.quests:
            if q.quest_name == "Chicken Dinner":
                if user1.nb_won >= q.quest_amount:
                    user1.xp += 500
                    user1.quests.remove(q)
            if q.quest_name == 'Mount Up!':
                if user1.nb_won >= q.quest_amount:
                    user1.xp += 200
                    user1.quests.remove(q)
            if q.quest_name == "First Blood":
                if user1.nb_played >= q.quest_amount:
                    user1.xp += 100
                    user1.quests.remove(q)
            if q.quest_name == "Master Of All":
                if user1.nb_played >= q.quest_amount:
                    user1.gold += 200 
                    user1.quests.remove(q)
            if q.quest_name == "Take Turns":
                if user1.nb_turns >= q.quest_amount:
                    user1.gold += 200
                    user1.quests.remove(q)
            if q.quest_name == "Play spell":
                if user1.spells_cast >= q.quest_amount:
                    user1.cards.append(get_Card(q.card_id))
                    user1.quests.remove(q)
    return


print(user.quests)
affect_quests(user)

#Test pour verifier que mission_complete retire bien les quêtes appropriés après atteinte de l'objectif
print("avant nombre de quêtes: " + str(len(user.quests)) + ", gold : " + str(user.gold) + ", XP : " + str(user.xp))
user.nb_played = 10
user.nb_won = 10
mission_complete(user)
print("après nombre de quêtes: " + str(len(user.quests)) + ", gold : " + str(user.gold) + ", XP : " + str(user.xp))

#Il faudra modifier le code pour qu'il récupère ses users de la liste d'utilisateurs et les infos de jeu du rapport de partie