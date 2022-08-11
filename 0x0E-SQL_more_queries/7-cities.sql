-- create the database 'hbtn_0d_usa' and the table 'cities' on your MySQL server
-- create the db
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create the table
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL, 
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES state(id)
);
