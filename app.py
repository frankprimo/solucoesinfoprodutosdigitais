from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # --- CONFIGURAÇÕES DOS PRODUTOS (LINKS ATUALIZADOS) ---
    p1_link = "https://amzn.to" 
    p1_img = "https://m.media-amazon.com"
    
    p2_link = "https://amzn.to" 
    p2_img = "https://m.media-amazon.com"

    return f"""
    <html>
    <head>
        <title>Ofertas Soluções Infoprodutos</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="font-family: sans-serif; text-align: center; padding: 10px; background-color: #f4f4f5; margin: 0;">
        
        <h1 style="color: #1a1a1a; margin: 25px 0; font-size: 1.5em; letter-spacing: -0.5px;">🚀 OFERTAS TECNOLÓGICAS DO DIA</h1>

        <!-- CRONÓMETRO DE URGÊNCIA -->
        <div style="background: #ef4444; color: white; padding: 12px 20px; border-radius: 50px; font-weight: bold; margin-bottom: 25px; display: inline-block; box-shadow: 0 4px 12px rgba(239, 68, 68, 0.2);">
            ⏱️ Ofertas expiram em: <span id="timer">00:00:00</span>
        </div>

        <!-- CARTÃO PRODUTO 1 -->
        <div style="background: white; padding: 25px; border-radius: 20px; display: block; margin: 0 auto 20px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); max-width: 420px; text-align: left; border: 1px solid #e5e7eb;">
            <h2 style="font-size: 1.15em; color: #1f2937; text-align: center; margin-bottom: 20px;">🖥️ PC Completo Intel i3 + Monitor 20"</h2>
            <div style="text-align: center;">
                <img src="{p1_img}" style="width: 100%; max-height: 220px; object-fit: contain; margin-bottom: 20px;">
            </div>
            
            <div style="background: #f9fafb; padding: 15px; border-radius: 12px; margin-bottom: 20px; font-size: 0.9em; color: #4b5563; border: 1px solid #f3f4f6;">
                <b style="color: #111827;">Por que escolher este modelo?</b>
                <ul style="margin: 8px 0 0 0; padding-left: 20px; line-height: 1.6;">
                    <li>Desempenho ágil com SSD incluso</li>
                    <li>Ideal para tarefas de escritório e estudos</li>
                    <li>Kit completo: Monitor, Teclado e Mouse</li>
                    <li>Sistema Windows 10 pronto para usar</li>
                </ul>
            </div>

            <a href="{p1_link}" target="_blank" style="text-decoration: none;">
                <button style="background-color: #ff9900; color: #111; border: none; padding: 18px; border-radius: 12px; cursor: pointer; font-size: 1.1em; font-weight: 800; width: 100%; box-shadow: 0 4px 0 #cc7a00; transition: 0.2s;">
                    VER PREÇO ATUALIZADO ➔
                </button>
            </a>
        </div>

        <!-- CARTÃO PRODUTO 2 -->
        <div style="background: white; padding: 25px; border-radius: 20px; display: block; margin: 0 auto 40px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); max-width: 420px; text-align: left; border: 1px solid #e5e7eb;">
            <h2 style="font-size: 1.15em; color: #1f2937; text-align: center; margin-bottom: 20px;">💻 Notebook Lenovo IdeaPad 1</h2>
            <div style="text-align: center;">
                <img src="{p2_img}" style="width: 100%; max-height: 220px; object-fit: contain; margin-bottom: 20px;">
            </div>

            <div style="background: #f9fafb; padding: 15px; border-radius: 12px; margin-bottom: 20px; font-size: 0.9em; color: #4b5563; border: 1px solid #f3f4f6;">
                <b style="color: #111827;">Destaques técnicos:</b>
                <ul style="margin: 8px 0 0 0; padding-left: 20px; line-height: 1.6;">
                    <li>Processador Intel Core i3 de 13ª Geração</li>
                    <li>8GB RAM + SSD NVMe de alta velocidade</li>
                    <li>Ecrã antirreflexo de 15.6" polegadas</li>
                    <li>Design fino e leve (Cloud Grey)</li>
                </ul>
            </div>

            <a href="{p2_link}" target="_blank" style="text-decoration: none;">
                <button style="background-color: #ff9900; color: #111; border: none; padding: 18px; border-radius: 12px; cursor: pointer; font-size: 1.1em; font-weight: 800; width: 100%; box-shadow: 0 4px 0 #cc7a00; transition: 0.2s;">
                    VER PREÇO ATUALIZADO ➔
                </button>
            </a>
        </div>

        <footer style="padding-bottom: 30px;">
            <p style="font-size: 0.75em; color: #9ca3af;">© 2026 Soluções Infoprodutos Digitais<br>Ofertas verificadas na Amazon Brasil.</p>
        </footer>

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
