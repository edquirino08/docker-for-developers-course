from flask import Flask, request, jsonify
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.config["DEBUG"] = True

DB_CONFIG = {
    "host": "db", 
    "database": "flaskdocker",
    "user": "postgres",
    "password": "postgres"
}

@app.route('/', methods=['GET'])
def index():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * FROM public.users;")
        rows = cur.fetchall()

        results = [dict(row) for row in rows]

        cur.close()
        conn.close()

        return jsonify(results)

    except psycopg2.Error as e:
        print("Erro ao acessar o banco:", e)
        return jsonify({"error": f"Erro ao acessar o banco de dados: {e}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
