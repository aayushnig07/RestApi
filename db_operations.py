import sqlite3

db=sqlite3.connect('books.db',check_same_thread=False)
cur=db.cursor()
def createTable():
    try:    
                   
        cur.execute('''CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author TEXT (20) NOT NULL,
        first_sentence TEXT (50) NOT NULL,
        title TEXT (20) NOT NULL,
        year_published int NOT NULL);''')
        print ('table created successfully')
    except Exception as e:
        print ('error in operation' + str(e))
        db.rollback()

def insertRecord(author,first_sentence,title,year_published):
    try:
                    
        qry = "insert into books (author,first_sentence,title,year_published) values(?,?,?,?);"
        cur.execute(qry,(author,first_sentence,title,year_published))
        db.commit()
        print('one record added successfully')
    except Exception as e:
        print('error in updation',e)  
    
def showAllData():
    sql="SELECT * from books;"
    cur.execute(sql)
    while True:
        record=cur.fetchone()
        if record==None:
            break
    print(record)
    return record

def showOneData(id):
    sql="SELECT * from books where id="+id+";"
    cur.execute(sql)
    while True:
        record=cur.fetchone()
        if record==None:
            break
    print(record)
    return record


