# 🚀 DevOps Platform – Kubernetes + GitOps + CI/CD + Monitoring

Proyecto práctico DevOps donde se construye una plataforma completa utilizando Docker, Kubernetes, GitHub Actions, ArgoCD y Prometheus, aplicando conceptos reales de automatización, GitOps, observabilidad y despliegue continuo.

---

# 🧠 Objetivo

Construir un entorno DevOps real donde:

- Una aplicación backend sea containerizada con Docker
- Kubernetes gestione los despliegues
- GitHub Actions automatice el pipeline CI/CD
- ArgoCD implemente GitOps
- Prometheus monitoree métricas
- Toda la infraestructura sea declarativa y versionada en Git

---

# 🏗️ Arquitectura

```text
Developer → GitHub → GitHub Actions → DockerHub
                              ↓
                          ArgoCD
                              ↓
                         Kubernetes
                              ↓
                    Flask + PostgreSQL
                              ↓
                         Prometheus
```

---

# ⚙️ Tecnologías utilizadas

## 🐳 Contenedores
- Docker
- DockerHub

## ☸️ Orquestación
- Kubernetes
- Minikube

## 🔄 GitOps & CI/CD
- GitHub Actions
- ArgoCD

## 📊 Monitoreo
- Prometheus

## 🧩 Backend
- Flask (Python)
- PostgreSQL

## ⚙️ Configuración
- ConfigMaps
- Secrets

## 🖥️ Sistema Operativo
- Linux

---

# 📁 Estructura del proyecto

```text
devops-platform/
│
├── app/
│   └── server/
│       ├── app.py
│       ├── requirements.txt
│       └── Dockerfile
│
├── docker/
│   └── docker-compose.yml
│
├── .github/
│   └── workflows/
│       └── ci-cd.yaml
│
├── k8s/
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── backend-configmap.yaml
│   ├── backend-secret.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-service.yaml
│   ├── prometheus-deployment.yaml
│   ├── prometheus-service.yaml
│   ├── ingress.yaml
│   └── prometheus-config.yaml
│
├── argocd/
│   └── application.yaml
│
└── README.md
```

---

# 🚀 Resultado final

Se logró una plataforma funcional con:

✅ Kubernetes  
✅ Docker  
✅ PostgreSQL  
✅ GitHub Actions  
✅ ArgoCD  
✅ GitOps  
✅ CI/CD  
✅ Prometheus  
✅ Auto Sync  
✅ Escalado  
✅ Rolling Updates  
✅ Versionado automático  
✅ Monitoreo  

---

# 👨‍💻 Autor

## Julio González

DevOps / Cloud Engineer (en formación)

- Docker
- Kubernetes
- GitOps
- ArgoCD
- GitHub Actions
- Prometheus
- Terraform
- AWS
- Linux