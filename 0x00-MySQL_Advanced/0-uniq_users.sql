-- creates a table users
DROP TABLE IF EXISTS holberton.users;
CREATE TABLE IF NOT EXISTS holberton.users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255));
