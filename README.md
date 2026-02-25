# GKE GenAI Gateway

A production-grade Generative AI microservice deployed on Google Kubernetes Engine (GKE) using the modern **Kubernetes Gateway API** and **Terraform**.

## 🏗️ Architecture
This project demonstrates a secure, scalable way to expose AI models to the internet.
* **Infrastructure as Code:** Terraform for VPC, Subnets, and GKE cluster provisioning.
* **Networking:** GKE Gateway API (`gke-l7-global-external-managed`) for Global Load Balancing.
* **AI Integration:** Python Flask microservice utilizing **Gemini 2.0 Flash** via Vertex AI.
* **Security:** **Workload Identity** to securely grant Pods access to GCP services without static API keys.



## 🚀 Deployment Workflow
1. **Infrastructure:** `terraform init && terraform apply`
2. **Containerization:** `gcloud builds submit --tag gcr.io/[PROJECT_ID]/hello-genai:v5`
3. **Orchestration:** `kubectl apply -f k8s/`

## 🛠️ Tech Stack
- **Cloud:** Google Cloud Platform (GCP)
- **Containerization:** Docker, Google Artifact Registry
- **Orchestration:** Kubernetes (GKE)
- **IaC:** Terraform
- **Language:** Python 3.9+
- **AI Model:** Gemini 2.0 Flash

## 🔍 Key Troubleshooting Lessons
- **State Management:** Handled Terraform state mismatches during project migrations.
- **Model Evolution:** Successfully transitioned from legacy Gemini 1.5 to 2.0 Flash.
- **IAM Sync:** Resolved Workload Identity propagation delays using K8s service account annotations.