from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # --- PRODUTO 1: PC COMPLETO ---
    p1_link = "https://a.co" 
    p1_img = "https://m.media-amazon.com"
    p1_preco = "R$ 1.199,00"

    # --- PRODUTO 2: NOTEBOOK LENOVO (NOVO) ---
    p2_link = "https://a.co" # Link sugerido para o IdeaPad 1
    p2_img = "https://m.media-amazon.com"
    p2_nome = "Notebook Lenovo IdeaPad 1 Core i3 8GB 256GB SSD"
    p2_preco = "R$ 2.696,07"

    return f"""
    <html>
    <head>
        <title>Soluções Infoprodutos - Ofertas Tech</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="font-family: sans-serif; text-align: center; padding: 10px; background-color: #f4f4f4; margin: 0;">
        
        <h1 style="color: #2c3e50; margin: 20px 0; font-size: 1.4em;">🚀 OFERTAS TECNOLOGIA DO DIA</h1>
        
        <!-- CRONÓMETRO GERAL DE URGÊNCIA -->
        <div style="background: #e67e22; color: white; padding: 10px; font-weight: bold; margin-bottom: 20px; border-radius: 10px; display: inline-block;">
            As ofertas terminam em: <span id="timer">00:00:00</span>
        </div>

        <!-- CARTÃO DO PRODUTO 1 (PC i3) -->
        <div style="background: white; padding: 25px; border-radius: 15px; margin: 0 auto 20px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); max-width: 400px; text-align: left;">
            <h2 style="font-size: 1.1em; color: #2c3e50; text-align: center;">🖥️ PC Completo Intel i3 + Monitor 20"</h2>
            <center><img src="{p1_img}" style="width: 100%; max-height: 200px; object-fit: contain; margin: 15px 0;"></center>
            <div style="text-align: center; background: #f9f9f9; padding: 10px; border-radius: 8px; border: 1px dashed #ff9900; margin-bottom: 15px;">
                <span style="font-size: 1.4em; font-weight: 800; color: #27ae60;">{p1_preco}</span>
            </div>
            <a href="{p1_link}" target="_blank" style="text-decoration: none;">
                <button style="background-color: #ff9900; color: #111; border: none; padding: 15px; border-radius: 8px; cursor: pointer; font-size: 1em; font-weight: bold; width: 100%; box-shadow: 0px 4px 0px #cc7a00;">VER NA AMAZON ➔</button>
            </a>
        </div>

        <!-- CARTÃO DO PRODUTO 2 (LENOVO) -->
        <div style="background: white; padding: 25px; border-radius: 15px; margin: 0 auto 40px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); max-width: 400px; text-align: left;">
            <h2 style="font-size: 1.1em; color: #2c3e50; text-align: center;">💻 {p2_nome}</h2>
            <center><img src="{p2_img}" style="width: 100%; max-height: 200px; object-fit: contain; margin: 15px 0;"></center>
            <div style="text-align: center; background: #f9f9f9; padding: 10px; border-radius: 8px; border: 1px dashed #ff9900; margin-bottom: 15px;">
                <span style="font-size: 1.4em; font-weight: 800; color: #27ae60;">{p2_preco}</span>
            </div>
            <a href="{p2_link}" target="_blank" style="text-decoration: none;">
                <button style="background-color: #ff9900; color: #111; border: none; padding: 15px; border-radius: 8px; cursor: pointer; font-size: 1em; font-weight: bold; width: 100%; box-shadow: 0px 4px 0px #cc7a00;">VER NA AMAZON ➔</button>
            </a>
        </div>

        <p style="font-size: 0.7em; color: #bdc3c7; padding-bottom: 20px;">© 2026 Soluções Infoprodutos Digitais</p>

        <script>
            function startTimer() {{
                const now = new Date();
                const end = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 23, 59, 59);
                function update() {{
                    const diff = end - new Date();
                    if (diff <= 0) {{ document.getElementById('timer').innerHTML = "00:00:00"; return; }}
                    const h = Math.floor(diff / 3600000), m = Math.floor((diff % 3600000) / 60000), s = Math.floor((diff % 60000) / 1000);
                    document.getElementById('timer').innerHTML = (h<10?"0"+h:h)+":"+(m<10?"0"+m:m)+":"+(s<10?"0"+s:s);
                }}
                update(); setInterval(update, 1000);
            }}
            startTimer();
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
