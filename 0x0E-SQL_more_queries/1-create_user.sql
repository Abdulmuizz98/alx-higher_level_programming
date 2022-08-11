-- creates the MySQL server user 'user_0d_1'
CREATE USER 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- grant the user all priviledges on the server
GRANT ALL ON *.* TO 'user_0d_2'@'localhost';
