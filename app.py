from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():

    produtos = [
        {
            "nome": "PC Completo Intel i3",
            "imagem": "https://m.media-amazon.com/images/I/71T1e2NG20L._AC_SY355_.jpg",
            "preco": "R$ 1.065,00",
            "processador": "Intel Core i3",
            "memoria": "8GB RAM",
            "armazenamento": "SSD 240GB",
            "sistema": "Windows 10",
            "link": "https://amzn.to/40mOIdP"
        },
        {
            "nome": "Notebook Lenovo IdeaPad",
            "imagem": "https://m.media-amazon.com/images/I/71uv+p19nTL._AC_SY355_.jpg",
            "preco": "R$ 2.789,00",
            "processador": "Intel Core i5",
            "memoria": "8GB RAM",
            "armazenamento": "SSD 256GB",
            "tela": "15.6 Full HD",
            "sistema": "Windows 11",
            "link": "https://amzn.to/4lnhLb1"
        },
        {
            "nome": "Monitor LG 24",
            "imagem": "https://m.media-amazon.com/images/I/61hxA0+MEWL._AC_SY355_.jpg",
            "preco": "R$ 500,00",
            "tela": "24 polegadas",
            "resolucao": "1920x1080",
            "taxa": "75Hz",
            "conexao": "HDMI / VGA",
            "link": "https://amzn.to/4sCIVwN"
        },
        {
            "nome": "Mouse Gamer Logitech G305",
            "imagem": "https://m.media-amazon.com/images/I/51sg9BLSMTL._AC_SY355_.jpg",
            "preco": "R$ 169,00",
            "dpi": "12000 DPI",
            "botoes": "6 programáveis",
            "bateria": "até 250 horas",
            "conexao": "LIGHTSPEED sem fio",
            "link": "https://amzn.to/4uidzx0"
        }
    ]

    html_produtos = ""

    for p in produtos:
        info = ""
        for chave, valor in p.items():
            if chave not in ["nome","imagem","preco","link"]:
                info += f"<li><b>{chave.capitalize()}</b>: {valor}</li>"

        html_produtos += f"""
        <div class="card">
            <div class="tag">🔥 TOP OFERTA</div>
            <img src="{p["imagem"]}">
            <h3>{p["nome"]}</h3>
            <div class="preco">{p["preco"]}</div>
            <ul>{info}</ul>
            <a href="{p["link"]}" target="_blank">
                <button>🛒 Comprar na Amazon</button>
            </a>
        </div>
        """

    return f"""
<html>
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Ofertas Tecnológicas</title>

<style>

body {{
font-family: Arial;
background:#f2f2f2;
margin:0;
}}

header {{
background: linear-gradient(90deg,#000,#222);
color:white;
padding:30px;
text-align:center;
}}

.banner {{
background:#ff9900;
color:black;
padding:10px;
font-weight:bold;
}}

.timer {{
font-size:22px;
color:#ff4444;
margin-top:10px;
}}

.container {{
display:flex;
flex-wrap:wrap;
justify-content:center;
gap:25px;
padding:40px;
max-width:1200px;
margin:auto;
}}

.card {{
background:white;
width:260px;
border-radius:12px;
padding:20px;
box-shadow:0 8px 20px rgba(0,0,0,0.15);
text-align:center;
transition:0.3s;
position:relative;
}}

.card:hover {{
transform:translateY(-10px);
}}

.card img {{
width:100%;
height:170px;
object-fit:contain;
}}

.card ul {{
text-align:left;
font-size:13px;
}}

.preco {{
color:green;
font-size:24px;
font-weight:bold;
margin:10px;
}}

button {{
background:#ff9900;
border:none;
padding:14px;
width:100%;
border-radius:8px;
font-weight:bold;
cursor:pointer;
font-size:15px;
}}

button:hover {{
background:#e68a00;
}}

.tag {{
position:absolute;
top:10px;
left:10px;
background:red;
color:white;
font-size:12px;
padding:5px 10px;
border-radius:6px;
}}

.info {{
max-width:900px;
margin:40px auto;
background:white;
padding:25px;
border-radius:10px;
}}

</style>

<script>

var tempo = 86400;

function atualizar(){{

var h = Math.floor(tempo/3600);
var m = Math.floor((tempo%3600)/60);
var s = tempo%60;

document.getElementById("timer").innerHTML = h+"h "+m+"m "+s+"s";

tempo--;

if(tempo < 0) tempo = 86400;

}}

setInterval(atualizar,1000);

</script>

</head>

<body>

<header>

<h1>🚀 OFERTAS TECNOLÓGICAS</h1>

<div class="banner">
💻 Promoções selecionadas com desconto
</div>

<div class="timer">
⏰ Oferta termina em: <span id="timer"></span>
</div>

</header>

<div class="container">
{html_produtos}
</div>

<div class="info">

<h3>ℹ️ Transparência</h3>

<p>Este site participa de programas de afiliados da Amazon.</p>

<p>Podemos receber comissão por compras feitas através dos links.</p>

<p>O preço é o mesmo para você.</p>

</div>

</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0", port=port)
