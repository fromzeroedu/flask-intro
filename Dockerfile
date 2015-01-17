#
# First Flask App Dockerfile
#
#

# Pull base image.
FROM dockerfile/ubuntu

# Define mountable directories.
#VOLUME ["/opt"]

# Define working directory.
#WORKDIR /data

# Define default command.
#CMD ["mysqld_safe"]

# Expose ports.
EXPOSE 5000
