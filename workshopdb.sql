CREATE DATABASE workshop;

USE workshop;

CREATE TABLE users(
user_id INT NOT NULL auto_increment primary key,
user_name varchar(50) NOT NULL UNIQUE,
password varchar(50) NOT NULL,
session_id varchar(50));