DROP DATABASE IF EXISTS skintect;
CREATE DATABASE skintect;
USE skintect;

DROP TABLE IF EXISTS Registration;
CREATE TABLE Registration (
  email varchar(64) NOT NULL, 
  fname varchar(100) NOT NULL,
  lname varchar(100) NOT NULL,
  mlnum mediumint NOT NULL,
  npi mediumint NOT NULL,
  street varchar(50) NOT NULL,
  state varchar(50) NOT NULL,
  zip mediumint NOT NULL,
  CHECK (email NOT REGEXP '^[a-zA-Z0-9][a-zA-Z0-9._-]*[a-zA-Z0-9._-]@[a-zA-Z0-9][a-zA-Z0-9._-]*[a-zA-Z0-9]\\.[a-zA-Z]{2,63}$'),
  PRIMARY KEY (email)
) ENGINE=InnoDB;

DROP TABLE IF EXISTS Accounts;
CREATE TABLE Accounts (
  email varchar(64) NOT NULL, 
  password varchar(30) NOT NULL,
  foreign key (email) references Registration(email),
  PRIMARY KEY (email)
) ENGINE =InnoDB;

DROP TABLE IF EXISTS Diagnose;
CREATE TABLE Diagnose (
  email varchar(64) NOT NULL, 
  sumbitTime DATETIME NOT NULL,
  imageId mediumint UNIQUE,
  diagnosis varchar(100) NOT NULL,
  diagnosisType varchar(100) NOT NULL,
  localization varchar(100) NOT NULL,
  age smallint NOT NULL,
  sex smallint NOT NULL,
  foreign key (email) references Registration(email),
  PRIMARY KEY (email, dateTime)
) ENGINE =InnoDB;
