from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # --- CONFIGURAÇÕES DO PRODUTO ---
    # Substitua pelo seu link de afiliado Amazon para este PC:
    amazon_link = "https://www.amazon.com.br" 
    # Link da imagem do PC (Procure no SiteStripe da Amazon e cole o link .jpg aqui):
    image_url = "https://m.media-amazon.com"

    return f"""
    <html>
    <head>
        <title>Oferta Especial: PC Completo Intel i3 + Monitor 20"</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding: 15px; background-color: #f0f2f5; margin: 0;">
        
        <div style="background: white; padding: 25px; border-radius: 15px; display: block; margin: 10px auto; box-shadow: 0px 8px 20px rgba(0,0,0,0.1); max-width: 500px; text-align: left;">
            
            <div style="background: #e74c3c; color: white; padding: 5px 12px; border-radius: 5px; font-weight: bold; font-size: 0.8em; display: inline-block; margin-bottom: 15px;">
                🔥 MELHOR CUSTO-BENEFÍCIO 2026
            </div>

            <h1 style="color: #2c3e50; font-size: 1.4em; margin-bottom: 10px; line-height: 1.3;">
                PC Completo Intel Core i3 + Monitor 20" LED + Wi-Fi | <span style="color: #27ae60;">Pronto para Uso</span>
            </h1>

            <p style="color: #7f8c8d; font-size: 0.95em; margin-bottom: 20px;">
                A solução definitiva para o seu <b>Home Office</b> ou <b>Estudos</b>. Inicialização em segundos com SSD!
            </p>

            <div style="text-align: center; margin-bottom: 20px;">
                <img src="{image_url}" alt="PC Completo i3" style="width: 100%; max-height: 300px; object-fit: contain; border-radius: 10px;">
            </div>

            <div style="background: #f9f9f9; padding: 15px; border-radius: 10px; border-left: 5px solid #2980b9;">
                <h3 style="margin-top: 0; color: #2980b9; font-size: 1em;">🚀 ESPECIFICAÇÕES:</h3>
                <ul style="font-size: 0.9em; color: #34495e; line-height: 1.6; padding-left: 20px;">
                    <li><b>Processador:</b> Intel Core i3 (Estabilidade garantida).</li>
                    <li><b>Monitor:</b> LED 20" (Imagens nítidas e cores vivas).</li>
                    <li><b>SSD Veloz:</b> Windows 10 inicia em até 15 segundos.</li>
                    <li><b>Kit Completo:</b> Acompanha Teclado, Mouse e Wi-Fi.</li>
                </ul>
            </div>

            <div style="text-align: center; margin-top: 25px;">
                <p style="font-size: 0.8em; color: #e67e22; font-weight: bold; margin-bottom: 10px; text-transform: uppercase;">
                    Oferta expira em: <span id="countdown">00:00:00</span>
                </p>
                
                <a href="{amazon_link}" target="_blank" style="text-decoration: none;">
                    <button style="background-color: #ff9900; color: #111; border: none; padding: 20px; border-radius: 10px; cursor: pointer; font-size: 1.1em; font-weight: 800; width: 100%; box-shadow: 0px 4px 0px #cc7a00;">
                        VER PREÇO E DISPONIBILIDADE ➔
                    </button>
                </a>
                
                <p style="margin-top: 20px; font-size: 0.7em; color: #bdc3c7; text-align: center;">
                    © 2026 Soluções Infoprodutos Digitais | Enviado pela Amazon.br
                </p>
            </div>
        </div>

        <script>
            var countDate = new Date().getTime() + (30 * 60 * 1000); 
            function updateCountdown() {{
                var now = new Date().getTime();
                var gap = countDate - now;
                var second = 1000, m = second * 60, h = m * 60;
                var hours = Math.floor(gap / h), mins = Math.floor((gap % h) / m), secs = Math.floor((gap % m) / second);
                document.getElementById('countdown').innerText = (hours < 10 ? '0'+hours : hours) + ":" + (mins < 10 ? '0'+mins : mins) + ":" + (secs < 10 ? '0'+secs : secs);
                if (gap < 0) document.getElementById('countdown').innerText = "00:00:00";
            }}
            setInterval(updateCountdown, 1000);
            updateCountdown();
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
