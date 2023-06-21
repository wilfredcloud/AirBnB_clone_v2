-- create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant user all privilege on database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- grant user select privilege on performance_schema db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
