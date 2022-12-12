DROP Schema public CASCADE;

CREATE schema ajc;


CREATE TABLE ajc.user (
    username 		VARCHAR(16),
    password 		VARCHAR(16),
    first_name 		VARCHAR(10),
    last_name 		VARCHAR(20),
    email 			VARCHAR(30),

    CONSTRAINT user_pkey PRIMARY KEY (username)
);

CREATE TABLE ajc.owner (
    username 		VARCHAR(16) REFERENCES ajc.user(username),

    CONSTRAINT owner_pkey PRIMARY KEY (username),
    CONSTRAINT owner_fkey FOREIGN KEY (username) REFERENCES ajc.user
);

CREATE TABLE ajc.book (
    isbn 			numeric(13,0) PRIMARY KEY,
    title 			VARCHAR(200),
    num_pages 	numeric(4,0),
    price 			numeric(5,2),
    genre			VARCHAR(15),
    inventory		 integer
);

CREATE TABLE ajc.author (
    first_name 		VARCHAR(20) NOT NULL,
    last_name	 	VARCHAR(20) NOT NULL,

    CONSTRAINT author_pkey PRIMARY KEY (first_name, last_name)
);

CREATE TABLE ajc.publisher (
    name 			VARCHAR(20) PRIMARY KEY,
    email	 		VARCHAR(40) UNIQUE,
    phone_num 	numeric(10) UNIQUE,
    bank_num	 	numeric(15) UNIQUE
);

CREATE TABLE ajc.basket (
	username   VARCHAR(16) NOT NULL,
    basket_id 	SERIAL NOT NULL,
	
	CONSTRAINT basket_pkey PRIMARY KEY (username, basket_id),
	CONSTRAINT basket_fkey FOREIGN KEY (username) REFERENCES ajc.user
);

CREATE TABLE ajc.order (
    order_num 	 	SERIAL NOT NULL PRIMARY KEY,
    tracking_num 	numeric(16,0) UNIQUE,
    date_placed 	timestamp without time zone,
    total_price 		numeric(9,2),
    status          	VARCHAR(20)
);


CREATE TABLE ajc.address (
    street_num 	numeric(6,0),
    street_name 	VARCHAR(20),
    city 			VARCHAR(20),
    province 		VARCHAR(20),
    country 		VARCHAR(20),
    postal_code 	VARCHAR(6),

    CONSTRAINT address_pkey PRIMARY KEY (street_num, street_name)
);

CREATE TABLE ajc.report (
    
);




CREATE TABLE ajc.writes (
    first_name 		VARCHAR(20) REFERENCES ajc.author  NOT NULL,
    last_name	 	VARCHAR(20) REFERENCES ajc.author  NOT NULL,
    isbn    			numeric(13,0) REFERENCES ajc.book(isbn) ON DELETE CASCADE,

    CONSTRAINT writes_pkey PRIMARY KEY (first_name, last_name, isbn),
    CONSTRAINT writes_fkey FOREIGN KEY (fisrt_name, last_name) REFERENCES ajc.author
);

CREATE TABLE ajc.publishes (
    isbn 		numeric(13) REFERENCES ajc.book(isbn) ON DELETE CASCADE,
    name	 	VARCHAR(20) REFERENCES ajc.publisher NOT NULL,
    year 		numeric(4),

    CONSTRAINT publishes_pkey PRIMARY KEY (isbn, name)
);

CREATE TABLE ajc.searches (
    username	 	VARCHAR(16) REFERENCES ajc.username(username),
    isbn 			numeric(13) REFERENCES ajc.book(isbn) ON DELETE CASCADE,
    quantity 		integer REFERENCES ajc.book(isbn) ON DELETE CASCADE,

    CONSTRAINT searches_pkey PRIMARY KEY (username, isbn)
);

CREATE TABLE ajc.basket_has (
    basket_id 		SERIAL NOT NULL REFERENCES ajc.basket(basket_id),
    isbn 			numeric(13) REFERENCES ajc.book(isbn) ON DELETE CASCADE,
    quantity 		integer,

    CONSTRAINT basket_has_pkey PRIMARY KEY (basket_id, isbn)
);

CREATE TABLE ajc.purchases (
    basket_id 		SERIAL NOT NULL REFERENCES ajc.basket(basket_id),
    order_num 	 	SERIAL REFERENCES ajc.order(order_num) NOT NULL,

    CONSTRAINT purchases_pkey PRIMARY KEY (basket_id, isbn)
);