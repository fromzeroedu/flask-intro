#
# First Flask App Dockerfile
#
#

# Pull base image.
FROM centos:7.0.1406

# Build commands
RUN yum install -y python-setuptools mysql-connector-python mysql-devel gcc python-devel
RUN easy_install pip
RUN mkdir /opt/flask-intro
WORKDIR /opt/flask-intro
ADD requirements.txt /opt/flask-intro/
RUN pip install -r requirements.txt
ADD . /opt/flask-intro

# Define mountable directories.
#VOLUME ["/opt"]

# Define working directory.
#WORKDIR /data

# Define default command.
#CMD ["mysqld_safe"]

# Expose ports.
EXPOSE 5000
