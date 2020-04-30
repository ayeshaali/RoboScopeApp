import sqlite3
db = 'grid.db'

def get_grid(): 
    all_squares = ""
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS squares (id int, active int, red int, green int, blue int, height int);''')  # run a CREATE TABLE comma
    for i in range(96): 
        row = c.execute('''SELECT * FROM squares WHERE id=(?);''', (i,)).fetchone()
        if row is None:
            c.execute('''INSERT into squares VALUES (?,?,?,?,?,?);''', (i, 1, 33, 150, 243, 10))
            row = (i, 1, 33, 150, 243, 10)
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
    return active

def toggle_module_height(id, height):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    for i in range((id-1)*8,id*8): 
        c.execute('''UPDATE squares set height=height+(?) where id=(?)''', (height,i));
    conn.commit()
    conn.close()

def toggle_module_color(id, rgb):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    for i in range((id-1)*8,id*8): 
        c.execute('''UPDATE squares set red=(?), green=(?), blue=(?) where id=(?)''', (rgb[0],rgb[1],rgb[2],i));
    conn.commit()
    conn.close()

def toggle_module_active(id, active_bool):
    if active_bool:
        active=1
    else:
        active=0
        
    conn = sqlite3.connect(db)
    c = conn.cursor()
    for i in range((id-1)*8,id*8): 
        c.execute('''UPDATE squares set active=(?) where id=(?)''', (active,i));
    conn.commit()
    conn.close()