from dbConnect import connectDB

#######################################################
# QUESTS
# ##################################################### 
# retourne toutes les quêtes
def get_all_quests() :
    db = connectDB()
    mySql_select_query = """SELECT * FROM quests"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query)
    records = cursor.fetchall()
    return records

# Retourne une quête passée en entrée
def get_quest(quest_id) :
    db = connectDB()
    mySql_select_query = """SELECT * FROM quests WHERE id = %s """
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (quest_id,))
    records = cursor.fetchall()
    return records

# Retourne l'id d'une quête random pour l'exemple
def get_example() :
    db = connectDB()
    mySql_select_query = """SELECT id FROM quests ORDER BY RAND() LIMIT 1"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query)
    records = cursor.fetchall()
    return records
