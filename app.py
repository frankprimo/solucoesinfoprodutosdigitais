from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Oferta Exclusiva - Soluções Digitais</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        </head>
        <body style="font-family: Arial, sans-serif; text-align: center; padding: 30px; background-color: #f4f4f4;">
            <div style="background: white; padding: 40px; border-radius: 15px; display: inline-block; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); max-width: 90%;">
                
                <h1 style="color: #c0392b;">🔥 OFERTA POR TEMPO LIMITADO!</h1>
                <p style="font-size: 1.2em; color: #2c3e50; font-weight: bold;">A promoção termina em:</p>
                
                <!-- CRONÓMETRO -->
                <div id="countdown" style="font-size: 2.5em; font-weight: bold; color: #e67e22; margin: 20px 0; letter-spacing: 2px;">
                    00:00:00
                </div>

                <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
                
                <p style="font-size: 1.1em; color: #7f8c8d;">Aproveite o desconto exclusivo antes que o tempo acabe.</p>

                <!-- SUBSTITUA O LINK ABAIXO PELO SEU LINK DA AMAZON OU MONETIZZE -->
                <a href="COLE_AQUI_O_SEU_LINK" style="text-decoration: none;">
                    <button style="background-color: #27ae60; color: white; border: none; padding: 15px 40px; border-radius: 5px; cursor: pointer; font-size: 1.3em; font-weight: bold; box-shadow: 0px 4px 0px #1e8449;">
                        GARANTIR MINHA OFERTA AGORA
                    </button>
                </a>

                <p style="margin-top: 25px; font-size: 0.8em; color: #bdc3c7;">© 2026 Soluções Infoprodutos Digitais</p>
            </div>

            <script>
                // CONFIGURAÇÃO DO TEMPO: Define 2 horas a partir de agora (exemplo)
                var countDate = new Date().getTime() + (2 * 60 * 60 * 1000);

                function updateCountdown() {
                    var now = new Date().getTime();
                    var gap = countDate - now;

                    var second = 1000;
                    var minute = second * 60;
                    var hour = minute * 60;

                    var h = Math.floor(gap / hour);
                    var m = Math.floor((gap % hour) / minute);
                    var s = Math.floor((gap % minute) / second);

                    document.getElementById('countdown').innerText = 
                        (h < 10 ? '0' + h : h) + ":" + 
                        (m < 10 ? '0' + m : m) + ":" + 
                        (s < 10 ? '0' + s : s);

                    if (gap <= 0) {
                        document.getElementById('countdown').innerText = "EXPIRADO!";
                    }
                }
                setInterval(updateCountdown, 1000);
            </script>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
