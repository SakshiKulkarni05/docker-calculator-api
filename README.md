# 🧮 Containerized Calculator API

> A REST API built with Python and FastAPI, containerized with Docker, tested with pytest,
> automated with GitHub Actions CI, and deployed locally with Kubernetes.

[![CI Pipeline](https://github.com/SakshiKulkarni05/docker-calculator-api/actions/workflows/ci.yml/badge.svg)](https://github.com/SakshiKulkarni05/docker-calculator-api/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green)
![Docker](https://img.shields.io/badge/Docker-containerized-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-local-326CE5)

---

## 1. Project Title

**Containerized Calculator API using Python, FastAPI, Docker, GitHub Actions and Kubernetes**

---

## 2. Overview

This project builds a fully containerized REST API that performs basic arithmetic operations.
It demonstrates a complete beginner-to-intermediate DevOps pipeline:

```
Write Code → Test → Containerize → Push to GitHub → Automate CI → Deploy with Kubernetes
```

Each phase builds on the last, covering real tools used in software engineering teams.

---

## 3. Problem Statement

Developers often build applications that only run on their own machine due to environment
differences. The goal of this project is to show how to:

- Package an application so it runs the same everywhere using **Docker**
- Automatically verify code quality on every push using **CI pipelines**
- Manage containerized workloads using **Kubernetes**
- Understand cloud deployment concepts using **Azure** (documented, not live)

---

## 4. Objectives

- Build a working REST API with Python and FastAPI
- Write automated tests using pytest
- Containerize the application using Docker
- Push the project to GitHub with proper version control
- Automate testing and builds using GitHub Actions
- Deploy locally using Kubernetes (Docker Desktop)
- Document Azure cloud deployment steps

---

## 5. Features

- ✅ 4 arithmetic operations: add, subtract, multiply, divide
- ✅ Input validation — division by zero returns HTTP 400 error
- ✅ Health check endpoint (`/health`)
- ✅ Auto-generated API docs at `/docs` (Swagger UI)
- ✅ 9 automated tests — all verified passing
- ✅ Fully containerized with Docker
- ✅ CI pipeline runs on every GitHub push
- ✅ Kubernetes deployment with NodePort service

---

## 6. Technologies

| Technology | Version | Purpose |
|-----------|---------|---------|
| Python | 3.12 | Programming language |
| FastAPI | 0.115.0 | Web framework for building the REST API |
| Uvicorn | 0.30.6 | ASGI server that runs the FastAPI app |
| pytest | 8.3.3 | Automated testing framework |
| httpx | 0.27.2 | HTTP client used by FastAPI TestClient |
| Docker | Desktop | Containerization platform |
| GitHub Actions | — | CI pipeline automation |
| Kubernetes | v1.36.1 | Container orchestration (local via Docker Desktop) |
| Azure ACI | — | Cloud deployment (documented, not live) |

---

## 7. Architecture

### Full Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                        DEVELOPER MACHINE                        │
│                                                                 │
│  main.py  ──►  pytest  ──►  docker build  ──►  git push        │
│                                                                 │
└───────────────────────────────┬─────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                          GITHUB                                 │
│                                                                 │
│  Repository  ──►  GitHub Actions CI Pipeline                    │
│                        │                                        │
│                        ├── ① Checkout code                      │
│                        ├── ② Setup Python 3.12                  │
│                        ├── ③ pip install -r requirements.txt    │
│                        ├── ④ pytest tests/ -v  (9 tests ✅)     │
│                        └── ⑤ docker build -t calculator-api .   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                  KUBERNETES (Docker Desktop)                    │
│                                                                 │
│   Deployment: calculator-api  (replicas: 1)                     │
│       └── Pod                                                   │
│           └── Container: calculator-api:latest                  │
│               └── FastAPI on port 8000                          │
│                                                                 │
│   Service: calculator-api-service (NodePort)                    │
│       └── localhost:30080  ──►  Pod port 8000                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼ (documented only)
┌─────────────────────────────────────────────────────────────────┐
│                     AZURE CLOUD (ACI)                           │
│                                                                 │
│   Azure Container Registry  ──►  Azure Container Instance       │
│       calculator-api:latest          Public URL: http://        │
│                                      <dns>.azurecontainer.io    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Request Flow (Kubernetes)

```
Browser / curl
     │
     ▼
localhost:30080   (NodePort Service)
     │
     ▼
Pod port 8000   (FastAPI + Uvicorn inside container)
     │
     ▼
JSON response   {"result": 15.0}
```

---

## 8. Project Structure

```
docker-calculator-api/
│
├── main.py                        # FastAPI application — all 6 endpoints
├── requirements.txt               # Pinned Python dependencies
├── Dockerfile                     # Container build instructions
├── conftest.py                    # Adds project root to pytest path
├── .gitignore                     # Files excluded from Git
├── .dockerignore                  # Files excluded from Docker build
├── README.md                      # This file
│
├── tests/
│   ├── __init__.py
│   └── test_main.py               # 9 automated pytest tests (all passing ✅)
│
├── k8s/
│   ├── deployment.yaml            # Kubernetes Deployment (1 replica)
│   └── service.yaml               # Kubernetes NodePort Service (port 30080)
│
└── .github/
    └── workflows/
        └── ci.yml                 # GitHub Actions CI pipeline
```

---

## 9. Local Setup

### Prerequisites
- Python 3.12+
- Git

### Steps

```bash
# Clone the repository
git clone https://github.com/SakshiKulkarni05/docker-calculator-api.git
cd docker-calculator-api

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Start the development server
uvicorn main:app --reload
```

The API is available at **http://localhost:8000**
Interactive docs at **http://localhost:8000/docs**

---

## 10. API Endpoints

| Method | Endpoint | Query Params | Description |
|--------|----------|-------------|-------------|
| GET | `/` | — | Confirms API is running |
| GET | `/health` | — | Service liveness check |
| GET | `/add` | `a`, `b` | Returns `a + b` |
| GET | `/subtract` | `a`, `b` | Returns `a - b` |
| GET | `/multiply` | `a`, `b` | Returns `a * b` |
| GET | `/divide` | `a`, `b` | Returns `a / b` (400 if b=0) |

### Example Requests

```bash
curl http://localhost:8000/
# {"message": "Calculator API is running!"}

curl http://localhost:8000/health
# {"status": "healthy"}

curl "http://localhost:8000/add?a=10&b=5"
# {"result": 15.0}

curl "http://localhost:8000/subtract?a=10&b=3"
# {"result": 7.0}

curl "http://localhost:8000/multiply?a=4&b=6"
# {"result": 24.0}

curl "http://localhost:8000/divide?a=10&b=2"
# {"result": 5.0}

curl "http://localhost:8000/divide?a=10&b=0"
# {"detail": "Division by zero is not allowed."}  HTTP 400
```

---

## 11. Testing

Tests use **pytest** and **FastAPI's TestClient** (no live server needed).

```bash
pytest tests/ -v
```

**Verified output (Python 3.12, pytest 8.3.3):**

```
tests/test_main.py::test_root                  PASSED
tests/test_main.py::test_health                PASSED
tests/test_main.py::test_add                   PASSED
tests/test_main.py::test_add_negative_numbers  PASSED
tests/test_main.py::test_subtract              PASSED
tests/test_main.py::test_multiply              PASSED
tests/test_main.py::test_multiply_by_zero      PASSED
tests/test_main.py::test_divide                PASSED
tests/test_main.py::test_divide_by_zero        PASSED

9 passed in 1.20s
```

### What is tested
- Root and health endpoints return correct responses
- All 4 arithmetic operations return correct float results
- Negative number inputs work correctly
- Division by zero returns HTTP 400 with correct error message

---

## 12. Docker

### Prerequisites
- Docker Desktop installed and running

### Build and Run

```bash
# Build the image
docker build -t calculator-api:latest .

# Run the container
docker run -p 8000:8000 calculator-api:latest

# Test it
curl http://localhost:8000/health
```

### How the Dockerfile works

```dockerfile
FROM python:3.12-slim        # Lightweight base image
WORKDIR /app                 # Working directory inside container
COPY requirements.txt .      # Copy deps file first (layer cache optimization)
RUN pip install ...          # Install dependencies
COPY main.py .               # Copy application code
EXPOSE 8000                  # Document the port
CMD ["uvicorn", "main:app",  # Start the server, accessible from outside container
     "--host", "0.0.0.0", "--port", "8000"]
```

---

## 13. Git / GitHub

```bash
# Stage all changes
git add .

# Commit with a message
git commit -m "Describe what changed"

# Push to GitHub
git push origin main
```

Repository: **https://github.com/SakshiKulkarni05/docker-calculator-api**

---

## 14. GitHub Actions CI

Every push or pull request to `main` triggers the pipeline automatically.

**Pipeline file:** `.github/workflows/ci.yml`

```
Push to GitHub
      │
      ▼
GitHub Actions (ubuntu-latest)
      │
      ├── ① Checkout code
      ├── ② Set up Python 3.12
      ├── ③ pip install -r requirements.txt
      ├── ④ pytest tests/ -v          ← fails here if tests break
      └── ⑤ docker build -t calculator-api .
```

**Status:** ✅ Pipeline passed on GitHub — [View Actions](https://github.com/SakshiKulkarni05/docker-calculator-api/actions)

---

## 15. Kubernetes

### Prerequisites
- Docker Desktop with Kubernetes enabled (kubeadm provisioner)

### Deploy

```bash
# 1. Build the image locally first
docker build -t calculator-api:latest .

# 2. Apply both manifests
kubectl apply -f k8s/

# 3. Verify
kubectl get pods
kubectl get services
```

**Verified output:**

```
NAME                              READY   STATUS    RESTARTS   AGE
calculator-api-5b4c98c954-d764p   1/1     Running   0          27s

NAME                     TYPE        CLUSTER-IP       PORT(S)
calculator-api-service   NodePort    10.101.176.188   80:30080/TCP
```

### Test the Kubernetes deployment

```bash
curl http://localhost:30080/
# {"message": "Calculator API is running!"}

curl "http://localhost:30080/add?a=10&b=5"
# {"result": 15.0}
```

**Status:** ✅ Verified running on Docker Desktop Kubernetes (kubeadm, v1.36.1)

### Useful Commands

```bash
kubectl get pods                          # List pods
kubectl get deployments                   # List deployments
kubectl get services                      # List services
kubectl describe pod <pod-name>           # Full pod details and events
kubectl logs <pod-name>                   # Application logs
kubectl delete -f k8s/                    # Remove all resources
```

---

## 16. Azure Deployment Overview

> ⚠️ **Not live** — documented for learning purposes.
> Azure resources cost money. New accounts receive $200 free credit for 30 days.

### Recommended approach: Azure Container Instances (ACI)

```
Local                          Azure
─────                          ─────────────────────────────
docker build                   Resource Group
    │                              │
    ▼                              ├── Azure Container Registry (ACR)
docker push ──────────────────►    │       └── calculator-api:latest
                                   │
                                   └── Azure Container Instance (ACI)
                                           └── http://<dns>.azurecontainer.io:8000
```

### Manual steps required (after `az login`)

```bash
az group create --name calculator-api-rg --location eastus
az acr create --resource-group calculator-api-rg --name calculatorapiregistry --sku Basic --admin-enabled true
az acr login --name calculatorapiregistry
docker tag calculator-api:latest calculatorapiregistry.azurecr.io/calculator-api:latest
docker push calculatorapiregistry.azurecr.io/calculator-api:latest
az container create --resource-group calculator-api-rg --name calculator-api \
  --image calculatorapiregistry.azurecr.io/calculator-api:latest \
  --dns-name-label calculator-api-demo --ports 8000
```

### Cleanup (to stop charges)

```bash
az group delete --name calculator-api-rg --yes --no-wait
```

---

## 17. Troubleshooting

### Tests fail to import `main`

```bash
# Make sure you're in the project root and venv is active
cd c:\docker-calculator-api
venv\Scripts\activate
pytest tests/ -v
```

### Docker build fails

```bash
# Make sure Docker Desktop is running
docker info

# Rebuild from scratch (no cache)
docker build --no-cache -t calculator-api:latest .
```

### Kubernetes Pod not starting

```bash
# Check pod status and events
kubectl describe pod <pod-name>

# Common causes:
# ErrImageNeverPull  → image not built locally. Run: docker build -t calculator-api:latest .
# CrashLoopBackOff   → app is crashing. Run: kubectl logs <pod-name>
# Pending            → not enough resources. Check Docker Desktop memory allocation.
```

### Port 30080 not accessible

```bash
# Check the service exists
kubectl get services

# Check the pod is actually running (not just scheduled)
kubectl get pods

# Make sure Docker Desktop Kubernetes uses kubeadm (not kind)
# Go to: Docker Desktop → Settings → Kubernetes → select Kubeadm
```

### GitHub Actions CI fails

- Check the **Actions** tab on GitHub for the error details
- Most common cause: a test is failing — fix the code and push again
- Check that `requirements.txt` lists all dependencies

---

## 18. Future Improvements

| Improvement | Description |
|------------|-------------|
| POST endpoints | Accept JSON body instead of query parameters |
| Input validation | Reject non-numeric inputs with clear error messages |
| Modulus operation | Add `%` as a fifth operation |
| Docker Compose | Add `docker-compose.yml` for easier local running |
| CD pipeline | Auto-push Docker image to Docker Hub after CI passes |
| Live Azure deployment | Actually deploy to ACI with GitHub Actions |
| HTTPS / TLS | Add SSL certificate for secure connections |
| Logging | Structured JSON logs for production monitoring |
| More tests | Edge cases: very large numbers, floats, missing params |

---

## License

This project is for educational purposes.

---

*Built step by step as a DevOps learning project — Python → Tests → Docker → GitHub → CI → Kubernetes → Azure*
