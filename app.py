from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # --- VARIÁVEIS TÉCNICAS ---
    amazon_link = "https://www.amazon.com.br/Condicionado-Split-TCL-T-Pro-Inverter/dp/B0F3QCWL1Z" 
    # LINK DA IMAGEM TOTALMENTE CORRIGIDO ABAIXO:
    image_url = "https://m.media-amazon.com"
    
    return f"""
    <html>
    <head>
        <title>Oferta TCL - Verão Gelado & Econômico</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="font-family: Arial, sans-serif; text-align: center; padding: 20px; background-color: #f4f4f4; margin: 0;">
        <div style="background: white; padding: 30px; border-radius: 15px; display: block; margin: 20px auto; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); max-width: 450px; text-align: left;">
            <h1 style="color: #2980b9; font-size: 1.3em; margin-bottom: 20px; text-align: center;">🚀 TECNOLOGIA E POTÊNCIA PARA O SEU VERÃO 🚀</h1>
            
            <div style="text-align: center;">
                <img src="{image_url}" alt="Ar-Condicionado TCL 9000 BTUs" style="width: 100%; max-height: 300px; object-fit: contain; border-radius: 10px; margin-bottom: 20px;">
            </div>

            <h2 style="font-size: 1.2em; color: #2c3e50; margin-bottom: 15px; text-align: center;">Apresentamos o TCL 9000 BTUs ❄️</h2>
            
            <ul style="color: #34495e; line-height: 1.8; padding-left: 10px; list-style: none; margin-bottom: 20px;">
                <li>✅ <b>Resfriamento Rápido:</b> Conforto imediato.</li>
                <li>✅ <b>Economia Real:</b> Tecnologia Inverter (até 75% de economia) 📉</li>
                <li>✅ <b>Confiabilidade TCL:</b> Wi-Fi integrado e Comando de Voz 🎙️</li>
            </ul>

            <div style="text-align: center; background-color: #ecf0f1; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
                <p style="font-size: 1em; color: #2c3e50; margin: 0;">Quer dormir fresco sem susto na conta de luz? 😴</p>
            </div>

            <div style="text-align: center;">
                <p style="font-size: 0.9em; color: #7f8c8d; font-weight: bold; margin-bottom: 5px;">ESTA CONDIÇÃO EXPIRE EM:</p>
                <div id="countdown" style="font-size: 2.2em; font-weight: bold; color: #e67e22; margin-bottom: 20px; letter-spacing: 2px;">00:00:00</div>
                
                <a href="{amazon_link}" target="_blank" style="text-decoration: none;">
                    <button style="background-color: #27ae60; color: white; border: none; padding: 20px 30px; border-radius: 8px; cursor: pointer; font-size: 1.1em; font-weight: bold; width: 100%; box-shadow: 0px 4px 0px #1e8449;">
                        QUERO ECONOMIZAR NA AMAZON
                    </button>
                </a>
                <p style="margin-top: 25px; font-size: 0.7em; color: #bdc3c7;">© 2026 Soluções Infoprodutos Digitais</p>
            </div>
        </div>

        <script>
            var countDate = new Date().getTime() + (45 * 60 * 1000); 
            function updateCountdown() {{
                var now = new Date().getTime();
                var gap = countDate - now;
                var second = 1000, minute = second * 60, hour = minute * 60;
                var h = Math.floor(gap / hour), m = Math.floor((gap % hour) / minute), s = Math.floor((gap % minute) / second);
                document.getElementById('countdown').innerText = (h < 10 ? '0'+h : h) + ":" + (m < 10 ? '0'+m : m) + ":" + (s < 10 ? '0'+s : s);
                if (gap < 0) document.getElementById('countdown').innerText = "00:00:00";
            }}
            setInterval(updateCountdown, 1000);
            updateCountdown();
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
