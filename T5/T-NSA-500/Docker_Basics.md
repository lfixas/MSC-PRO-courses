# Docker Basics

## Docker Image

A **Dockerfile** is a file that defines what is inside the container.

### Example:

```dockerfile
FROM node:alpine            # Base OS (can be Ubuntu, Debian, etc.)
WORKDIR /api                # Set working directory to /api
COPY package*.json .        # Copy package.json to the current directory (/api)
RUN npm install             # Install dependencies
COPY ./src .            
COPY .env .            
EXPOSE 8000                 # Expose port 8000
CMD [ "npm", "run", "dev" ] # Start the application
```

A **container** is a running instance of a Docker image.  
(It shares the same kernel as the image but has separate file storage.)

### Syntax:

```bash
docker build -t <image_name> <path_to_dockerfile>
docker run --name <container_name> -d -p <host_port:container_port> <image:tag>
```

Flags:
- `-d`: Run in detached mode (without a terminal)
- `-p`: Map host port to container port

---

## Docker Volumes

Volumes share files between containers and synchronize local files with the container.  
Example: **Databases** in containers.

- **"Bind Mount"**: Uses the host system filesystem.
- **"Volume"**: Managed by Docker.

### Create a Volume:

```bash
docker volume create <volume_name>
```

### Use a Volume:

```bash
docker run -p 8000:8000 --mount type=volume,source=mydata,target=/data myapp
```

Options:
- **type**: `bind` or `volume`
- **source**: Path or volume name
- **target**: Path inside the container

---

## Docker Networks

Containers **do not communicate** by default.  
Docker networks allow communication between them.

Default network: **"bridge"**  
Other options: **"host", "none", "overlay"**

### Create a Network:

```bash
docker network create --driver=bridge <network_name>
```

### Run a Container on a Custom Network:

```bash
docker run --name <container_name> -it --network <network_name> <image>
```

---

## Docker Compose

Docker Compose simplifies container orchestration using a `docker-compose.yml` file.

### Example `docker-compose.yml`:

```yaml
version: "3.9"
services:
  db:
    container_name: my_database
    image: postgres:latest
    ports:
      - "5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data

  api:
    depends_on:
      - db
    image: my_api
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgres://user:password@db:5432/dbname

volumes:
  db_data:
```

### Run with Docker Compose:

```bash
docker compose up -d
```

### Convert `docker run` to `docker-compose.yml`:

Use **[Composerize](https://www.composerize.com)** to automatically generate `docker-compose.yml` from a `docker run` command.
