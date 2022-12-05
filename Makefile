objects = main.o Book.o Bookstore.o

bookstore: $(objects)
	g++ -o bookstore $(objects)

main.o: main.cc Bookstore.h
	g++ -c main.cc 

Book.o: Book.h Book.cc
	g++ -c Book.cc

Bookstore.o: Bookstore.h Bookstore.cc
	g++ -c Bookstore.cc

clean:
	rm -f bookstore *.o	

