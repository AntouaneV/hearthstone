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
    mySql_select_query = """SELECT card_id, unit FROM collection WHERE user_id = %s """
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (player_id,))
    records = cursor.fetchall()
    return records