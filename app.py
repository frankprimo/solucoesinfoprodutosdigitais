from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # --- CONFIGURAÇÕES DO PRODUTO ---
    amazon_link = "https://a.co/d/0cXXjFpC" 
    
    # NOVO LINK DE IMAGEM (MAIS COMPATÍVEL)
    image_url = "https://m.media-amazon.com"

    return f"""
    <html>
    <head>
        <title>PC Completo i3 - Soluções Infoprodutos</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="font-family: sans-serif; text-align: center; padding: 20px; background-color: #f4f4f4; margin: 0;">
        <div style="background: white; padding: 30px; border-radius: 15px; display: block; margin: 10px auto; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); max-width: 450px; text-align: left;">
            <h1 style="color: #2c3e50; font-size: 1.3em; margin-bottom: 15px; text-align: center;">🖥️ PC Completo Intel i3 + Monitor 20"</h1>
            
            <div style="text-align: center;">
                <!-- Link da imagem com parâmetro de segurança -->
                <img src="{image_url}" alt="Computador Completo" style="width: 100%; max-height: 300px; object-fit: contain; border-radius: 10px; margin-bottom: 20px;">
            </div>

            <p style="font-size: 0.9em; color: #34495e; line-height: 1.6;">
                Ideal para <b>Home Office</b> e <b>Estudos</b>. Equipado com SSD para inicialização ultrarrápida e Wi-Fi incluso.
            </p>
            <ul style="font-size: 0.85em; color: #7f8c8d; padding-left: 20px;">
                <li>✅ Windows 10 Pro Instalado</li>
                <li>✅ Teclado e Mouse Inclusos</li>
                <li>✅ Monitor LED de Alta Definição</li>
            </ul>
            <div style="text-align: center; margin-top: 25px;">
                <a href="{amazon_link}" target="_blank" style="text-decoration: none;">
                    <button style="background-color: #ff9900; color: #111; border: none; padding: 18px; border-radius: 8px; cursor: pointer; font-size: 1.1em; font-weight: bold; width: 100%; box-shadow: 0px 4px 0px #cc7a00;">
                        VER PRODUTO NA AMAZON ➔
                    </button>
                </a>
                <p style="margin-top: 30px; font-size: 0.7em; color: #bdc3c7;">
                    © 2026 Soluções Infoprodutos Digitais | Oferta verificada na Amazon.br
                </p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
