from flask import Flask, request, jsonify
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.config["DEBUG"] = True

DB_CONFIG = {
    "host": "host.docker.internal",
    "port": 5432,
    "database": "z002",
    "user": "postgres",
    "password": "postgres"
}

@app.route('/', methods=['GET'])
def index():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT cod_contratante, razao_social, nome_fantasia, cnpj, parametros FROM public.tb_contratante;")
        rows = cur.fetchall()

        results = [dict(row) for row in rows]

        cur.close()
        conn.close()

        return jsonify(results)

    except psycopg2.Error as e:
        print("Erro ao acessar o banco:", e)
        return jsonify({"error": "Erro ao acessar o banco de dados"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
