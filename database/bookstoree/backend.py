import sqlite3
def create():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS book(id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()
def insert(title,author,year,isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows
def delete(id):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,))
    conn.commit()
    conn.close()
def update(id,title,author,year,isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("UPDATE  book SET title = ? ,author = ?,year = ?,isbn=? WHERE id = ?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book ")
    rows=cur.fetchall()#displays dataa as tuples
    conn.close()
    return rows
create()
#insert("abc","Rob",1999,733548)
#delete(2)
#delete(3)


#print(search(author = "Rob"))
#update(1,"rich","sajid",2018,38574)
#sprint(view())
