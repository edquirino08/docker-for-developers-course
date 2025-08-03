# docker-for-developers-course
Companion project for the Docker for Developers course. Includes practical exercises with Docker, Docker Swarm, and Kubernetes.


## Running Docker Containers

- docker run <image-name> - run a container from an image (container name is auto-generated).
- docker run -d <image-name> - run a container in detached mode.
- docker run --name <container-name> <image-name> - run a container with a specific name.
- docker run -p <host-port>:<container-port> <image-name> - run a container and map a host port to a container port.
- docker run -d -p <host-port>:<container-port> --name <container-name> <image-name> - run a container in detached mode with port mapping and a specific name.
- docker run -it <image-name> - run a container in interactive mode (useful for debugging).
- docker run -it --rm <image-name> - run a container in interactive mode and remove it after exit.

## Listing and Managing Containers
- docker ps - list running containers.
- docker ps -a - list all containers (including stopped ones).

## Stopping and Removing Containers
- docker stop <container-id> - stop a running container.
- docker rm <container-id> - remove a stopped container.
- docker rmi <image-name> - remove an image.

## Docker Images
- docker pull <image-name> - download an image from Docker Hub.
- docker build -t <image-name> . - build a Docker image from a Dockerfile.
- docker images - list all Docker images.


## Inspecting Containers and Images
- docker inspect <container-id> - view detailed information about a container.
- docker inspect <image-name> - view detailed information about an image.
- docker exec -it <container-id> <command> - execute a command inside a running container.
- docker logs <container-id> - view logs of a container.
- docker top <container-id> - view running processes inside a container.
- docker stats <container-id> - view resource usage statistics of a container.
- docker stats - view resource usage statistics of all running containers.

## Docker Hub Actions
- docker login - log in to Docker Hub.
- docker logout - log out of Docker Hub.
- docker tag <image-name> <new-image-name> - tag an image with a new name.
- docker push <image-name> - push an image to Docker Hub.

## Docker Volumes
- docker run -d -p <host-port>:<container-port> --name <name> --rm  -v /path <image-name> - anonymous volume mount.
- docker volume ls - list all Docker volumes.
- docker run -v <volume-name>:/path <image-name> - mount a named volume to a container.
- docker run -d -p <host-port>:<container-port> --name <name> -v <volume-name>:/<path> <image-name> - run a container with a named volume.
- docker volume create <volume-name> - create a new Docker volume.

## Bind Mounts
- docker run -d -p <host-port>:<container-port> --name <name> -v /path:/<path> <image-name> - Persists data in a specific directory on the host machine.
- docker run -d -p <host-port>:<container-port> --name <name -v <project-directory>:/<docker-directory> <image-name> - Mounts a project directory from the host machine to the container. Is useful for development purposes, because changes made in the host directory are reflected in the container.
