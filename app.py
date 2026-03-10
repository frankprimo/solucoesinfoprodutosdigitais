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
            "descricao": "Computador completo com monitor de 20 polegadas ideal para trabalho, estudo e internet.",
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
            "descricao": "Notebook Lenovo IdeaPad ideal para trabalho, estudo e uso diário com ótimo desempenho e design moderno.",
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
            "descricao": "Monitor LG de 24 polegadas com resolução Full HD ideal para escritório e entretenimento.",
            "tela": "24 polegadas",
            "resolucao": "1920 x 1080",
            "taxa": "75Hz",
            "conexao": "HDMI / VGA",
            "link": "https://amzn.to/4sCIVwN"
        },
        {
            "nome": "Mouse Gamer Logitech G305",
            "imagem": "https://m.media-amazon.com/images/I/51sg9BLSMTL._AC_SY355_.jpg",
            "preco": "R$ 169,00",
            "descricao": "Mouse gamer sem fio Logitech com sensor de alta precisão ideal para jogos competitivos.",
            "dpi": "12.000 DPI",
            "botoes": "6 botões programáveis",
            "bateria": "até 250 horas",
            "conexao": "LIGHTSPEED sem fio",
            "link": "https://amzn.to/4uidzx0"
        }
    ]

    html_produtos = ""

    for p in produtos:

        info_extra = ""

        for chave, valor in p.items():
            if chave not in ["nome","imagem","preco","link"]:
                info_extra += f"<b>{chave.capitalize()}:</b> {valor}<br>"

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

        <p style="text-align:left;font-size:14px">
        {info_extra}
        </p>

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

    <script>

    var tempo = 86400;

    function atualizarRelogio() {{

        var horas = Math.floor(tempo / 3600);
        var minutos = Math.floor((tempo % 3600) / 60);
        var segundos = tempo % 60;

        document.getElementById("relogio").innerHTML =
        horas + "h " + minutos + "m " + segundos + "s";

        tempo--;

        if (tempo < 0) {{
            tempo = 86400;
        }}
    }}

    setInterval(atualizarRelogio,1000);

    </script>

    </head>

    <body style="font-family:sans-serif;background:#f4f4f4;text-align:center">

    <h1>🚀 OFERTAS TECNOLÓGICAS DO DIA</h1>

    <h2 style="color:red">
    ⏰ Oferta termina em:
    <span id="relogio"></span>
    </h2>

    {html_produtos}

    <div style="max-width:900px;margin:40px auto;padding:20px;
    background:white;border-radius:10px;
    font-size:14px;text-align:left;
    box-shadow:0 2px 10px rgba(0,0,0,0.1)">

    <h3>ℹ️ Transparência e Informações</h3>

    <p>
    Este site participa de programas de afiliados. Isso significa que,
    se você clicar em um link e comprar o produto, eu posso receber
    uma pequena comissão. O preço é o mesmo para você.
    </p>

    <p>
    <b>Cookies:</b> O prazo para garantir de preço e contabilizar a comissão é de 24h a partir
    do clique. Porém, se você adicionar o produto ao carrinho dentro
    desse período, voce tera prazo de até 90 dias para decidir sua compra.
    </p>

    <p>
    <b>Preços:</b> Os valores são dinâmicos e podem variar a qualquer
    momento no site da Amazon.
    </p>

    </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

