from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # --- PRODUTO 1: PC COMPLETO ---
    p1_link = "https://amzn.to/4aOpkCA" 
    p1_img = "https://m.media-amazon.com/images/I/71T1e2NG20L._AC_SY355_.jpg"
    p1_preco = "R$ 1.199,00"
    
    # --- PRODUTO 2: NOTEBOOK LENOVO ---
    p2_link = "https://amzn.to/4qYpqNQ" 
    p2_img = "https://m.media-amazon.com/images/I/71v4hoMadIL._AC_SY355_.jpg"
    p2_preco = "R$ 2.696,07"

    return f"""
    <html>
    <head>
        <title>Ofertas Soluções Infoprodutos</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="font-family: sans-serif; text-align: center; padding: 10px; background-color: #f4f4f4; margin: 0;">
        
        <h1 style="color: #2c3e50; margin: 20px 0; font-size: 1.5em;">🚀 OFERTAS TECNOLÓGICAS DO DIA</h1>

        <!-- CRONÓMETRO GERAL -->
        <div style="background: #e67e22; color: white; padding: 10px; font-weight: bold; margin-bottom: 20px; border-radius: 10px; display: inline-block;">
            Ofertas expiram em: <span id="timer">00:00:00</span>
        </div>

        <!-- CARTÃO PRODUTO 1 -->
        <div style="background: white; padding: 25px; border-radius: 15px; display: block; margin: 0 auto 20px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); max-width: 420px; text-align: left;">
            <h2 style="font-size: 1.1em; color: #2c3e50; text-align: center;">🖥️ PC Completo Intel i3 + Monitor 20"</h2>
            <div style="text-align: center;">
                <img src="{p1_img}" style="width: 100%; max-height: 220px; object-fit: contain; margin-bottom: 15px;">
            </div>
            <div style="text-align: center; margin-bottom: 15px; background: #fff9e6; padding: 10px; border-radius: 8px; border: 1px dashed #ff9900;">
                <span style="font-size: 1.5em; font-weight: 800; color: #27ae60;">{p1_preco}</span>
            </div>
            <a href="{p1_link}" target="_blank" style="text-decoration: none;">
                <button style="background-color: #ff9900; color: #111; border: none; padding: 15px; border-radius: 8px; cursor: pointer; font-size: 1.1em; font-weight: bold; width: 100%; box-shadow: 0px 4px 0px #cc7a00;">VER NA AMAZON ➔</button>
            </a>
        </div>

        <!-- CARTÃO PRODUTO 2 -->
        <div style="background: white; padding: 25px; border-radius: 15px; display: block; margin: 0 auto 30px; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); max-width: 420px; text-align: left;">
            <h2 style="font-size: 1.1em; color: #2c3e50; text-align: center;">💻 Notebook Lenovo IdeaPad 1</h2>
            <div style="text-align: center;">
                <img src="{p2_img}" style="width: 100%; max-height: 220px; object-fit: contain; margin-bottom: 15px;">
            </div>
            <div style="text-align: center; margin-bottom: 15px; background: #fff9e6; padding: 10px; border-radius: 8px; border: 1px dashed #ff9900;">
                <span style="font-size: 1.5em; font-weight: 800; color: #27ae60;">{p2_preco}</span>
            </div>
            <a href="{p2_link}" target="_blank" style="text-decoration: none;">
                <button style="background-color: #ff9900; color: #111; border: none; padding: 15px; border-radius: 8px; cursor: pointer; font-size: 1.1em; font-weight: bold; width: 100%; box-shadow: 0px 4px 0px #cc7a00;">VER NA AMAZON ➔</button>
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

