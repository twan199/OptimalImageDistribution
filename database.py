import os
import sqlite3


def create_database(conn):
    # Create table
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS images
                (currency text, setnr integer, size_length real, size_width real, filename text)'''
              )
    conn.commit()


def add_to_database(conn, listoffiles):
    c = conn.cursor()
    filenames = []
    setid = []
    for row in c.execute('SELECT filename FROM images ORDER BY filename;'):
        filenames.append(row[0])
    for row in c.execute('SELECT setnr FROM images ORDER BY filename;'):
        setid.append(row[0])

    if len(setid) == 0:
        max_set = 0
    else:
        max_set = max(setid) + 1
    for image in listoffiles:
        if image in filenames:
            pass
        else:
            print('\n' + image)
            is_set = input('Together with previous? (y/n) ')
            if is_set == 'n':
                textname = input('Name of currency and amount? ')
                size_length = input('Length in mm? ')
                size_width = input('Width in mm? ')
                max_set = int(max_set + 1)
                if size_length > size_width:
                    size_length1 = size_width
                    size_width1 = size_length
                    size_length = size_length1
                    size_width = size_width1
            elif is_set == 'y':
                max_set = max_set
            else:
                try:
                    raise (ValueError)
                except ValueError:
                    print("Please use y or n ...")
                    break
            new_images = (textname, max_set, size_length, size_width, image)
            c.execute('INSERT INTO images VALUES (?,?,?,?,?)', new_images)
            conn.commit()


def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn


def select_from_database(conn, listoffiles):
    c = conn.cursor()
    data = []
    for filename in listoffiles:
        filename_tuple = tuple([filename])
        for row in c.execute(
                'SELECT * FROM images WHERE (filename) IN (VALUES (?)) ORDER BY filename;',
                filename_tuple):
            data.append(row)
    print(data)
    # for image in listoffiles:
    #     print(image)


def db_main(listoffiles):
    database = "images.db"
    conn = create_connection(database)
    create_database(conn)
    add_to_database(conn, listoffiles)
    select_from_database(conn, listoffiles)