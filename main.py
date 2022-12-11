"""
          Author: Clint Galvez
            Date: 11 Dec 2022
         Purpose: bookstore application connected to a database (sql),
                  see database.py for database functions used in this file

    Reference(s): - NA
"""

from database import *


def login():
    loggedIn = False
    username = ""
    password = ""
    isOwner = False

    print("Login --")

    # get login info
    username = input("Enter username: ")
    password = input("Enter password: ")

    # verify login info
    print("\nVerifying user...")
    # query through database...

    # reattempt login
    loggedIn = True  # TEMP
    while not loggedIn:
        print("\n...verification failed\n\nplease try again...")

        # get login info
        username = input("Enter username: ")
        password = input("Enter password: ")

        # verify login info
        # query through database...
        loggedIn = True

    # verification complete
    print("...verification successful")

    # check if user is an owner
    if username == "owner":
        isOwner = True

    return username, isOwner


def menu(isOwner):
    o = -1

    if isOwner:
        o = input("\nmenu:"
                  "\n\t0. Exit"
                  "\n\t1. Add Book"
                  "\n\t2. Remove Book"
                  "\n\t3. Print Report"
                  "\nEnter an integer from 0-3: ")
        while not o.isnumeric() or not (0 <= int(o) <= 3):
            print("...invalid option\n")
            o = input("menu:"
                      "\n\t0. Exit"
                      "\n\t1. Add Book"
                      "\n\t2. Remove Book"
                      "\n\t3. Print Report"
                      "\nEnter an integer from 0-3: ")
    else:
        o = input("\nmenu:"
                  "\n\t0. Exit"
                  "\n\t1. Browse"
                  "\n\t2. Search"
                  "\n\t3. View Basket"
                  "\n\t4. Track Order"
                  "\nEnter an integer from 0-4: ")
        while not o.isnumeric() or not (0 <= int(o) <= 4):
            print("...invalid option\n")
            o = input("menu:"
                      "\n\t0. Exit"
                      "\n\t1. Browse"
                      "\n\t2. Search"
                      "\n\t3. View Basket"
                      "\n\t4. Track Order"
                      "\nEnter an integer from 0-4: ")
    return int(o)


def addBook():
    # get book info
    print("Add Book --")

    name = input("Enter name: ")
    isbn = input("Enter ISBN: ")

    pageQuantity = input("Enter page quantity: ")
    while not (pageQuantity.isnumeric()):
        pageQuantity = input("\nERROR: invalid input\n\nEnter page quantity: ")
    pageQuantity = int(pageQuantity)

    price = input("Enter price: ")
    while not (price.isnumeric()):
        price = input("\nERROR: invalid input\n\nEnter price: ")
    price = float(price)

    publisher = input("Enter publisher: ")

    authors = []
    print("\nEnter authors (Enter 0 when done) --")
    while True:
        author = input("Enter author: ")
        if author == "0":
            break
        authors.append(author)

    genres = []
    print("\nEnter genres (Enter 0 when done) --")
    while True:
        genre = input("Enter genre: ")
        if genre == "0":
            break
        genres.append(genre)

    # create book
    book = {
        "name": name,
        "isbn": isbn,
        "pageQuantity": pageQuantity,
        "price": price,
        "publisher": publisher,
        "authors": authors,
        "genres": genres
    }

    # insert book in database
    print("adding book...")
    result = insert(book)
    if result > 0:
        print("...book added")
        return
    elif result < 0:
        print("...book already exists")
        return
    print(print("...failed to add book"))


def removeBook():
    # get book info
    print("Remove Book --")
    book = input("Enter name: ")

    # delete book from database
    print("removing book...")
    result = delete(book)
    if result > 0:
        print("...book removed")
        return
    elif result < 0:
        print("...book does not exist")
        return
    print("...failed to remove book")


if __name__ == '__main__':
    # application variables
    out = None
    user = ""
    isOwner = False
    option = -1

    # run application
    out = login()
    user = out[0]
    isOwner = out[1]
    while True:
        # menu
        option = menu(isOwner)

        # options
        if isOwner:
            if option == 1:  # add book
                addBook()
            elif option == 2:  # remove book
                removeBook()
            elif option == 3:  # print report
                print("report begin...\n...finished")
        else:
            if option == 1:  # browse
                print("books...\n...finished")
            elif option == 2:  # search
                print("searching...\n...finished")
            elif option == 3:  # view basket
                print("basket...\n...finished")
            elif option == 4:  # track order
                print("order...\n...finished")

        # exit application
        if option == 0:
            break

    print("...application closed")