from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():

    produtos = [
        {
            "nome": "PC Completo Intel i3",
            "imagem": "https://m.media-amazon.com/images/I/71T1e2NG20L._AC_SY355_.jpg",
            "preco": "R$ 1.199,00",
            "link": "https://amazon.com"
        },
        {
            "nome": "Notebook Lenovo IdeaPad",
            "imagem": "https://m.media-amazon.com/images/I/61Dw5Z8LzJL._AC_SL1000_.jpg",
            "preco": "R$ 2.199,00",
            "link": "https://amazon.com"
        },
        {
            "nome": "Monitor LG 24",
            "imagem": "https://m.media-amazon.com/images/I/71vFKBpKakL._AC_SL1500_.jpg",
            "preco": "R$ 899,00",
            "link": "https://amazon.com"
        },
        {
            "nome": "Mouse Gamer Logitech",
            "imagem": "https://m.media-amazon.com/images/I/51sg9BLSMTL._AC_SY355_.jpg",
            "preco": "R$ 169,00",
            "link": "https://amzn.to/4uidzx0"
        }
    ]

    html_produtos = ""

    for p in produtos:

        html_produtos += f"""
        <div style="background:white;padding:25px;margin:20px auto;
        border-radius:15px;max-width:450px;
        box-shadow:0 4px 15px rgba(0,0,0,0.1)">

        <h2 style="text-align:center">{p["nome"]}</h2>

        <img src="{p["imagem"]}" 
        style="width:100%;max-height:260px;object-fit:contain">

        <h3 style="color:green;text-align:center">
        {p["preco"]}
        </h3>

        <a href="{p["link"]}" target="_blank">
        <button style="background:#ff9900;border:none;
        padding:18px;width:100%;font-size:18px;
        border-radius:8px;font-weight:bold">

        VER NA AMAZON

        </button>
        </a>

        </div>
        """

    return f"""
    <html>
    <head>
    <title>Ofertas do Dia</title>
    <meta charset="UTF-8">
    </head>

    <body style="font-family:sans-serif;background:#f4f4f4;text-align:center">

    <h1>🚀 OFERTAS TECNOLÓGICAS DO DIA</h1>

    {html_produtos}

    </body>
    </html>
    """


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


