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

# Retourne les cartes selon leurs type
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

# Retourne toutes les cartes d'une classe pour un set précis (tests)
def get_SetClassCards(set_id, class_id) :
    db = connectDB()
    mySql_select_query = """SELECT id FROM cards WHERE cardSet = %s AND playerClass = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (set_id, class_id))
    records = cursor.fetchall()
    return records

# Retourne toutes les cartes données à l'ajout d'un joueur
def get_card_for_new() :
    db = connectDB()
    mySql_select_query = """SELECT id FROM cards WHERE rarity IS NULL OR type = 'Hero'"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query)
    records = cursor.fetchall()
    return records

# Retourne les données d'exemple
def get_example() :
    db = connectDB()
    mySql_select_query = """SELECT id FROM cards ORDER BY RAND() LIMIT 1"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query)
    records = cursor.fetchall()
    return records
