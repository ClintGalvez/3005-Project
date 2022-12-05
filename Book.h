#ifndef BOOK_H
#define BOOK_H

#include <iostream>
#include <string>

using namespace std;

class Book
{
    friend ostream& operator<<(ostream&, const Book&);

	public:
		// constructor
        Book(const string& name);
        ~Book();

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