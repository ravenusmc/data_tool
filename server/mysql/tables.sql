CREATE DATABASE data_tool;

use data_tool;

CREATE TABLE users
(
  user_id INT NOT NULL AUTO_INCREMENT,
  username VARCHAR(240) NOT NULL,
  email VARCHAR(240) NOT NULL,
  password VARCHAR(240) NOT NUll,
  PRIMARY KEY(user_id)
);

SHOW COLUMNS FROM users;

INSERT INTO users
VALUES (1, 'test', 'a1@yahoo.com', 'test');