--For the AirBnB clone

CREATE DATABASE IF NOT EXIST hbnb_dev_db;
CREATE USER 'hbnb_dev'@'local host' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'local host';
GRANT SELECT PRIVILEGES ON performance_schema.* TO 'hbnb_dev'@'local host';
FLUSH PRIVILEGES;
