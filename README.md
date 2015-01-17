### Step #20

Dockerizing our app.

To build the image:
```
docker build .
```

First, let's create a container from the From Zero image, but making our directory
available as a data mount:
```
docker run -d -P --name myflaskapp -v /Users/jorge/flask-intro:/opt/webapp training/webapp python app.py
```
