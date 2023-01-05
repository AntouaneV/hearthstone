from dbConnect import connectDB

#######################################################
# CARDS
# #####################################################
# Retourne toutes les cartes
def get_all_cards():
    db = connectDB()
    mySql_select_query = """SELECT * FROM cards"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query)
    records = cursor.fetchall()
    return records

# Retourne une carte passée en entrée
def get_Card(card_id) :
    db = connectDB()
    mySql_select_query = """SELECT * FROM cards WHERE id = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (card_id,))
    records = cursor.fetchall()
    return records

def get_Card_Type(type_card) :
    db = connectDB()
    mySql_select_query = """SELECT * FROM cards WHERE type = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (type_card,))
    records = cursor.fetchall()
    return records

def get_mechanics(card_id) :
    db = connectDB()
    mySql_select_query = """SELECT mechanics FROM cards WHERE id = %s """
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (card_id,))
    records = cursor.fetchall()
    return records

