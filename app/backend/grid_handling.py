import sqlite3
db = 'grid.db'

def get_grid(): 
    # returns grid in the form a string of tuples (id,active_status,red,green,blue,height)()()
    all_squares = ""
    #connect to database
    conn = sqlite3.connect(db)
    c = conn.cursor()
    #create a table if not existed
    c.execute('''CREATE TABLE IF NOT EXISTS squares (id int, active int, red int, green int, blue int, height int);''') 
    #get all rows
    for i in range(96): 
        row = c.execute('''SELECT * FROM squares WHERE id=(?);''', (i,)).fetchone()
        if row is None:
            c.execute('''INSERT into squares VALUES (?,?,?,?,?,?);''', (i, 1, 33, 150, 243, 10))
            row = (i, 1, 33, 150, 243, 10)
        all_squares+=str(row)
    #commit changes and close connection 
    conn.commit()
    conn.close()
    return all_squares
    
def toggleactive(id): 
    #takes an ID of a grid square and toggles the active status
    #returns active status (1: active, 0: inactive)
    #connect to database
    conn = sqlite3.connect(db)
    c = conn.cursor()
    #get row with ID
    row = c.execute('''SELECT * FROM squares WHERE id=(?);''', (id,)).fetchone()
    #find and set new active
    active=1
    if row[1]==1:
        active=0
    #update row
    c.execute('''UPDATE squares set active=(?) where id=(?)''', (active,id));
    #commit changes and close connection 
    conn.commit()
    conn.close()
    return active

def toggle_module_height(id, height):
    #takes an ID of a module and an increase or decrease in height
    #updates all squares in modules with new height change
    #connect to database
    conn = sqlite3.connect(db)
    c = conn.cursor()
    #iterate through all squares in module: 8(id-1) to 8(id)
    for i in range((id-1)*8,id*8): 
        c.execute('''UPDATE squares set height=height+(?) where id=(?)''', (height,i));
    #commit changes and close connection 
    conn.commit()
    conn.close()

def toggle_module_color(id, rgb):
    #takes an ID of a module and a tuple of RGB values
    #updates all squares in modules with new color
    #connect to database
    conn = sqlite3.connect(db)
    c = conn.cursor()
    #iterate through all squares in module: 8(id-1) to 8(id)
    for i in range((id-1)*8,id*8): 
        c.execute('''UPDATE squares set red=(?), green=(?), blue=(?) where id=(?)''', (rgb[0],rgb[1],rgb[2],i));
    #commit changes and close connection 
    conn.commit()
    conn.close()

def toggle_module_active(id, active_bool):
    #takes an ID of a module and boolean that determines inactive (false) and active (true)
    if active_bool:
        active=1
    else:
        active=0
    #connect to database    
    conn = sqlite3.connect(db)
    c = conn.cursor()
    #iterate through all squares in module: 8(id-1) to 8(id)
    for i in range((id-1)*8,id*8): 
        c.execute('''UPDATE squares set active=(?) where id=(?)''', (active,i));
    #commit changes and close connection 
    conn.commit()
    conn.close()