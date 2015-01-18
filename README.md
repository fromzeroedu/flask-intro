### Step #20

Dockerizing our app.

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

### To build the image
```
docker build -t flask-intro .
```

### Run the container with volume
```
docker run -d -p 5000:5000 -v /Users/jorge/flask-intro:/opt/flask-intro --name web flask-intro
```
