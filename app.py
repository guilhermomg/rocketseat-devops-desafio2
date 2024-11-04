from flask import Flask, jsonify, request
import os
import psycopg2

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT', '5432')
}

# Conexão com o banco de dados
def get_db_connection():
    conn = psycopg2.connect(**db_config)
    return conn

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name) VALUES (%s)', (new_user['name'],))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
