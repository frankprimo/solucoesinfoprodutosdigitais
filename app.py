from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    busca = request.args.get("q", "").lower()

    produtos = [

        {"nome":"PC Completo Intel i3","categoria":"Computador","avaliacao":"⭐⭐⭐⭐☆","imagem":"https://m.media-amazon.com/images/I/71T1e2NG20L._AC_SY355_.jpg","preco":"Só na AMAZON","processador":"Intel Core i3","memoria":"8GB RAM","armazenamento":"SSD 240GB","sistema":"Windows 10","link":"https://amzn.to/40mOIdP"},

        {"nome":"Notebook Lenovo IdeaPad","categoria":"Notebook","avaliacao":"⭐⭐⭐⭐⭐","imagem":"https://m.media-amazon.com/images/I/71uv+p19nTL._AC_SY355_.jpg","preco":"Só na AMAZON","processador":"Intel Core i5","memoria":"8GB RAM","armazenamento":"SSD 256GB","tela":"15.6 Full HD","sistema":"Windows 11","link":"https://amzn.to/4lnhLb1"},

        {"nome":"Monitor LG 24","categoria":"Monitor","avaliacao":"⭐⭐⭐⭐☆","imagem":"https://m.media-amazon.com/images/I/61hxA0+MEWL._AC_SY355_.jpg","preco":"Só na AMAZON","tela":"24 polegadas","resolucao":"1920x1080","taxa":"75Hz","conexao":"HDMI / VGA","link":"https://amzn.to/4sCIVwN"},

        {"nome":"Mouse Gamer Logitech G305","categoria":"Periférico","avaliacao":"⭐⭐⭐⭐⭐","imagem":"https://m.media-amazon.com/images/I/51sg9BLSMTL._AC_SY355_.jpg","preco":"Só na AMAZON","dpi":"12000 DPI","botoes":"6 programáveis","bateria":"até 250 horas","conexao":"LIGHTSPEED sem fio","link":"https://amzn.to/4uidzx0"},

        {"nome":"Teclado Gamer Redragon Kumara","categoria":"Periférico","avaliacao":"⭐⭐⭐⭐⭐","imagem":"https://m.media-amazon.com/images/I/61Z9sR8i1lL._AC_SY355_.jpg","preco":"Só na AMAZON","switch":"Outemu Blue","iluminacao":"LED Vermelho","conexao":"USB","link":"https://amzn.to/exemplo1"},

        {"nome":"Headset Gamer HyperX Cloud Stinger","categoria":"Áudio","avaliacao":"⭐⭐⭐⭐⭐","imagem":"https://m.media-amazon.com/images/I/61iYJk3E6sL._AC_SY355_.jpg","preco":"Só na AMAZON","driver":"50mm","microfone":"Com cancelamento","conexao":"P2","link":"https://amzn.to/exemplo2"},

        {"nome":"SSD Kingston 480GB","categoria":"Armazenamento","avaliacao":"⭐⭐⭐⭐⭐","imagem":"https://m.media-amazon.com/images/I/61nvsBnH7CL._AC_SX450_.jpg","preco":"Só na AMAZON","capacidade":"480GB","velocidade":"500MB/s","interface":"SATA","link":"https://amzn.to/3NAEXWE"},

        {"nome":"Memória RAM 16GB Corsair","categoria":"Memória","avaliacao":"⭐⭐⭐⭐⭐","imagem":"https://m.media-amazon.com/images/I/61a7pZ4K0XL._AC_SY355_.jpg","preco":"Só na AMAZON","capacidade":"16GB","frequencia":"3200MHz","tipo":"DDR4","link":"https://amzn.to/4sOo4qA"},

        {"nome":"Webcam Logitech C920","categoria":"Acessório","avaliacao":"⭐⭐⭐⭐⭐","imagem":"https://m.media-amazon.com/images/I/61-6uAf8soL._AC_SY355_.jpg","preco":"Só na AMAZON","resolucao":"Full HD 1080p","microfone":"Duplo integrado","conexao":"USB","link":"https://amzn.to/4lzwXls"},

        {"nome":"Cadeira Gamer ThunderX3","categoria":"Gamer","avaliacao":"⭐⭐⭐⭐☆","imagem":"https://m.media-amazon.com/images/I/71VqjPlOJAL._AC_SY355_.jpg","preco":"Só na AMAZON","material":"Couro sintético","ajuste":"Altura e inclinação","suporte":"até 120kg","link":"https://amzn.to/4su2rw1"}

    ]

    filtrados = []

    for p in produtos:
        if busca:
            if busca not in p["nome"].lower() and busca not in p["categoria"].lower():
                continue
        filtrados.append(p)

    return render_template("index.html", produtos=filtrados, busca=busca)


# ✅ ROTA DE TESTE
@app.route("/teste")
def teste():
    return "OK FUNCIONANDO"


# ✅ EXECUÇÃO
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
