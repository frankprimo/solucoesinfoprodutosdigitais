from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # --- CONFIGURAÇÕES DO PRODUTO ---
    # Seu link de afiliado Amazon
    amazon_link = "https://a.co" 
    
    # LINK DA IMAGEM ATUALIZADO (LINK DIRETO DA AMAZON)
    image_url = "https://m.media-amazon.com/images/I/71T1e2NG20L._AC_SY355_.jpg"
    
    # VALOR DO PRODUTO
    preco_produto = "R$ 1.199,00"

    return f"""
    <html>
    <head>
        <title>Oferta: PC Completo i3 - Soluções Infoprodutos</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body style="font-family: sans-serif; text-align: center; padding: 20px; background-color: #f4f4f4; margin: 0;">
        <div style="background: white; padding: 30px; border-radius: 15px; display: block; margin: 10px auto; box-shadow: 0px 4px 15px rgba(0,0,0,0.1); max-width: 450px; text-align: left;">
            
            <div style="background: #e74c3c; color: white; padding: 5px 10px; border-radius: 5px; font-size: 0.8em; font-weight: bold; display: inline-block; margin-bottom: 10px;">🔥 OFERTA DO DIA</div>
            
            <h1 style="color: #2c3e50; font-size: 1.3em; margin-bottom: 15px; text-align: center;">🖥️ PC Completo Intel i3 + Monitor 20"</h1>
            
            <div style="text-align: center;">
                <img src="{image_url}" alt="Computador Completo" style="width: 100%; max-height: 280px; object-fit: contain; border-radius: 10px; margin-bottom: 15px;">
            </div>

            <div style="text-align: center; margin-bottom: 20px; background: #fff9e6; padding: 15px; border-radius: 10px; border: 1px dashed #ff9900;">
                <span style="font-size: 0.9em; color: #7f8c8d; text-decoration: line-through;">De: R$ 1.499,00</span><br>
                <span style="font-size: 1.8em; font-weight: 800; color: #27ae60;">Por apenas {preco_produto}</span><br>
                <span style="font-size: 0.8em; color: #34495e;">em até 10x sem juros na Amazon</span>
            </div>

            <p style="font-size: 0.9em; color: #34495e; line-height: 1.6;">
                Ideal para <b>Home Office</b> e <b>Estudos</b>. Sistema pronto para uso com SSD e Wi-Fi.
            </p>
            
            <ul style="font-size: 0.85em; color: #7f8c8d; padding-left: 20px; margin-bottom: 25px;">
                <li>✅ Windows 10 Pro Instalado</li>
                <li>✅ Teclado e Mouse Inclusos</li>
                <li>✅ Monitor LED de Alta Definição</li>
            </ul>

            <div style="text-align: center;">
                <a href="{amazon_link}" target="_blank" style="text-decoration: none;">
                    <button style="background-color: #ff9900; color: #111; border: none; padding: 20px; border-radius: 8px; cursor: pointer; font-size: 1.2em; font-weight: bold; width: 100%; box-shadow: 0px 4px 0px #cc7a00;">
                        QUERO COMPRAR NA AMAZON ➔
                    </button>
                </a>
                <p style="margin-top: 25px; font-size: 0.7em; color: #bdc3c7;">
                    © 2026 Soluções Infoprodutos Digitais | Preço verificado na Amazon.br
                </p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
