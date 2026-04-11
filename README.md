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

## 🧠 Continuacion del Proyecto

Este proyecto no solo consistió en desplegar una aplicación, sino en construir un flujo completo de trabajo DevOps, integrando desarrollo, infraestructura, automatización y observabilidad.

Durante el desarrollo se implementaron:

- Despliegue en Kubernetes (Deployments, Services, Ingress)
- Configuración segura con ConfigMaps y Secrets
- Pipeline de CI/CD con build y push automático de imágenes Docker
- Versionado de imágenes para control de releases
- Integración de métricas con Prometheus

---

## 🚨 Problemas encontrados y soluciones aplicadas

### 1. Error en despliegue de imágenes (ImagePullBackOff)
**Problema:** Kubernetes no podía descargar la imagen.  
**Causa:** Imagen inexistente o no publicada en DockerHub.  
**Solución:** Se construyó y publicó correctamente la imagen (`docker build` + `docker push`) y se verificó el nombre/tag.

---

### 2. Configuración incorrecta en Deployment
**Problema:** Error en `replicas` y nombre de contenedor.  
**Causa:** Valores mal definidos en YAML.  
**Solución:** Corrección de sintaxis y validación con `kubectl`.

---

### 3. Error de conexión a base de datos
**Problema:** Endpoint `/db` devolvía error 500.  
**Causa:** Variables de entorno mal configuradas.  
**Solución:** Uso de ConfigMaps y Secrets para desacoplar configuración.

---

### 4. CI/CD fallando en GitHub Actions
**Problema:** Error en login a DockerHub.  
**Causa:** Credenciales incorrectas o mal configuradas.  
**Solución:** Uso de secrets (`DOCKER_USERNAME` y `DOCKER_PASSWORD`) correctamente definidos.

---

### 5. Fallo al desplegar desde CI/CD a Kubernetes
**Problema:** El runner no podía conectarse al cluster local (Minikube).  
**Causa:** Falta de acceso remoto al cluster.  
**Solución:** Se limitó el pipeline a build & push, dejando el deploy manual/local (entendiendo la limitación del entorno).

---

### 6. Prometheus no detectaba métricas (TARGET DOWN)
**Problema:** Endpoint `/metrics` no era válido para Prometheus.  
**Causa:** Flask devolvía `Content-Type: text/html`.  
**Solución:** Uso de `Response()` con `CONTENT_TYPE_LATEST` para exponer métricas correctamente.

---

## 🚀 Resultado final

Se logró un sistema funcional que permite:

- Desplegar una aplicación en Kubernetes
- Exponerla mediante Ingress
- Automatizar builds con CI/CD
- Monitorear métricas en tiempo real con Prometheus

---

## 📈 Próximos pasos

- Integración con Grafana para visualización
- Implementación de alertas
- Escalado automático (HPA)
- Deploy en entorno cloud (EKS / GKE / DigitalOcean)

---

## 💬 Reflexión final

Este proyecto refleja el aprendizaje real en DevOps:  
no se trata solo de implementar herramientas, sino de entender cómo resolver problemas en entornos reales, iterar, y mejorar continuamente.


## 👨‍💻 Autor

Julio González  
DevOps / Cloud Engineer (en formación)