# Moon Active - Home Assignment
# Microservices Deployment with Kubernetes
This project demonstrates the deployment of microservices on a Kubernetes cluster. The microservices are simple web applications that consume URLs from environment variables, send API requests, and return responses. The deployment is managed using Helm charts, allowing for easy configuration and scaling.

Getting Started
Deploy a Kubernetes Cluster on your preferred platform.

Clone this repository to set up the codebase for your microservices:
```
git clone https://github.com/Ofekbb/moon.git
```

# Build and Deploy:
The images are built as part of the github action pipeline proccess.
The helm charts are deployed as part of the github action pipeline proccess.

## MicroServices 
# Frontend: 
this microservice is responsible for rendering the UI and sending the url path to the backend,
and recived backend api response  

# Backend:
this microservice post api request that it recived from the frontend, and send it back to the frontend.

## Pathes
# Path: /uselessfact
Description: Retrieves a random fact from uselessfacts.jsph.pl.

# Path: /funnyfact
Description: Retrieves a random Chuck Norris joke from api.chucknorris.io.

# Path: /ready
Description: Responds with a status code of 200 from backend service, indicating that the service is ready.

# Path: /backend-health
Description: Responds with a status code of 200 from backend service, indicating that the service is ready.


## GitHub Action Workflow
The workflow triggered manually and performs the following steps:
Pulls the source code from the repository.
Builds Docker images for the services, tagging them with the build number.
Pushes the Docker images to a Dockerhub registry.
Deploys the services to the Kubernetes cluster using Helm charts.
Runs tests with helm test to verify correct responses from the deployed services.


The application has been configured to be resilient using Kubernetes features such as Pod replicas, liveness probes, and readiness probes.

Ingress has been set up to split requests to the correct microservices using the same domain.

Contributing
Contributions to this project are welcome! Feel free to create pull requests or open issues if you have suggestions, improvements, or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

This README provides a basic structure for your project documentation. Feel free to customize and expand it based on the specifics of your project and any additional information you want to include.