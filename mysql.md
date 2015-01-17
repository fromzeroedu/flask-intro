# MySQL Setup

### Start boot2docker
```
boot2docker start
```

### Export environment variables
```
export DOCKER_HOST=tcp://192.168.59.103:2376
export DOCKER_CERT_PATH=/Users/jorge/.boot2docker/certs/boot2docker-vm
export DOCKER_TLS_VERIFY=1
```

### Start the main db:
```
docker run --name mysql -e MYSQL_ROOT_PASSWORD=test -d -p 3306:3306 mariadb
```

### Start a client:
```
docker run --name mysql-client -it --link mysql:mysql --rm mariadb sh -c 'exec mysql -uroot -ptest -hmysql'
```

### Create a database

Show databases
```
SHOW DATABASES
```

Create the database
```
CREATE DATABASE my_flask_app;
```

Check the database exists
```
SHOW DATABASES
```

Select the database
```
USE my_flask_app;
```

Create the User table
```
CREATE TABLE user(
user_id INT NOT NULL AUTO_INCREMENT,
username VARCHAR(64) NOT NULL,
password VARCHAR(40) NOT NULL,
PRIMARY KEY(user_id)
);
```

Check the table exists
```
SHOW TABLES;
```

Insert a record to make sure the table works
```
insert into user values('','admin','12345');
```

Check the record exists
```
SELECT * FROM user;
```
Now we need to install the Flask MySQL extension
```
pip install flask-mysql
```
