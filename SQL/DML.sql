INSERT INTO "user"(username, "password", "owner")
VALUES
	('a', 'a', FALSE),
	('Amanda', 'password', FALSE),
	('Jacob', 'password', FALSE),
	('Ali', 'password', FALSE),
	('Clint', 'password', TRUE),
	('o', 'o', TRUE),
	('owner', 'owner', TRUE)

INSERT INTO publisher("name", address, email, "phone_number", "banking_account")
VALUES
	('AJC', 'Address 1', 'ajc@gmail.com', 1111111111, 'bank account 1'),
	('Clint Co.', 'Address 2', 'clintco@gmail.com', 2222222222, 'bank account 2'),
	('Jacob Stories & More', 'Address 3', 'jacobstoriesandmore@gmail.com', 3333333333, 'bank account 3'),
	('Fiesty Ali Pro.', 'Address 4', 'fiestyaliproductions@gmail.com', 4444444444, 'bank account 4')

INSERT INTO book("name", isbn, "page_quantity", price, publisher)
VALUES
	('Lord of the Rings', 12141, 400, 20, 'AJC'),
	('Cat in the Hat', 41321, 15, 15, 'Clint Co.'),
	('Chicken 101', 14321, 101, 10, 'Fiesty Ali Pro.'),
	('How to Eat Fried Worms!', 24123, 146, 36, 'Jacob Stories & More'),
	('Twilight: A Story Retold', 12141, 400, 20, 'AJC')

INSERT INTO author("name")
VALUES
	('Bill'),
	('Joe'),
	('Steve')