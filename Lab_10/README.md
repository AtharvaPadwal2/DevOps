# Lab 10 — End-to-End DevOps Pipeline

## Aim

To design and demonstrate an end-to-end DevOps pipeline integrating development, testing, deployment, security, and monitoring stages.

## Tools Used

- Git and GitHub
- Jira
- Jenkins
- Python and PyTest
- SonarQube
- Docker and Docker Compose
- Prometheus and Grafana

## Implementation

1. **Agile Planning:** Managed development activities through Jira.
2. **Version Control:** Maintained project code using Git and GitHub.
3. **Continuous Integration:** Configured Jenkins to execute automated stages.
4. **Automated Testing:** Executed 12 PyTest test cases successfully.
5. **Security Analysis:** Performed static code analysis using SonarQube.
6. **Containerization:** Built a Docker image for the Python application.
7. **Deployment:** Executed the containerized application using Docker.
8. **Monitoring:** Used Prometheus and Grafana to verify monitoring service health.

## Pipeline Workflow

GitHub → Jenkins → PyTest → SonarQube → Docker Build → Container Execution → Monitoring Verification

## Results

- Automated tests: 12 passed.
- Jenkins pipeline: Successful.
- SonarQube analysis: Executed successfully.
- Docker container: Executed successfully.
- Prometheus health query: 1.
- Grafana health dashboard: Working.

## Conclusion

An end-to-end DevOps pipeline was successfully implemented using GitHub, Jenkins, PyTest, SonarQube, Docker, Prometheus, and Grafana. The practical demonstrated automated testing, static security analysis, container execution, and basic infrastructure monitoring.