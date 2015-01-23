### Step #20

Dockerizing our app.

### To build the image
```
docker build -t flask-intro .
```

### Run the container with volume
```
docker run -d -p 5000:5000 -v /Users/jorge/flask-intro:/opt/flask-intro --name web --link db:mysql flask-intro-mysql
```
