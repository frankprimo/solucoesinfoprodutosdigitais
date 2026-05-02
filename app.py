from flask import Flask, request, render_template, redirect
import sqlite3
import os

app = Flask(__name__)

# =========================
# BANCO DE DADOS (SQLite)
# =========================
def init_db():
    conn = sqlite3.connect("produtos.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        categoria TEXT,
        avaliacao TEXT,
        imagem TEXT,
        preco TEXT,
        link TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()


# =========================
# HOME (LISTA PRODUTOS)
# =========================
@app.route("/")
def home():
    busca = request.args.get("q", "").lower()

    conn = sqlite3.connect("produtos.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nome, categoria, avaliacao, imagem, preco, link FROM produtos")
    rows = cursor.fetchall()

    conn.close()

    produtos = []

    for r in rows:
        p = {
            "nome": r[0],
            "categoria": r[1],
            "avaliacao": r[2],
            "imagem": r[3],
            "preco": r[4],
            "link": r[5]
        }

        if busca:
            if busca not in p["nome"].lower() and busca not in p["categoria"].lower():
                continue

        produtos.append(p)

    return render_template("index.html", produtos=produtos, busca=busca)


# =========================
# ADMIN (CADASTRAR PRODUTO)
# =========================
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":

        nome = request.form["nome"]
        categoria = request.form["categoria"]
        avaliacao = request.form["avaliacao"]
        imagem = request.form["imagem"]
        preco = request.form["preco"]
        link = request.form["link"]

        conn = sqlite3.connect("produtos.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO produtos (nome, categoria, avaliacao, imagem, preco, link)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (nome, categoria, avaliacao, imagem, preco, link))

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("admin.html")


# =========================
# TESTE
# =========================
@app.route("/teste")
def teste():
    return "OK FUNCIONANDO"


# =========================
# RODAR
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
