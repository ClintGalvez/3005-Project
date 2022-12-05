#ifndef BOOKSTORE_H
#define BOOKSTORE_H

#include <iostream>
#include <string>

#include "Book.h"

class Bookstore
{
    friend ostream& operator<<(ostream&, const Book&);

	public:
		// constructor
        Bookstore(const string& name);
        ~Bookstore();

        // getters
        //

        // setters
        //

		// other
        //

	private:
        string name;
};

#endif