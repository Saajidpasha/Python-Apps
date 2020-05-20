import sqlite3

#create a connection
#create a cursor object
#commot any changes
#close the connection
def create():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS store(name TEXT,quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()
def insert(name,quantity,price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(name,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
def update(quantity,price,name):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?,price = ? WHERE name = ?",(quantity,price,name))
    conn.commit()
    conn.close()

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE name = ?",(item,))
    conn.commit()
    conn.close()
update(0,2,"chsmpagne")
print(view())
