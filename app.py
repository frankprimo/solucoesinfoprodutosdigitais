from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Substitua este link pelo seu link de afiliado real
    amazon_link = "https://amzn.to" 
    
    return f"""
    <html>
    <head>
        <title>Oferta Especial - Soluções Digitais</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="font-family: Arial, sans-serif; text-align: center; padding: 20px; background-color: #f4f4f4; margin: 0;">
        <div style="background: white; padding: 30px; border-radius: 15px; display: block; margin: 20px auto; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); max-width: 450px; text-align: left;">
            <h1 style="color: #c0392b; font-size: 1.5em; margin-bottom: 20px; text-align: center;">🔥 OFERTA EXCLUSIVA!</h1>
            
            <div style="text-align: center;">
                <img src="https://m.media-amazon.com/images/I/51OmHUb71RL._AC_SX342_.jpg" alt="Fechadura Digital" style="width: 100%; max-height: 350px; object-fit: contain; border-radius: 10px; margin-bottom: 20px;">
            </div>

            <h2 style="font-size: 1.2em; color: #2c3e50; margin-bottom: 10px;">Fechadura Digital Inteligente</h2>
            <ul style="color: #7f8c8d; line-height: 1.6; padding-left: 20px; margin-bottom: 20px;">
                <li>✅ <b>Abertura Versátil:</b> Senha, TAG ou Chave.</li>
                <li>✅ <b>Segurança Máxima:</b> Travamento automático.</li>
                <li>✅ <b>Fácil Instalação:</b> Guia passo a passo incluso.</li>
            </ul>

            <div style="text-align: center;">
                <p style="font-size: 1.1em; color: #2c3e50; font-weight: bold; margin-bottom: 5px;">A promoção termina em:</p>
                <div id="countdown" style="font-size: 2.2em; font-weight: bold; color: #e67e22; margin-bottom: 20px; letter-spacing: 2px;">00:00:00</div>
                
                <a href="{amazon_link}" target="_blank" style="text-decoration: none;">
                    <button style="background-color: #27ae60; color: white; border: none; padding: 18px 30px; border-radius: 8px; cursor: pointer; font-size: 1.2em; font-weight: bold; width: 100%; box-shadow: 0px 4px 0px #1e8449;">
                        VER PREÇO NA AMAZON
                    </button>
                </a>
                <p style="margin-top: 25px; font-size: 0.7em; color: #bdc3c7;">© 2026 Soluções Infoprodutos Digitais</p>
            </div>
        </div>

        <script>
            var countDate = new Date().getTime() + (2 * 60 * 60 * 1000);
            function updateCountdown() {{
                var now = new Date().getTime();
                var gap = countDate - now;
                var second = 1000, minute = second * 60, hour = minute * 60;
                var h = Math.floor(gap / hour), m = Math.floor((gap % hour) / minute), s = Math.floor((gap % minute) / second);
                document.getElementById('countdown').innerText = (h < 10 ? '0'+h : h) + ":" + (m < 10 ? '0'+m : m) + ":" + (s < 10 ? '0'+s : s);
            }}
            setInterval(updateCountdown, 1000);
            updateCountdown();
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    # Para produção, utilize um servidor como Gunicorn.
    app.run(debug=True)
