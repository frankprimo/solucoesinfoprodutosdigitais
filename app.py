from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Oferta Especial - Soluções Digitais</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body style="font-family: Arial, sans-serif; text-align: center; padding: 20px; background-color: #f4f4f4;">
            <div style="background: white; padding: 30px; border-radius: 15px; display: inline-block; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); max-width: 450px;">
                
                <h1 style="color: #c0392b; font-size: 1.5em; margin-bottom: 20px;">🔥 OFERTA EXCLUSIVA!</h1>

                <!-- IMAGEM DO PRODUTO ATUALIZADA -->
                <img src="https://m.media-amazon.com/images/I/51OmHUb71RL._AC_SX342_.jpg" alt="Produto Amazon" style="width: 100%; max-height: 350px; object-fit: contain; border-radius: 10px; margin-bottom: 20px;">

                <p style="font-size: 1.1em; color: #2c3e50; font-weight: bold; margin-bottom: 5px;">A promoção termina em:</p>
                
                <div id="countdown" style="font-size: 2.2em; font-weight: bold; color: #e67e22; margin-bottom: 20px; letter-spacing: 2px;">
                    00:00:00
                </div>

                <!-- SEU LINK DE AFILIADO COMPLETO -->
                <a href="https://amzn.to" style="text-decoration: none;">
                    <button style="background-color: #27ae60; color: white; border: none; padding: 18px 30px; border-radius: 8px; cursor: pointer; font-size: 1.2em; font-weight: bold; width: 100%; box-shadow: 0px 4px 0px #1e8449;">
                        VER PREÇO NA AMAZON
                    </button>
                </a>

                <p style="margin-top: 25px; font-size: 0.7em; color: #bdc3c7;">© 2026 Soluções Infoprodutos Digitais</p>
            </div>

            <script>
                var countDate = new Date().getTime() + (2 * 60 * 60 * 1000);
                function updateCountdown() {
                    var now = new Date().getTime();
                    var gap = countDate - now;
                    var second = 1000, minute = second * 60, hour = minute * 60;
                    var h = Math.floor(gap / hour), m = Math.floor((gap % hour) / minute), s = Math.floor((gap % minute) / second);
                    document.getElementById('countdown').innerText = (h < 10 ? '0'+h : h) + ":" + (m < 10 ? '0'+m : m) + ":" + (s < 10 ? '0'+s : s);
                    if (gap <= 0) document.getElementById('countdown').innerText = "EXPIRADO!";
                }
                setInterval(updateCountdown, 1000);
            </script>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
