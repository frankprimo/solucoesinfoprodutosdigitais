from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():

    # --- LINKS DOS PRODUTOS ---
    p1_link = "https://amzn.to"
    p1_img = "https://m.media-amazon.com/images/I/71T1e2NG20L._AC_SY355_.jpg"

    p2_link = "https://amzn.to"
    p2_img = "https://m.media-amazon.com/images/I/61Dw5Z8LzJL._AC_SL1000_.jpg"

    preco_produto = "R$ 1.199,00"

    return f"""
    <html>
    <head>
        <title>Ofertas Soluções Infoprodutos</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>

    <body style="font-family:sans-serif;text-align:center;padding:20px;background:#f4f4f5;margin:0;">

        <h1 style="color:#1a1a1a;margin-bottom:20px;">🚀 OFERTAS TECNOLÓGICAS DO DIA</h1>

        <div style="background:#ef4444;color:white;padding:10px 20px;border-radius:30px;font-weight:bold;margin-bottom:30px;display:inline-block;">
            ⏱️ Ofertas expiram em: <span id="timer">00:00:00</span>
        </div>


        <!-- PRODUTO 1 -->
        <div style="background:white;padding:25px;border-radius:15px;margin:auto;margin-bottom:30px;max-width:420px;box-shadow:0 5px 15px rgba(0,0,0,0.1);">

            <h2>🖥️ PC Completo Intel i3 + Monitor 20"</h2>

            <img src="{p1_img}" style="width:100%;max-height:250px;object-fit:contain;margin-bottom:15px;">

            <div style="background:#fff9e6;padding:15px;border-radius:10px;margin-bottom:15px;">
                <span style="font-size:0.9em;text-decoration:line-through;color:#888;">De: R$ 1.499,00</span><br>
                <span style="font-size:1.8em;font-weight:bold;color:#27ae60;">{preco_produto}</span>
            </div>

            <a href="{p1_link}" target="_blank">
                <button style="background:#ff9900;border:none;padding:15px;width:100%;font-size:1.1em;font-weight:bold;border-radius:10px;cursor:pointer;">
                    VER PREÇO NA AMAZON
                </button>
            </a>

        </div>


        <!-- PRODUTO 2 -->
        <div style="background:white;padding:25px;border-radius:15px;margin:auto;margin-bottom:30px;max-width:420px;box-shadow:0 5px 15px rgba(0,0,0,0.1);">

            <h2>💻 Notebook Lenovo IdeaPad</h2>

            <img src="{p2_img}" style="width:100%;max-height:250px;object-fit:contain;margin-bottom:15px;">

            <p style="font-size:0.9em;color:#555;">
            ✔ Processador Intel i3<br>
            ✔ 8GB RAM<br>
            ✔ SSD NVMe<br>
            ✔ Tela 15.6"
            </p>

            <a href="{p2_link}" target="_blank">
                <button style="background:#ff9900;border:none;padding:15px;width:100%;font-size:1.1em;font-weight:bold;border-radius:10px;cursor:pointer;">
                    VER PREÇO NA AMAZON
                </button>
            </a>

        </div>


        <footer style="font-size:12px;color:#888;margin-top:20px;">
        © 2026 Soluções Infoprodutos Digitais
        </footer>


<script>

function startTimer() {{

    const now = new Date();
    const end = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 23, 59, 59);

    function update() {{

        const diff = end - new Date();

        if(diff <= 0){{
            document.getElementById("timer").innerHTML="00:00:00";
            return;
        }}

        const h = Math.floor(diff / 3600000);
        const m = Math.floor((diff % 3600000) / 60000);
        const s = Math.floor((diff % 60000) / 1000);

        document.getElementById("timer").innerHTML =
        (h<10?"0"+h:h)+":"+(m<10?"0"+m:m)+":"+(s<10?"0"+s:s);

    }}

    update();
    setInterval(update,1000);
}}

startTimer();

</script>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
