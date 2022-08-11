-- creates the MySQL server user 'user_0d_1'
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- grant all the privileges to user
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
