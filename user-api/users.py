from dbConnect import connectDB
    
    
def InsertUser():
    db = connectDB()
    mySql_select_query = """SELECT * FROM users"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query)
    records = cursor.fetchall()
    return records    


def FindUser(user_id) :
    db = connectDB()
    mySql_select_query = """SELECT * FROM users WHERE id = %s"""
    cursor = db.cursor()
    cursor.execute(mySql_select_query, (user_id,))
    records = cursor.fetchall()
    return records   

def create_user(username, password, email):
    db = connectDB()
    insert_query = "INSERT INTO users (username, password,email) VALUES (%s, %s, %s)"
    cursor = db.cursor()
    cursor.execute(insert_query, (username, password, email))
    db.commit()
    cursor.close()
