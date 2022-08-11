-- create the database 'hbtn_0d_usa' and the table 'states' on your MySQL server
-- create the db
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create the table
CREATE TABLE IF NOT EXISTS states(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
