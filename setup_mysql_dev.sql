-- create database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create user
CREATE USER IF NOT EXISTS "hbnb_dev@localhost" IDENTIFIED BY "hbnb_dev_pwd";
-- grant user all privilege on database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO "hbnb_dev@localhost";
FLUSH PRIVILEGES;
-- grant user select privilege on performance_schema db
GRANT SELECT ON performance_schema.* TO "hbnb_dev@localhost";
FLUSH PRIVILEGES;
