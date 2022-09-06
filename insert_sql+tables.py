INSERT INTO customer(
	customer_id,
	first_name,
	last_name
)
VALUES(
	2,
	'samad',
	'sama'
);
INSERT INTO Concessions(
	concession_id,
	amount,
	concession_name,
	customer_id
)
VALUES(
	5,
	3.00,
	'marry',
	5
);
INSERT INTO Movies(
	movie_id,
	runtime,
	rating,
	movie_name
)
VALUES(
	3,
	'home work',
	'sam',
	'james'	
); 
INSERT INTO Tickets(
	ticket_id,
	price,
	movie_id,
	customer_id,
	movie_name,
	rating
)
VALUES(
	3,
	7.00,
	3,
	3,
	'harry potter',
	'R'
);
UPDATE Tickets
SET movie_name = 'harry potter'
WHERE movie_id = 3;
UPDATE Tickets
SET rating = 'R'
WHERE movie_id = 3;

INSERT INTO showtimes(
	showtime_id,
	movie_id,
	show_time
)
VALUES(
	1,
	1,
	'2022-08-30 02:00:00-05'
);
INSERT INTO showtimes(
	showtime_id,
	movie_id,
	show_time
)
VALUES(
	2,
	2,
	'2022-08-30 05:00:00-05'
);
INSERT INTO showtimes(
	showtime_id,
	movie_id,
	show_time
)
VALUES(
	3,
	3,
	'2022-08-30 07:00:00-05'
);
UPDATE Movies
SET movie_genre = 'SCI-FI'
WHERE movie_id = 1;
UPDATE Movies
SET movie_genre = 'Comedy'
WHERE movie_id = 2;
UPDATE Movies
SET movie_genre = 'Comedy'
WHERE movie_id = 3;
UPDATE Tickets
SET showtime_id = 1
WHERE ticket_id = 1;
UPDATE Tickets
SET showtime_id = 2
WHERE ticket_id = 2;
UPDATE Tickets
SET showtime_id = 3
WHERE ticket_id = 3;


CREATE TABLE Customer (
  customer_id SERIAL,
  first_name VARCHAR(60),
  last_name VARCHAR(60),
  PRIMARY KEY ("customer_id")
);

CREATE TABLE Concessions (
  concession_id SERIAL,
  amount NUMERIC(5,2),
  concession_name VARCHAR(60),
  customer_id SERIAL,
  PRIMARY KEY ("concession_id"),
	FOREIGN KEY("customer_id")
   REFERENCES Customer("customer_id")
);

CREATE TABLE Movies (
  movie_id SERIAL,
  runtime TIME,
  rating VARCHAR(60),
  movie_name VARCHAR(60),
  show_time DATE DEFAULT CURRENT_DATE,
  PRIMARY KEY (movie_id)
);
CREATE TABLE Showtimes(
	showtime_id SERIAL,
	movie_id INTEGER,
	show_time TIMESTAMP WITH TIME ZONE,
	PRIMARY KEY (showtime_id),
	FOREIGN KEY (movie_id)
		REFERENCES Movies("movie_id")
	
);

CREATE TABLE Tickets (
  ticket_id SERIAL,
  price NUMERIC(5,2),
  movie_id INTEGER NOT NULL,
  customer_id INTEGER NOT NULL,
  PRIMARY KEY ("ticket_id"),
  FOREIGN KEY ("movie_id")
	REFERENCES Movies("movie_id"),
  FOREIGN KEY ("customer_id")
	REFERENCES Customer("customer_id")
);
ALTER TABLE Tickets
ADD movie_name VARCHAR(60);
ALTER TABLE movies
DROP show_time;
ALTER TABLE Movies
ADD movie_genre VARCHAR(60);
ALTER TABLE Tickets
ADD showtime_id INTEGER;
ALTER TABLE Tickets
DROP rating;
ALTER TABLE Tickets
DROP movie_name;