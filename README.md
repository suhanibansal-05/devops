# 🛠️ Automated CI/CD Pipeline with Jenkins, Docker, and GitHub Integration

This project demonstrates a fully automated CI/CD pipeline setup using **Jenkins**, **Docker**, and **GitHub**. It pulls the latest code from the repository, runs Python tests, builds a Docker container, and deploys it — all triggered automatically on code updates.

---

## 🚀 Features

- ✅ **CI/CD Pipeline using Jenkins**
- 🔁 **GitHub Webhooks** to trigger builds on every commit/push
- 🐳 **Docker Image Build & Push** automated via Jenkins
- 🧪 **Python Unit Testing** before Docker image creation
- 📦 **Automated Deployment** of updated container

---

## 🧩 Tech Stack

- **Jenkins** (for automation)
- **GitHub** (as source control + webhook trigger)
- **Python** (application language)
- **Docker** (for containerization)
- **Docker Hub** (image registry)

---

## 🧪 Workflow Overview

1. **Code Commit**: You push changes to the GitHub repository.
2. **GitHub Webhook**: Triggers a Jenkins job automatically.
3. **Jenkins Job**:
   - Pulls latest code from GitHub
   - Runs Python tests
   - Builds a Docker image if tests pass
   - Logs into Docker Hub using access token
   - Pushes the new image to Docker Hub
   - Optionally runs the container

---

## 📂 Project Structure
├── Jenkinsfile / Jenkins Job Script
├── Dockerfile
├── requirements.txt
├── app/ or src/
│ ├── main.py
│ └── ...
├── tests/
│ └── test_app.py
└── README.md
