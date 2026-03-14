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
    "preco":"Só na AMAZON",
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
    "preco":"Só na AMAZON",
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
    "preco":"Só na AMAZON",
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
    "preco":"Só na AMAZON",
    "dpi":"12000 DPI",
    "botoes":"6 programáveis",
    "bateria":"até 250 horas",
    "conexao":"LIGHTSPEED sem fio",
    "link":"https://amzn.to/4uidzx0"
    },

    {
    "nome":"Teclado Gamer Redragon Kumara",
    "categoria":"Periférico",
    "avaliacao":"⭐⭐⭐⭐⭐",
    "imagem":"https://m.media-amazon.com/images/I/61Z9sR8i1lL._AC_SY355_.jpg",
    "preco":"Só na AMAZON",
    "switch":"Outemu Blue",
    "iluminacao":"LED Vermelho",
    "conexao":"USB",
    "link":"https://amzn.to/exemplo1"
    },

    {
    "nome":"Headset Gamer HyperX Cloud Stinger",
    "categoria":"Áudio",
    "avaliacao":"⭐⭐⭐⭐⭐",
    "imagem":"https://m.media-amazon.com/images/I/61iYJk3E6sL._AC_SY355_.jpg",
    "preco":"Só na AMAZON",
    "driver":"50mm",
    "microfone":"Com cancelamento",
    "conexao":"P2",
    "link":"https://amzn.to/exemplo2"
    },

    {
    "nome":"SSD Kingston 480GB",
    "categoria":"Armazenamento",
    "avaliacao":"⭐⭐⭐⭐⭐",
    "imagem":"https://m.media-amazon.com/images/I/61nvsBnH7CL._AC_SX450_.jpg",
    "preco":"Só na AMAZON",
    "capacidade":"480GB",
    "velocidade":"500MB/s",
    "interface":"SATA",
    "link":"https://amzn.to/3NAEXWE"
    },

    {
    "nome":"Memória RAM 16GB Corsair",
    "categoria":"Memória",
    "avaliacao":"⭐⭐⭐⭐⭐",
    "imagem":"https://m.media-amazon.com/images/I/61a7pZ4K0XL._AC_SY355_.jpg",
    "preco":"Só na AMAZON",
    "capacidade":"16GB",
    "frequencia":"3200MHz",
    "tipo":"DDR4",
    "link":"https://amzn.to/4sOo4qA"
    },

    {
    "nome":"Webcam Logitech C920",
    "categoria":"Acessório",
    "avaliacao":"⭐⭐⭐⭐⭐",
    "imagem":"https://m.media-amazon.com/images/I/61-6uAf8soL._AC_SY355_.jpg",
    "preco":"Só na AMAZON",
    "resolucao":"Full HD 1080p",
    "microfone":"Duplo integrado",
    "conexao":"USB",
    "link":"https://amzn.to/4lzwXls"
    },

    {
    "nome":"Cadeira Gamer ThunderX3",
    "categoria":"Gamer",
    "avaliacao":"⭐⭐⭐⭐☆",
    "imagem":"https://m.media-amazon.com/images/I/71VqjPlOJAL._AC_SY355_.jpg",
    "preco":"Só na AMAZON",
    "material":"Couro sintético",
    "ajuste":"Altura e inclinação",
    "suporte":"até 120kg",
    "link":"https://amzn.to/4su2rw1"
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
