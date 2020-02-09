import sqlite3

db_file = 'art_werks.db'



class InputError(Exception):
    pass

def main():
    menu = True
    while menu:
        # Prints out a display for the user to see. 
        print('\n Database Menu : \n '
        '1 : Add new Artist \n'
        '2 : Search Artwork by Artist \n'
        '3 : Display Available Artwork By Artist \n'
        '4 : Add New Artwork by Artist \n'
        '5 : Change Availbilty by Artwork \n'
        '6 : Type Quit to Exit the program \n')

        menuChoice = input("Please enter a number. ")
        # Went for a simple Menu layout. If I can get this to run I would like to try and use a GUI. 

        if menuChoice == '1':
            add_Artist()
        if menuChoice == '2':
            search_Artwork()
        if menuChoice == '3':
            displayAvailable()
        if menuChoice == '4':
            add_new_Artwork()
        if menuChoice == '5':
            change_Availblity()
        if menuChoice == '6' :
            menu = False
        else :
            print("Please enter a valid option")

def add_Artist():
    ''' Add new Artist to database. If the Artist is already in the database the program with tell the user
    and then go back to the main menu. '''

    # Function to return a valid name
    added_artist = isName()
    # Fuction to return a valid email
    added_email = isEmail()
    
    insert_sql = "INSERT INTO artists (artist , email_address) VALUES (?,?)"
    
    with sqlite3.connect(db_file) as conn : 
        c = conn.cursor()
        c.execute(' SELECT * FROM artists WHERE artist =(?)',(added_artist,))
        all_rows = c.fetchall()
        if len(all_rows) == 0:
            conn.execute(insert_sql ,(added_artist, added_email) ) 
            print(f" {added_artist} Added to the database.")
        else :
            print ("Already in the database. ")

def search_Artwork():
    # If an artist is in the database it will list their works. Otherwise it will tell the user that there is nothing here
    
    search_term = input('Enter an artist to search for : ')
    read_sql = "SELECT artist , artwork_name FROM artworks WHERE artist = (?)"

    with sqlite3.connect(db_file) as conn :
        c = conn.cursor()
        c.execute (read_sql ,(search_term,) )
        all_rows = c.fetchall()

        # Checking if there are any Artwork and returning the proper values.
        if len (all_rows) == 0 :
            print(f'{search_term} has no Artwork here.')
        else:
         for row in all_rows:
                print (row[0] + " " + row[1])

def displayAvailable():
    
    search_term = input('Enter an artist to search for : ')
    read_sql = "SELECT artist , artwork_name FROM artworks WHERE artist = (?) AND available = 'Available' "

    with sqlite3.connect(db_file) as conn :
        c = conn.cursor()
        c.execute (read_sql ,(search_term,) )
        all_rows = c.fetchall()

        # Checking if there are any Artwork and returning the proper values.
        if len (all_rows) == 0 :
            print(f'{search_term} has no Artwork here.')
        else:
            for row in all_rows:
                print (row[0] + " " + row[1])

def add_new_Artwork():
    pass
def change_Availblity():
    pass

def isEmail():
# Checks the endings of the email to make sure it has propers extension
    extentsions_list = (".net", ".com", ".edu")
    email = input("Please enter an Artist Email")
# Index to check the last 4 values of the email. 
    if email[:-4] not in extentsions_list :
        email = input("Please enter an Artist Email that ends with a .com")
    else: 
        return email
        
def isName():
# Mainly checks if a name is present. Difficult to Regex names 
    name = input("Please enter an Artist Name")
    while not name :
        name = input("Please enter an Artist Name")
    return name


main()