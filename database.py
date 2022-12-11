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


def insert(data):
    """ insert a new book into the book table """
    sql = """INSERT INTO book(book)
                 VALUES(%s) RETURNING book_id;"""
    book_id = None
    result = 0

    # connect to database
    out = connect()
    conn = out[0]
    cur = out[1]

    try:
        # # execute the INSERT statement
        # cur.execute(sql, (data,))
        # # get the generated id back
        # book_id = cur.fetchone()[0]
        # # commit the changes to the database
        # conn.commit()

        result = 1
        print(data)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # disconnect from database
        disconnect(conn, cur)

    return result


def delete(data):
    """ delete book by part name """
    rows_deleted = 0
    result = 0

    # connect to database
    out = connect()
    conn = out[0]
    cur = out[1]

    try:
        # # execute the UPDATE  statement
        # cur.execute("DELETE FROM book WHERE name = %s", (data,))
        # # get the number of updated rows
        # rows_deleted = cur.rowcount
        # # Commit the changes to the database
        # conn.commit()

        result = 1
        print(data)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # disconnect from database
        disconnect(conn, cur)

    return result
