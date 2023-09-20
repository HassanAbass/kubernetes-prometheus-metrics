# K8S application that dispatch pods on demand

This repository contains the Dockerized version of my application.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/)

## Building the Docker Image

To build the Docker image for this application, follow these steps:

1. Build custom image with flask and kubernetes package on it

   ```bash
   docker build -t python-flask:latest .
2. Run the k8s resources
    ```
    kubectl apply -f job.deplyment.yml
    ```

## Usage
1. Once the resources is created you can hit the http://localhost:8000 which will dispatch a job with a pod inside it that will run for sometime then switch to success and no longer utilize any OS resources.
