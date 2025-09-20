# MLOps API Deployment Template

This is a template repository for deploying a machine learning model as a scalable API on Google Cloud Run using a fully automated CI/CD pipeline with GitHub Actions.

## ✨ Features

- **FastAPI**: A high-performance Python web framework for building APIs.
- **Docker**: Containerize the application for reproducibility and portability.
- **Google Cloud Run**: Deploy as a scalable, serverless service.
- **CI/CD Automation**: Fully automated testing and deployment using GitHub Actions.
- **Workload Identity Federation**: Secure, passwordless authentication between GitHub and GCP.

## 🚀 How to Use This Template

1.  **Generate Your Repository**: Click the **"Use this template"** button on the GitHub page to create a new repository in your own account.

2.  **Clone Your New Repository**:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    ```

3.  **Set Up Your Google Cloud Project**:
    - Create a GCP Project.
    - Enable the Cloud Run and Artifact Registry APIs.
    - Create an Artifact Registry repository named `api-images`.

4.  **Configure GitHub Secrets**:
    - Set up a GCP Service Account and Workload Identity Federation as per the MLOps tutorial.
    - In your new GitHub repository, go to **Settings > Secrets and variables > Actions** and create the following three secrets:
      - `GCP_PROJECT_ID`: Your GCP project ID.
      - `GCP_SERVICE_ACCOUNT`: The email of your deployer service account.
      - `GCP_WIF_PROVIDER`: The full resource name of your Workload Identity Provider.

5.  **Customize Your Model**:
    - Replace the code in `app/model.py` with your own model's logic.
    - Update the `requirements.txt` file with your model's dependencies.

6.  **Push and Deploy**:
    Commit your changes and push them to the `main` branch. The GitHub Actions pipeline will automatically deploy your model.
    ```bash
    git push origin main
    ```