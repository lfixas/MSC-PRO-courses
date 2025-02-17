# POPEYE BECOME A TRUE DOCKER SAILOR!

---

## Overview

This project aims to containerize and deploy a simple web poll application using Docker and Docker Compose. The application consists of several components:

- **Poll**: A Flask Python web application that gathers votes and pushes them into a Redis queue.
- **Redis Queue**: Holds the votes sent by the Poll application, awaiting consumption by the Worker.
- **Worker**: A Java application that consumes votes from the Redis queue and stores them into a PostgreSQL database.
- **PostgreSQL Database**: Persists the votes stored by the Worker.
- **Result**: A Node.js web application that fetches votes from the database and displays the result.

---

## Docker Images

### Poll
- Based on a Python official image.
- Installs app dependencies with `pip3 install -r requirements.txt`.
- Exposes and runs on port 80.
- Starts the app with `flask run --host=0.0.0.0 --port=80`.

### Result
- Based on an official Node.js v12 Alpine image.
- Exposes and runs on port 80.
- Installs app dependencies with `npm install`.

### Worker
- Uses a multi-stage build:
  - **First stage - compilation**:
    - Based on `maven:3.8.4-jdk-11-slim`.
    - Builds and packages the Worker application.
    - Generates `worker-jar-with-dependencies.jar`.
  - **Second stage - run**:
    - Based on `openjdk:11-jre-slim`.
    - Runs the Worker with `java -jar worker-jar-with-dependencies.jar`.

## Docker Compose

The `docker-compose.yml` file orchestrates the containers:

- **Services**:
  - `poll`: Builds the Poll image and redirects port 5000 of the host to port 80 of the container.
  - `redis`: Uses an existing official Redis image and opens port 6379.
  - `worker`: Builds the Worker image.
  - `db`: Represents the PostgreSQL database and uses an existing official PostgreSQL image.
  - `result`: Builds the Result image and redirects port 5001 of the host to port 80 of the container.
- **Networks**:
  - `poll-tier`: Allows Poll to communicate with Redis.
  - `result-tier`: Allows Result to communicate with the database.
  - `back-tier`: Allows Worker to communicate with Redis and the database.
- **Volume**:
  - `db-data`: Named volume for persistent database data.

---

## Running the Application

1. Make sure you have Docker and Docker Compose installed on your system.
2. Clone this repository.
3. Navigate to the project directory.
4. Run `docker-compose up --build` to build and start the containers.
5. Access the Poll application at `http://localhost:5000` and submit votes.
6. View the results at `http://localhost:5001`.

## License

This project is licensed under the terms of the [MIT licence](LICENSE).
