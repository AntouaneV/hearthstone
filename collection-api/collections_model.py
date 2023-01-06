from dbConnect import connectDB

#######################################################
# COLLECTIONS
# #####################################################
def get_Collection() :
    db = connectDB()
    mySql_select_query = """SELECT user_id, card_id, unit FROM collection"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query)
    records = cursor.fetchall()
    return records

# Retourne toutes les cartes possédées par le joueur
def get_playerCollection(player_id) :
    db = connectDB()
    mySql_select_query = """SELECT * FROM collection WHERE user_id = %s """
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (player_id,))
    records = cursor.fetchall()
    return records

# POST : Ajout d'une carte dans la collection d'un joueur
def add_CardToCollection(player_id, card_id, units) :
    db = connectDB()
    
    if isCardObtained(player_id, card_id):
        try:
            mySql_select_query = """UPDATE collection SET unit = unit + %s WHERE user_id = %s AND card_id = %s"""
            cursor = db.cursor()
            print("Carte déjà obtenue : Ajout d'exemplaires à une entrée existante")
            cursor.execute(mySql_select_query, (units, player_id, card_id))
            db.commit()
        except:
            print("An error has occured")
    else:
        try:
            print("Nouvelle carte : Ajout d'une entrée")
            mySql_select_query = """INSERT INTO collection VALUES ('%s', '%s', '%s')"""
            cursor = db.cursor()
            cursor.execute(mySql_select_query, (player_id, card_id, units))
            db.commit()
        except:
            print("An error has occured")
    

# Retourne True si le joueur possède déjà au moins 1 exemplaire de cette carte
def isCardObtained(player_id, card_id) :
    db2 = connectDB()
    mySql_select_query = """SELECT COUNT(*) FROM collection WHERE user_id = %s AND card_id = %s"""
    cursor = db2.cursor()
    cursor.execute(mySql_select_query, (player_id, card_id))
    records = cursor.fetchone()[0]
    print(records)
    if records == 0:
        return False
    else:
        return True

# POST : Suppression d'une carte dans la collection d'un joueur (disenchant)
def remove_CardFromCollection(player_id, card_id) :
    db = connectDB()
    try:
        mySql_select_query = """DELETE FROM collection WHERE user_id = %s AND card_id = %s"""
        cursor = db.cursor()
        print("Suppression d'une carte de la collection")
        cursor.execute(mySql_select_query, (player_id, card_id))
        db.commit()
    except:
        print("An error has occured")


# Ajouts des cartes lorsqu'il y a un nouveau joueur
def add_card(player_id, card_id) :
    db = connectDB()
    cursor = db.cursor()
    for card in card_id :
        mySql_select_query = """INSERT INTO collection(user_id, card_id) VALUES (%s, %s)"""
        record = (player_id, card[0])
        cursor.execute(mySql_select_query, record)
    records = db.commit()
    return records

# Retourne les données d'exemple
def get_example() :
    db = connectDB()
    mySql_select_query = """SELECT user_id FROM collection ORDER BY RAND() LIMIT 1"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query)
    records = cursor.fetchall()
    return records
