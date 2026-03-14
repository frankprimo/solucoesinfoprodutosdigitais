from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():

    busca = request.args.get("q","").lower()

    produtos = [

    {
    "nome":"PC Completo Intel i3",
    "categoria":"Computador",
    "avaliacao":"⭐⭐⭐⭐☆",
    "imagem":"https://m.media-amazon.com/images/I/71T1e2NG20L._AC_SY355_.jpg",
    "preco":"R$ 1.065,00",
    "processador":"Intel Core i3",
    "memoria":"8GB RAM",
    "armazenamento":"SSD 240GB",
    "sistema":"Windows 10",
    "link":"https://amzn.to/40mOIdP"
    },

    {
    "nome":"Notebook Lenovo IdeaPad",
    "categoria":"Notebook",
    "avaliacao":"⭐⭐⭐⭐⭐",
    "imagem":"https://m.media-amazon.com/images/I/71uv+p19nTL._AC_SY355_.jpg",
    "preco":"R$ 2.789,00",
    "processador":"Intel Core i5",
    "memoria":"8GB RAM",
    "armazenamento":"SSD 256GB",
    "tela":"15.6 Full HD",
    "sistema":"Windows 11",
    "link":"https://amzn.to/4lnhLb1"
    },

    {
    "nome":"Monitor LG 24",
    "categoria":"Monitor",
    "avaliacao":"⭐⭐⭐⭐☆",
    "imagem":"https://m.media-amazon.com/images/I/61hxA0+MEWL._AC_SY355_.jpg",
    "preco":"R$ 500,00",
    "tela":"24 polegadas",
    "resolucao":"1920x1080",
    "taxa":"75Hz",
    "conexao":"HDMI / VGA",
    "link":"https://amzn.to/4sCIVwN"
    },

    {
    "nome":"Mouse Gamer Logitech G305",
    "categoria":"Periférico",
    "avaliacao":"⭐⭐⭐⭐⭐",
    "imagem":"https://m.media-amazon.com/images/I/51sg9BLSMTL._AC_SY355_.jpg",
    "preco":"R$ 169,00",
    "dpi":"12000 DPI",
    "botoes":"6 programáveis",
    "bateria":"até 250 horas",
    "conexao":"LIGHTSPEED sem fio",
    "link":"https://amzn.to/4uidzx0"
    }

    ]

    html_produtos = ""

    for p in produtos:

        if busca and busca not in p["nome"].lower():
            continue

        info = ""

        for chave, valor in p.items():
            if chave not in ["nome","imagem","preco","link","categoria","avaliacao"]:
                info += f"<li><b>{chave.capitalize()}</b>: {valor}</li>"

        html_produtos += f"""

        <div class="card">

        <div class="tag">🔥 MAIS VENDIDO</div>

        <img src="{p["imagem"]}">

        <h3>{p["nome"]}</h3>

        <div class="categoria">{p["categoria"]}</div>

        <div class="avaliacao">{p["avaliacao"]}</div>

        <div class="preco">{p["preco"]}</div>

        <ul>{info}</ul>

        <a href="{p["link"]}" target="_blank" rel="nofollow sponsored">

        <button>🛒 Comprar na Amazon</button>

        </a>

        </div>

        """

    return f"""
<html>

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Ofertas Tecnológicas</title>

<style>

body{{font-family:Arial;background:#f4f4f4;margin:0}}

header{{background:#111;color:white;padding:30px;text-align:center}}

.search{{margin-top:20px}}

.search input{{padding:10px;width:250px;border-radius:5px;border:none}}

.container{{display:flex;flex-wrap:wrap;justify-content:center;gap:25px;padding:30px}}

.card{{background:white;width:260px;padding:20px;border-radius:12px;box-shadow:0 4px 15px rgba(0,0,0,0.1);text-align:center;position:relative;transition:0.3s}}

.card:hover{{transform:translateY(-10px)}}

.card img{{width:100%;height:170px;object-fit:contain}}

.preco{{color:green;font-size:22px;font-weight:bold;margin:10px}}

button{{background:#ff9900;border:none;padding:12px;width:100%;border-radius:8px;font-weight:bold;cursor:pointer}}

button:hover{{background:#e68a00}}

.tag{{position:absolute;top:10px;left:10px;background:red;color:white;font-size:11px;padding:5px 8px;border-radius:6px}}

.categoria{{font-size:12px;color:#666}}

.avaliacao{{color:#ff9900;margin:5px}}

</style>

</head>

<body>

<header>

<h1>🚀 OFERTAS TECNOLÓGICAS</h1>

<form class="search">

<input type="text" name="q" placeholder="Pesquisar produto...">

</form>

</header>

<div class="container">

{html_produtos}

</div>

</body>

</html>

"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0", port=port)
