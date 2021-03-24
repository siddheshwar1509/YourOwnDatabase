import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (Id INTEGER PRIMARY KEY , name text , date integer , email text , age integer , birthdate integer ,location text)")
    conn.commit()
    conn.close()

def insert(name , date , email , age , birthdate , location):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ?,?,?,?,?,?)" , (name , date , email , age , birthdate , location))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=? ", (id,))
    conn.commit()
    conn.close()

def search(name='' , date='' , email='' , age='' , birthdate='' , location=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE name=?  OR date=? OR email=? OR age=? OR birthdate=? OR location=?" , (name , date , email , age , birthdate , location))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
