"""
          Author: Clint Galvez
            Date: 11 Dec 2022
         Purpose: database functionality with postgresql (using pgadmin 4 for this project)

    Reference(s): - https://www.postgresqltutorial.com/postgresql-python/
                  - https://www.postgresqltutorial.com/postgresql-python/connect/
"""

import psycopg2
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    # cur = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print("...connection successful")
        return conn, cur


def disconnect(conn, cur):
    # close the communication with the PostgreSQL
    cur.close()

    # close connection
    if conn is not None:
        conn.close()
        print('Database connection closed.')


def verifyLogin(username, password):
    """ output: validLogin, isOwner """

    # connect to database
    out = connect()
    conn = out[0]
    cur = out[1]
    user = None

    try:
        cur.execute("""SELECT * FROM "user" WHERE username = %s""", (username,))
        user = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # disconnect from database
        disconnect(conn, cur)

    if user is None:
        print("ERROR: invalid username!")
        return False, False

    if user[1] != password:
        print("ERROR: incorrect password!")
        return False, False

    return True, user[2]


def insert(data):
    # connect to database
    out = connect()
    conn = out[0]
    cur = out[1]

    try:
        sql = """INSERT INTO book("name", isbn, "page_quantity", price, publisher)
                         VALUES(%s, %s, %s, %s, %s)"""
        # execute the INSERT statement
        cur.execute(sql, (data["name"], data["isbn"], data["pageQuantity"], data["price"], data["publisher"]))

        # sql = "INSERT INTO wrote(book, author)  VALUES(%s, %s)"
        # for author in data["authors"]:
        #     # check if author exists
        #     cur.execute("SELECT * FROM author WHERE author=%s;", author)
        #
        #     # add author to author relation if not already added
        #     if cur.fetchone() is None:
        #         # execute the INSERT statement
        #         cur.execute("INSERT INTO author(name)  VALUES(%s)", author)
        #
        #     # execute the INSERT statement
        #     cur.execute(sql, (data["name"], author))

        # commit the changes to the database
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # disconnect from database
        disconnect(conn, cur)

    return 1


def delete(data):
    """ delete book by name """

    # connect to database
    out = connect()
    conn = out[0]
    cur = out[1]

    try:
        # execute the UPDATE  statement
        cur.execute("DELETE FROM book WHERE name = %s", (data,))
        # Commit the changes to the database
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # disconnect from database
        disconnect(conn, cur)

    return 1


def browseData():
    # connect to database
    out = connect()
    conn = out[0]
    cur = out[1]
    books = None

    try:
        cur.execute("""SELECT "name" FROM book""")
        books = cur.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # disconnect from database
        disconnect(conn, cur)

    return books


def searchData():
    # connect to database
    out = connect()
    conn = out[0]
    cur = out[1]
    books = []

    try:
        cur.execute("""SELECT * FROM "user" WHERE username = %s""", )
        user = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # disconnect from database
        disconnect(conn, cur)

    return True