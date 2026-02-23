from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Soluções Infoprodutos Digitais</title>
            <meta charset="UTF-8">
        </head>
        <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px; background-color: #f4f4f4;">
            <div style="background: white; padding: 40px; border-radius: 15px; display: inline-block; shadow: 0px 4px 10px rgba(0,0,0,0.1);">
                <h1 style="color: #2c3e50;">Soluções Infoprodutos Digitais</h1>
                <p style="font-size: 1.2em; color: #7f8c8d;">Bem-vindo à nossa página oficial de divulgação.</p>
                <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
                <p>Estamos a preparar novidades incríveis para si!</p>
                <button style="background-color: #27ae60; color: white; border: none; padding: 15px 30px; border-radius: 5px; cursor: pointer; font-size: 1em;">
                    Saber Mais
                </button>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
