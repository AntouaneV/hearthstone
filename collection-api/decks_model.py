from dbConnect import connectDB

#######################################################
# DECKS
# #####################################################
# Retourne tous les decks d'un joueur
def get_decks(user_id):
    db = connectDB()
    mySql_select_query = """SELECT * FROM deck WHERE user_id = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (user_id,))
    records = cursor.fetchall()
    return records

# Retourne un deck d'un joueur
# (Le fait de demander l'user ID est pas obligatoire, mais c'est pour éviter de pouvoir
# récupérer le deck d'un autre joueur via des bugs ou trucs du genre)
def get_oneUserDeck(user_id, deck_id):
    db = connectDB()
    mySql_select_query = """SELECT * FROM deck WHERE user_id = %s AND id = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (user_id, deck_id))
    records = cursor.fetchall()
    return records

# Retourne les données d'exemple
def get_example() :
    db = connectDB()
    mySql_select_query = """SELECT id, user_id FROM deck ORDER BY RAND() LIMIT 1"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query)
    records = cursor.fetchall()
    return records


# POST : Ajout d'une carte dans la collection d'un joueur
def add_DeckToCollection(player_id, deck_name, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, card26, card27, card28, card29, card30) :
    db = connectDB()
    if isDeckNameTaken(player_id, deck_name):
        try:
            print("Ce nom de deck est déjà pris : Ajout d'un (copy) à la fin du nom.")
            mySql_select_query = """INSERT INTO deck (user_id, name, card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_11, card_12, card_13, card_14, card_15, card_16, card_17, card_18, card_19, card_20, card_21, card_22, card_23, card_24, card_25, card_26, card_27, card_28, card_29, card_30 ) VALUES ('%s', "%s(copy)", '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""
            # print(mySql_select_query)
            cursor = db.cursor()
            cursor.execute(mySql_select_query, (player_id, deck_name, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, card26, card27, card28, card29, card30))
            db.commit()
        except:
            print("An error has occured")
    else:
        try:
            print("Ajout d'un nouveau deck")
            mySql_select_query = """INSERT INTO deck (user_id, name, card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_11, card_12, card_13, card_14, card_15, card_16, card_17, card_18, card_19, card_20, card_21, card_22, card_23, card_24, card_25, card_26, card_27, card_28, card_29, card_30 ) VALUES ('%s', "%s", '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""
            # print(mySql_select_query, (deck_id, player_id, deck_name, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, card26, card27, card28, card29, card30))
            cursor = db.cursor()
            cursor.execute(mySql_select_query, (player_id, deck_name, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, card26, card27, card28, card29, card30))
            db.commit()
        except:
            print("An error has occured")

# Retourne True si le joueur possède déjà au moins 1 exemplaire de cette carte
def isDeckNameTaken(player_id, deck_name) :
    db2 = connectDB()
    mySql_select_query2 = """SELECT COUNT(*) FROM deck WHERE user_id = %s AND name = \"%s\""""
    cursor2 = db2.cursor()
    cursor2.execute(mySql_select_query2, (player_id, deck_name))
    records2 = cursor2.fetchone()[0]
    # print(records2)
    if records2 == 0:
        return False
    else:
        return True