import sqlite3

def connect():
     conn = sqlite3.connect("AAACNL.db")
     cur = conn.cursor()
     cur.execute("CREATE TABLE IF NOT EXISTs AAACNL (id INTEGER PRIMARY KEY, name TEXT, address TEXT, phone_number INTEGER, gender TEXT)")
     conn.commit()
     conn.close
     
def insert(name, address, phone_number, gender):
     conn = sqlite3.connect("AAACNL.db")
     cur = conn.cursor()
     cur.execute("INSERT INTO AAACNL VALUES (NULL, ?,?,?,?)", (name, address, phone_number, gender))
     conn.commit()
     conn.close()
     
     
def view():
     conn = sqlite3.connect("AAACNL.db")
     cur = conn.cursor()
     cur.execute("SELECT * FROM AAACNL")
     row = cur.fetchall()
     conn.close()
     return row
     
def search(name = " ", address = " ", phone_number = " ", gender = " "):
     conn = sqlite3.connect("AAACNL.db")
     cur = conn.cursor()
     cur.execute("SELECT * FROM AAACNL WHERE name = ? OR address = ? OR phone_number = ? OR gender = ? ", (name, address, phone_number, gender))
     row = cur.fetchall()
     conn.close()
     return row

def delete(id):
     conn = sqlite3.connect("AAACNL.db")
     cur = conn.cursor()
     cur.execute("DELETE FROM AAACNL WHERE id = ?", (id,))
     conn.commit()
     conn.close()
     
def update(id, name, address, phone_number, gender):
     conn = sqlite3.connect("AAACNL.db")
     cur = conn.cursor()
     cur.execute("UPDATE AAACNL SET name = ?, address = ?, phone_number = ?, gender = ?  WHERE id = ?", (name, address, phone_number, gender, id))
     conn.commit()
     conn.close()
     
connect()
