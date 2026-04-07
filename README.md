# 🚀 DevOps Platform – Docker + Kubernetes + PostgreSQL

Proyecto práctico de DevOps donde se construye y despliega una aplicación completa utilizando contenedores y Kubernetes, aplicando buenas prácticas reales de infraestructura.

---

## 🧠 Objetivo

Simular un entorno real de despliegue donde una aplicación backend se conecta a una base de datos dentro de un cluster de Kubernetes, utilizando configuración desacoplada y arquitectura escalable.

---

## 🏗️ Arquitectura

- Backend: Flask (Python)
- Base de Datos: PostgreSQL
- Contenedores: Docker
- Orquestación: Kubernetes (Minikube)
- Configuración:
  - ConfigMap (variables de entorno)
  - Secret (credenciales)

---

## ⚙️ Tecnologías utilizadas

- Docker & Docker Compose
- Kubernetes
- PostgreSQL
- Flask
- ConfigMaps & Secrets
- Linux

---

## 📁 Estructura del proyecto

devops-platform/
├── app/
│   └── server/
│       ├── app.py
│       ├── Dockerfile
│       └── requirements.txt
├── docker/
│   └── docker-compose.yml
├── k8s/
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── backend-configmap.yaml
│   ├── backend-secret.yaml
│   ├── postgres-deployment.yaml
│   └── postgres-service.yaml
├── terraform/   (futuro)
└── README.md

---

## 🚀 Despliegue paso a paso

### 1. Clonar repositorio

git clone <tu-repo>
cd devops-platform

---

### 2. Construir imagen Docker

docker build -t devops-backend:v1 ./app/server

---

### 3. Levantar Kubernetes (Minikube)

minikube start

---

### 4. Aplicar recursos en Kubernetes

kubectl apply -f k8s/backend-configmap.yaml
kubectl apply -f k8s/backend-secret.yaml
kubectl apply -f k8s/postgres-deployment.yaml
kubectl apply -f k8s/postgres-service.yaml
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml

---

### 5. Acceder a la aplicación

minikube service backend-service

---

## 🧪 Endpoints disponibles

- / → Hello World
- /health → Estado de la aplicación
- /db → Verificación de conexión a PostgreSQL

---

## 🧠 Aprendizajes clave

- Containerización de aplicaciones con Docker
- Orquestación con Kubernetes
- Uso de Deployments y Services
- Comunicación entre servicios dentro del cluster
- Uso de ConfigMaps para configuración
- Uso de Secrets para credenciales sensibles
- Debugging con logs (kubectl logs)
- Resolución de errores reales

---

## 📈 Próximos pasos

- CI/CD con GitHub Actions
- Ingress Controller
- Monitoreo con Prometheus + Grafana

---

## 👨‍💻 Autor

Julio González  
DevOps / Cloud Engineer (en formación)