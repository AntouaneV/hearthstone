from dbConnect import connectDB
    
    
def InsertUser():
    db = connectDB()
    mySql_select_query = """SELECT * FROM users"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query)
    records = cursor.fetchall()
    return records    


