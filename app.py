from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi Página Flask</title>

        <style>
            *{
                margin:0;
                padding:0;
                box-sizing:border-box;
                font-family: Arial, sans-serif;
            }

            body{
                height:100vh;
                display:flex;
                justify-content:center;
                align-items:center;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                overflow:hidden;
            }

            .card{
                background:white;
                padding:40px;
                border-radius:20px;
                text-align:center;
                width:400px;
                box-shadow:0 10px 30px rgba(0,0,0,0.3);
                animation: aparecer 1s ease;
            }

            h1{
                color:#1e3c72;
                margin-bottom:15px;
                font-size:40px;
            }

            p{
                color:#555;
                margin-bottom:25px;
                font-size:18px;
            }

            .btn{
                display:inline-block;
                padding:12px 25px;
                background:#1e3c72;
                color:white;
                text-decoration:none;
                border-radius:10px;
                transition:0.3s;
                font-weight:bold;
            }

            .btn:hover{
                background:#2a5298;
                transform:scale(1.05);
            }

            @keyframes aparecer{
                from{
                    opacity:0;
                    transform:translateY(30px);
                }
                to{
                    opacity:1;
                    transform:translateY(0);
                }
            }
        </style>
    </head>

    <body>

        <div class="card">
            <h1>🔥 Flask App</h1>
            <p>
                Bienvenido a tu página moderna hecha con Python y Flask.
            </p>

            <a href="#" class="btn">Empezar</a>
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)