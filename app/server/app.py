from flask import Flask
import psycopg2
import os
app = Flask(__name__)

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db = os.getenv("DB_NAME")

print("DB_HOST:", host)

@app.route('/')
def home():
         return "🔥 DevOps Platform V3 - Pipeline CI/CD + Kubernetes + despliegue automático en producción"

@app.route("/health")
def health():
         return {"status": "OK"}, 200
# Por que usar "0.0.0.0"? Para que la aplicación sea accesible desde fuera del contenedor o servidor

@app.route('/db')
def db_test():
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


if __name__ == '__main__':
         app.run(host="0.0.0.0", port=5000)