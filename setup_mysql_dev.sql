--For the AirBnB clone

CREATE DATABASE IF NOT EXIST hbnb_dev_db;
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT PRIVILEGES ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
