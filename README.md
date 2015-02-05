### Step #21

### Start the main db:
```
docker run --name db -e MYSQL_ROOT_PASSWORD=test -d -p 3306:3306 mariadb
```

### Create the database, running a temporary client:
```
docker run --name mysql-client -it --link db:mysql --rm mariadb sh -c 'exec mysql -uroot -ptest -hmysql'
```

Once inside MySQL:
```
CREATE DATABASE my_flask_app;
USE my_flask_app;
CREATE TABLE user(
    user_id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(64) NOT NULL,
    password VARCHAR(64) NOT NULL,
    PRIMARY KEY(user_id)
    );
INSERT INTO user VALUES('', 'jorge', '12345');
```

### Build the new image:
```
docker build -t flask-intro-mysql .
```

### Run the container with volume and sql connection
```
docker run -d -p 5000:5000 -v /Users/jorge/flask-intro:/opt/flask-intro --name web --link db:mysql flask-intro-mysql
```
