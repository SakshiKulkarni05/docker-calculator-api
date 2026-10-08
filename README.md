# 🧮 Calculator API

A containerized REST API built with **Python + FastAPI**, tested with **pytest**, deployed with **Docker**, orchestrated with **Kubernetes**, and documented for **Azure cloud deployment**.

[![CI Pipeline](https://github.com/SakshiKulkarni05/docker-calculator-api/actions/workflows/ci.yml/badge.svg)](https://github.com/SakshiKulkarni05/docker-calculator-api/actions/workflows/ci.yml)

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Phase 1 — Run Locally](#phase-1--run-locally)
- [Phase 2 — Run Tests](#phase-2--run-tests)
- [Phase 3 — Docker](#phase-3--docker)
- [Phase 4 — GitHub](#phase-4--github)
- [Phase 5 — GitHub Actions CI](#phase-5--github-actions-ci)
- [Phase 6 — Kubernetes](#phase-6--kubernetes)
- [Phase 7 — Azure Deployment](#phase-7--azure-deployment)

---

## Project Overview

This project demonstrates a complete modern software delivery pipeline:

```
Code → Tests → Docker → GitHub → CI Pipeline → Kubernetes → Azure Cloud
```

Built as a learning project covering real-world DevOps concepts step by step.

---

## API Endpoints

| Method | Endpoint | Description | Example |
|--------|----------|-------------|---------|
| GET | `/` | API is running | `{"message": "Calculator API is running!"}` |
| GET | `/health` | Service liveness check | `{"status": "healthy"}` |
| GET | `/add?a=&b=` | Add two numbers | `/add?a=10&b=5` → `{"result": 15.0}` |
| GET | `/subtract?a=&b=` | Subtract b from a | `/subtract?a=10&b=5` → `{"result": 5.0}` |
| GET | `/multiply?a=&b=` | Multiply two numbers | `/multiply?a=10&b=5` → `{"result": 50.0}` |
| GET | `/divide?a=&b=` | Divide a by b | `/divide?a=10&b=5` → `{"result": 2.0}` |

> Interactive API docs at `/docs` (Swagger UI) and `/redoc`

---

## Project Structure

```
docker-calculator-api/
├── main.py                        # FastAPI application
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Container build instructions
├── conftest.py                    # pytest configuration
├── .gitignore
├── .dockerignore
├── tests/
│   ├── __init__.py
│   └── test_main.py               # Automated pytest tests
├── k8s/
│   ├── deployment.yaml            # Kubernetes Deployment
│   └── service.yaml               # Kubernetes Service (NodePort)
└── .github/
    └── workflows/
        └── ci.yml                 # GitHub Actions CI pipeline
```

---

## Phase 1 — Run Locally

### Prerequisites
- Python 3.12+

### Setup

```bash
git clone https://github.com/SakshiKulkarni05/docker-calculator-api.git
cd docker-calculator-api

python -m venv venv
venv\Scripts\activate        # Windows

pip install -r requirements.txt
uvicorn main:app --reload
```

API available at **http://localhost:8000**

---

## Phase 2 — Run Tests

```bash
pytest tests/ -v
```

Expected: 9 tests, all passing.

---

## Phase 3 — Docker

### Prerequisites
- Docker Desktop

```bash
docker build -t calculator-api:latest .
docker run -p 8000:8000 calculator-api:latest
curl http://localhost:8000/health
```

---

## Phase 4 — GitHub

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

Repository: https://github.com/SakshiKulkarni05/docker-calculator-api

---

## Phase 5 — GitHub Actions CI

Every push to `main` automatically triggers:

```
Push to GitHub → Checkout → Python 3.12 → Install deps → pytest → Docker build
```

View runs: [Actions Tab](https://github.com/SakshiKulkarni05/docker-calculator-api/actions)

---

## Phase 6 — Kubernetes

### Prerequisites
- Docker Desktop with Kubernetes enabled (kubeadm provisioner)

```bash
docker build -t calculator-api:latest .
kubectl apply -f k8s/

kubectl get pods
kubectl get services
```

**Test the live API:**
```bash
curl http://localhost:30080/
curl "http://localhost:30080/add?a=10&b=5"
```

### Architecture

```
Kubernetes Cluster (Docker Desktop)
├── Deployment: calculator-api (1 replica)
│   └── Pod → calculator-api:latest (port 8000)
└── Service: calculator-api-service (NodePort → localhost:30080)
```

### Useful Commands

```bash
kubectl get pods
kubectl get deployments
kubectl get services
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl delete -f k8s/
```

---

## Phase 7 — Azure Deployment

> ⚠️ **Cost Warning**: Azure resources incur charges. New accounts get $200 free credits for 30 days. Always clean up resources after use.

### What is Azure?

Microsoft Azure is a cloud computing platform — a global network of data centres where you can run your application 24/7 with a public URL, without managing physical servers.

### Architecture

```
Local Machine                         Azure Cloud
─────────────                         ──────────────────────────────────
main.py                               Resource Group: calculator-api-rg
    │                                     │
Dockerfile ──► docker build               ├── Azure Container Registry (ACR)
                    │                     │       └── calculator-api:latest
                    └──► docker push ────►│
                                          └── Azure Container Instance (ACI)
                                                  └── Public URL:
                                          http://<dns>.azurecontainer.io:8000
```

### Azure Deployment Options

| Option | Complexity | Approx. Cost | Best For |
|--------|-----------|-------------|----------|
| **Azure Container Instances (ACI)** | Simplest | ~$0.01/hr | Learning, demos |
| Azure App Service | Moderate | ~$13/mo | Production APIs |
| Azure Kubernetes Service (AKS) | Complex | ~$70+/mo | Large-scale production |

> **Recommended for this project: Azure Container Instances (ACI)**

### Prerequisites

1. **Azure Account** — [Create free account](https://azure.microsoft.com/free)
2. **Azure CLI**:
   ```powershell
   winget install Microsoft.AzureCLI
   ```
3. **Docker Desktop** — already installed ✅

### Deployment Overview

> 🔐 Run these steps manually — they require your Azure login.

**Step 1 — Login:**
```bash
az login
```

**Step 2 — Create Resource Group:**
```bash
az group create --name calculator-api-rg --location eastus
```

**Step 3 — Create Container Registry:**
```bash
az acr create \
  --resource-group calculator-api-rg \
  --name calculatorapiregistry \
  --sku Basic \
  --admin-enabled true
```

**Step 4 — Build and Push Image:**
```bash
az acr login --name calculatorapiregistry

docker tag calculator-api:latest \
  calculatorapiregistry.azurecr.io/calculator-api:latest

docker push calculatorapiregistry.azurecr.io/calculator-api:latest
```

**Step 5 — Get ACR credentials:**
```bash
az acr credential show --name calculatorapiregistry
# Save the username and password for Step 6
```

**Step 6 — Deploy Container Instance:**
```bash
az container create \
  --resource-group calculator-api-rg \
  --name calculator-api \
  --image calculatorapiregistry.azurecr.io/calculator-api:latest \
  --registry-login-server calculatorapiregistry.azurecr.io \
  --registry-username <acr-username> \
  --registry-password <acr-password> \
  --dns-name-label calculator-api-demo \
  --ports 8000 \
  --os-type Linux \
  --cpu 1 \
  --memory 1
```

**Step 7 — Get your public URL:**
```bash
az container show \
  --resource-group calculator-api-rg \
  --name calculator-api \
  --query ipAddress.fqdn \
  --output tsv
```

### Testing After Deployment

```bash
# Replace <your-dns> with the output of Step 7
curl http://<your-dns>.azurecontainer.io:8000/
curl http://<your-dns>.azurecontainer.io:8000/health
curl "http://<your-dns>.azurecontainer.io:8000/add?a=10&b=5"
```

Expected responses:
```json
{"message": "Calculator API is running!"}
{"status": "healthy"}
{"result": 15.0}
```

### Monitoring

```bash
# View container logs
az container logs \
  --resource-group calculator-api-rg \
  --name calculator-api

# Check container status
az container show \
  --resource-group calculator-api-rg \
  --name calculator-api \
  --query containers[0].instanceView.currentState
```

### Cost Considerations

| Resource | Approximate Cost |
|----------|-----------------|
| Azure Container Registry (Basic) | ~$5/month |
| Container Instance (1 CPU, 1GB) running 24/7 | ~$35/month |
| Container Instance stopped | Free |

> 💡 Stop the container when not in use:
> ```bash
> az container stop --resource-group calculator-api-rg --name calculator-api
> ```

### Cleanup — Remove All Azure Resources

> ⚠️ Run this when done to stop all charges:

```bash
az group delete --name calculator-api-rg --yes --no-wait
```

This removes everything: Container Instance, Container Registry, all images, and networking resources.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.12 | Programming language |
| FastAPI | Web framework |
| Uvicorn | ASGI server |
| pytest | Automated testing |
| Docker | Containerization |
| Kubernetes | Container orchestration |
| GitHub Actions | CI pipeline |
| Azure ACI | Cloud deployment |

---

## 📄 License

This project is for educational purposes.
