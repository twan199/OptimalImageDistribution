import os
import sqlite3


def create_database(servername, c):
    if os.path.isfile(servername) is False:
        # Create table
        c.execute('''CREATE TABLE IF NOT EXISTS images
                (currency text, setnr text, size_length text, size_width real, filename text)'''
                  )


def add_values(listoffiles, c):
    c.execute(
        "INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")


def db_main():
    conn = sqlite3.connect('images.db')
    c = conn.cursor()
    create_database("images.db", c)
    #add_values(listofvalues, c)


db_main()