from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    amazon_link = "https://a.co"
    image_url = "https://m.media-amazon.com/images/I/71T1e2NG20L._AC_SY355_.jpg"
    preco_produto = "R$ 1.199,00"

    html = f"""
    <html>
    <head>
        <title>Oferta: PC Completo i3</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>

    <body style="font-family:sans-serif;text-align:center;background:#f4f4f4;padding:20px">

        <div style="background:white;padding:30px;border-radius:15px;
        margin:auto;max-width:450px;box-shadow:0 4px 15px rgba(0,0,0,0.1)">

            <div style="background:#e74c3c;color:white;padding:5px 10px;
            border-radius:5px;font-size:12px;font-weight:bold;display:inline-block">
            🔥 OFERTA DO DIA
            </div>

            <h2>🖥️ PC Completo Intel i3 + Monitor 20"</h2>

            <img src="{image_url}" style="width:100%;max-height:280px;
            object-fit:contain;border-radius:10px">

            <p style="margin-top:15px;color:#777">Esta oferta expira em</p>

            <div id="timer" style="font-size:30px;font-weight:bold;color:#e67e22">
            00:00:00
            </div>

            <div style="background:#fff9e6;padding:15px;border-radius:10px;margin-top:15px">

                <span style="text-decoration:line-through;color:#888">
                De: R$ 1.499,00
                </span>

                <br>

                <span style="font-size:28px;color:#27ae60;font-weight:bold">
                {preco_produto}
                </span>

            </div>

            <p>
            Ideal para <b>Home Office</b> e <b>Estudos</b>
            </p>

            <a href="{amazon_link}" target="_blank">
            <button style="background:#ff9900;border:none;padding:18px;
            width:100%;font-size:18px;font-weight:bold;border-radius:8px;cursor:pointer">
            QUERO COMPRAR NA AMAZON
            </button>
            </a>

        </div>

<script>

function startTimer(){{

const now = new Date();
const end = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 23,59,59);

function update(){{

const diff = end - new Date();

if(diff <= 0){{
document.getElementById("timer").innerHTML="00:00:00";
return;
}}

const h = Math.floor(diff/3600000);
const m = Math.floor((diff%3600000)/60000);
const s = Math.floor((diff%60000)/1000);

document.getElementById("timer").innerHTML =
(h<10?"0"+h:h)+":"+(m<10?"0"+m:m)+":"+(s<10?"0"+s:s);

}}

update();
setInterval(update,1000);

}}

startTimer();

</script>

    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run(debug=True)
