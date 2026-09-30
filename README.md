# 🚀 Python DevOps CI/CD Project

A complete end-to-end DevOps project demonstrating the automation and deployment of a Python application using modern DevOps practices.

## 📌 Project Overview

This project implements a complete CI/CD pipeline that automatically tests, builds, containerizes, and deploys a Python application to a Kubernetes cluster running on AWS EC2.

The goal of this project is to demonstrate a real-world DevOps workflow from source code to production deployment.

## 🏗️ Architecture

Developer → GitHub → GitHub Actions CI/CD → Docker → Container Registry → Kubernetes (K3s) → AWS EC2

## 🛠️ Technologies Used

- Python (Flask)
- Pytest (Automated Testing)
- Docker
- GitHub Actions (CI/CD Pipeline)
- GitHub Container Registry (GHCR)
- Kubernetes
- K3s
- Helm
- AWS EC2
- Prometheus
- Grafana
- Node Exporter

## ⚙️ CI/CD Pipeline

The pipeline automatically performs:

✅ Source code checkout  
✅ Install dependencies  
✅ Run automated tests  
✅ Build Docker image  
✅ Push image to container registry  
✅ Connect to AWS EC2  
✅ Deploy application to Kubernetes  
✅ Restart deployment and verify status  

## 📦 Application Features

- Python web application
- Health check endpoint
- Automated testing
- Containerized deployment
- Kubernetes-based production environment

## 📊 Monitoring

Monitoring stack implemented using:

- Prometheus for metrics collection
- Grafana for visualization dashboards
- Node Exporter for server metrics

## ☁️ Infrastructure

Deployment environment:

- AWS EC2 instance
- Kubernetes K3s cluster
- Kubernetes Services
- Container-based application deployment

## 🎯 Project Objectives

- Build practical DevOps experience
- Implement CI/CD automation
- Understand container orchestration
- Deploy production-style applications
- Monitor infrastructure and applications

## 👨‍💻 Author

DevOps Project by [Your Name]

---

⭐ This project demonstrates a complete DevOps lifecycle from development to production deployment.
