from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
import psycopg2
import os

app = Flask(__name__)

# 📊 Métrica Prometheus
REQUEST_COUNT = Counter('app_requests_total', 'Total de requests a la app')

# 🌐 Variables de entorno
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db = os.getenv("DB_NAME")

print("DB_HOST:", host)

# 🔄 Contador de requests
@app.before_request
def before_request():
    REQUEST_COUNT.inc()

# 🏠 Endpoint principal
@app.route('/')
def home():
    return "🔥 DevOps Platform V6 - Pipeline CI/CD + Kubernetes + despliegue automático en producción"

# ❤️ Healthcheck
@app.route("/health")
def health():
    return {"status": "OK"}, 200

# 🗄️ Test DB
@app.route('/db')
def db_test():
    try:
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=db
        )
        
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()

        cur.close()
        conn.close()

        return {"result": result[0]}

    except Exception as e:
        return {"error": str(e)}, 500

# 📈 Métricas Prometheus (FORMA CORRECTA)
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# 🚀 Run app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)