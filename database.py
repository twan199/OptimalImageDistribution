import os
import sqlite3


def create_database(conn):
    # Create table
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS images
                (currency text, setnr real, size_length real, size_width real, filename text)'''
              )
    conn.commit()


def add_values(conn, new_images):
    c = conn.cursor()
    c.executemany("INSERT INTO images VALUES (?,?,?,?,?)", new_images)
    conn.commit()
    conn.close()


def order_images(conn, listoffiles):
    listoffiles.sort()
    c = conn.cursor()
    filenames = []
    for row in c.execute('SELECT filename FROM images ORDER BY filename;'):
        filenames.append(row)
    for image in listoffiles:
        if image in filenames:
            ...
    #new_images = list(, , ,  , ,)


def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


def db_main(listoffiles):
    database = "images.db"
    conn = create_connection(database)
    create_database(conn)
    order_images(conn, listoffiles)
