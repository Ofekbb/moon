# Moon Active - Home Assignment
# Microservices Deployment with Kubernetes
This project demonstrates the deployment of microservices on a Kubernetes cluster. The microservices are simple web applications that consume URLs from environment variables, send API requests, and return responses. The deployment is managed using Helm charts, allowing for easy configuration and scaling.

Getting Started
Deploy a Kubernetes Cluster on your preferred platform.

Clone this repository to set up the codebase for your microservices:

bash
Copy code
```
git clone https://github.com/your-username/your-repo.git
```

Build and Deploy the Microservices using Helm:
The microservices are deployed using Helm charts. Each service can be deployed with different configuration values by providing a values file.
Set up GitHub Action Workflow:
A GitHub Action workflow is included in the repository to automate the deployment process. This workflow can be triggered manually.
Microservices
Useless Fact Service
Path: /uselessfact
Description: Retrieves a random fact from uselessfacts.jsph.pl.
Funny Fact Service
Path: /funnyfact
Description: Retrieves a random Chuck Norris joke from api.chucknorris.io.
Ready Service
Path: /ready
Description: Responds with a status code of 200, indicating that the service is ready.
GitHub Action Workflow
The workflow can be triggered manually and performs the following steps:
Pulls the source code from the repository.
Builds Docker images for the services, tagging them with the build number.
Pushes the Docker images to a Docker registry.
Deploys the services to the Kubernetes cluster using Helm charts and environment variables.
Runs tests to verify correct responses from the deployed services.
Bonus Features
The application has been configured to be resilient using Kubernetes features such as Pod replicas, liveness probes, and readiness probes.

Ingress has been set up to split requests to the correct microservices using the same domain.

Contributing
Contributions to this project are welcome! Feel free to create pull requests or open issues if you have suggestions, improvements, or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

This README provides a basic structure for your project documentation. Feel free to customize and expand it based on the specifics of your project and any additional information you want to include.