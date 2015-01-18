### Step #20

Dockerizing our app.

To build the image:
```
docker build -t flask-intro .
```

Run it as:
```
docker run -d -p 5000:5000 flask-intro
```
