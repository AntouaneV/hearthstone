# Script d'ajout de deck 

import random 
import dbConnect

min = 0
max = 452 
user_id = 2
name = "IPSSI Deck"

liste = [user_id, name]


while len(liste) < 32: 
    number = random.randint(min, max)
    if number not in liste:
        liste.append(number)

liste = tuple(liste)
print(liste)

db = dbConnect.connectDB()
cursor = db.cursor()
sql = "INSERT INTO `deck`(`user_id`, `name`, `card_1`, `card_2`, `card_3`, `card_4`, `card_5`, `card_6`, `card_7`, `card_8`, `card_9`, `card_10`, `card_11`, `card_12`, `card_13`, `card_14`, `card_15`, `card_16`, `card_17`, `card_18`, `card_19`, `card_20`, `card_21`, `card_22`, `card_23`, `card_24`, `card_25`, `card_26`, `card_27`, `card_28`, `card_29`, `card_30`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
liste = tuple(liste)
cursor.execute(sql, liste)
db.commit()
db.close()