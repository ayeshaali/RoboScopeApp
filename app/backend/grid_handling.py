import sqlite3
db = 'grid.db'

#computation methods
def ID_to_board(id):
    return id

def RGB565(color):
    val = ("%0.4X" % ((int(color[0] / 255 * 31) << 11) | (int(color[1] / 255 * 63) << 5) | (int(color[2] / 255 * 31))))
    print(val)
    output = [int(val[0:2],16), int(val[2:4],16)]
    return output

def interaction(id):
    return int('10101010',2)
    
#access methods
def get_grid(): 
    '''
    Returns grid in the form a string of tuples 
    tuple: (id,active_status,red,green,blue,height)()()
    '''
    
    all_squares = ""
    #connect to database
    conn = sqlite3.connect(db)
    c = conn.cursor()
    #create a table if not existed
    c.execute('''CREATE TABLE IF NOT EXISTS squares (id int, mod_id int, active int, red int, green int, blue int, height int);''') 
    #get all rows
    for i in range(96): 
        row = c.execute('''SELECT * FROM squares WHERE id=(?);''', (i,)).fetchone()
        if row is None:
            c.execute('''INSERT into squares VALUES (?,?,?,?,?,?,?);''', (i, 0, 1, 33, 150, 243, 10))
            row = (i, 0, 1, 33, 150, 243, 10)
        all_squares+=str(row)
    #commit changes and close connection 
    conn.commit()
    conn.close()
    return all_squares

def get_all_heights():
    '''
    Returns heights of all pixels in order of ID
    '''
    conn = sqlite3.connect(db)
    c = conn.cursor()
    heights = c.execute('''SELECT height FROM squares''').fetchall()
    conn.commit()
    conn.close()
    return [h[0] for h in heights]

def get_all_colors():
    '''
    Returns colors (RGB tuple) of all pixels in order of ID
    '''
    colors = []
    conn = sqlite3.connect(db)
    c = conn.cursor()
    for i in range(96): 
        row = c.execute('''SELECT red, green, blue FROM squares WHERE id=(?);''', (i,)).fetchone()
        colors.append(row)
    conn.commit()
    conn.close()
    return colors

def serial_get(list):   
    conn = sqlite3.connect(db)
    c = conn.cursor()
    
    to_write = []
    for id in list:
        row = c.execute('''SELECT * FROM squares WHERE id=(?);''', (id,)).fetchone()
        board_id = ID_to_board(id)
        colors = RGB565(row[3:6])
        val = [board_id, interaction(id), row[6], colors[0], colors[1]]
        to_write.append([str(i) for i in val])
        
    conn.commit()
    conn.close()
    return to_write
    
#pixel methods
def toggle_active(id): 
    '''
    Takes an ID of a grid square and toggles the active status
    Returns active status (1: active, 0: inactive)
    '''
    
    conn = sqlite3.connect(db)
    c = conn.cursor()
    row = c.execute('''SELECT active FROM squares WHERE id=(?);''', (id,)).fetchone()
    active=1
    if row[0]==1:
        active=0
    c.execute('''UPDATE squares set active=(?) where id=(?)''', (active,id));
    conn.commit()
    conn.close()
    return active

def change_height(id, height):
    '''
    Takes an ID of a grid square and increase/decrease in height
    Updates pixel with new height change
    '''
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''UPDATE squares set height=height+(?) where id=(?)''', (height,id));
    conn.commit()
    conn.close()
    
def change_color(id, rgb):
    '''
    Takes an ID of a grid square and RGB values 
    Updates pixel with new color
    '''
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''UPDATE squares set red=(?), green=(?), blue=(?) where id=(?)''', (rgb[0],rgb[1],rgb[2],id));
    conn.commit()
    conn.close()

def change_mod(id, mod_id):
    '''
    Takes an ID of a grid square and a module ID
    Adds pixel to module 
    '''
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''UPDATE squares set mod_id=(?) where id=(?)''', (mod_id,id));
    conn.commit()
    conn.close()

def change_mult_mod(ids, mod_id):
    '''
    Takes a module ID and a list of pixel IDs
    Changes mod_id of pixels in list to new mod_id 
    '''
    conn = sqlite3.connect(db)
    c = conn.cursor()
    for i in ids:   
        c.execute('''UPDATE squares set mod_id=(?) where id=(?)''', (mod_id,i));
    conn.commit()
    conn.close()
    
#module methods 
def toggle_module_height(id, height):
    '''
    Takes an ID of a module and an increase or decrease in height
    Updates all squares in modules with new height change
    '''
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''UPDATE squares set height=height+(?) where mod_id=(?)''', (height,id));
    conn.commit()
    conn.close()

def toggle_module_color(id, rgb):
    '''
    takes an ID of a module and a tuple of RGB values
    Updates all squares in modules with new color
    '''
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''UPDATE squares set red=(?), green=(?), blue=(?) where mod_id=(?)''', (rgb[0],rgb[1],rgb[2],id));
    conn.commit()
    conn.close()

def toggle_module_active(id, active_bool):
    '''
    takes an ID of a module and boolean that determines inactive (false) and active (true)
    Updates all squares in module with new status
    '''
    if active_bool:
        active=1
    else:
        active=0
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('''UPDATE squares set active=(?) where mod_id=(?)''', (active,id));
    conn.commit()
    conn.close()