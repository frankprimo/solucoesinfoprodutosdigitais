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
            <span class="tag">OFERTA</span>
            <h3>{p["nome"]}</h3>
            <img src="{p["imagem"]}">
            <div class="preco">{p["preco"]}</div>
            <ul>{info}</ul>
            <a href="{p["link"]}" target="_blank">
                <button>🛒 Ver na Amazon</button>
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
body {{ font-family: Arial; background:#f4f4f4; margin:0; }}
header {{ background:#111; color:white; padding:25px; text-align:center; }}
.timer {{ text-align:center; font-size:20px; color:red; margin-top:10px; }}
.container {{ display:flex; flex-wrap:wrap; justify-content:center; gap:25px; padding:30px; max-width:1200px; margin:auto; }}
.card {{ background:white; width:260px; padding:20px; border-radius:12px; box-shadow:0 4px 15px rgba(0,0,0,0.1); position:relative; text-align:center; }}
.card img {{ width:100%; height:170px; object-fit:contain; }}
.card ul {{ text-align:left; font-size:13px; }}
.preco {{ color:green; font-size:22px; font-weight:bold; margin:10px; }}
button {{ background:#ff9900; border:none; padding:12px; width:100%; border-radius:8px; font-weight:bold; cursor:pointer; }}
button:hover {{ background:#e68a00; }}
.tag {{ position:absolute; top:10px; left:10px; background:red; color:white; font-size:12px; padding:5px 10px; border-radius:6px; }}
.info {{ max-width:900px; margin:40px auto; background:white; padding:25px; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,0.1); }}
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
<h1>🚀 OFERTAS TECNOLÓGICAS DO DIA</h1>
<div class="timer">⏰ Oferta termina em: <span id="timer"></span></div>
</header>
<div class="container">{html_produtos}</div>
<div class="info">
<h3>ℹ️ Transparência</h3>
<p>Este site participa de programas de afiliados da Amazon. Podemos receber comissão por compras feitas através dos links.</p>
<p>O preço é o mesmo para você.</p>
<p>Os preços podem variar diretamente no site da Amazon.</p>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0", port=port)
