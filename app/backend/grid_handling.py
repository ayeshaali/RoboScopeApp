import sqlite3
db = 'grid.db'

def get_grid(): 
    all_squares = ""
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS squares (id int, active int, red int, green int, blue int);''')  # run a CREATE TABLE comma
    for i in range(96): 
        row = c.execute('''SELECT * FROM squares WHERE id=(?);''', (i,)).fetchone()
        if row is None:
            c.execute('''INSERT into squares VALUES (?,?,?,?,?);''', (i, 1, 255, 0, 0))
            row = (i, 1, 255, 0, 0)
        all_squares+=str(row)
    conn.commit()
    conn.close()
    return all_squares
    
def toggleactive(id): 
    all_squares = ""
    conn = sqlite3.connect(db)
    c = conn.cursor()
    row = c.execute('''SELECT * FROM squares WHERE id=(?);''', (id,)).fetchone()
    active=1
    if row[1]==1:
        active=0
    c.execute('''UPDATE squares set active=(?) where id=(?)''', (active,id));
    conn.commit()
    conn.close()
    