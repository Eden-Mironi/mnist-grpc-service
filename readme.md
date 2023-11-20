# MNIST GRPC Service

This repository contains a GRPC service for streaming MNIST samples to a client.

## Prerequisites

- Python 3.11.1
- Docker (optional)

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/eden-mironi/mnist-grpc-service.git
    cd mnist-grpc-service
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Service

### Without Docker

1. **Start the MNIST service:**

    ```bash
    python mnist_service_server.py
    ```

2. **The service will be running on port 50051.**

### With Docker

1. **Build the Docker image for the server:**

    ```bash
    docker build -t mnist-service-server -f Dockerfile_server .
    ```

2. **Run the Docker container for the server:**

    ```bash
    docker run -p 50051:50051 mnist-service-server
    ```

## Running the Client

1. **Ensure the MNIST service is running.**

2. **Run the client:**

    ```bash
    python mnist_service_client.py
    ```

### Running the Client in a Docker Container

1. **Build the Docker image for the client:**

    ```bash
    docker build -t mnist-service-client -f Dockerfile_client .
    ```

2. **Run the Docker container for the client:**

    ```bash
    docker run mnist-service-client
    ```

3. **The client will connect to the MNIST service, open a stream, and receive training samples.**


