from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Gestor de Tareas</title>
        <style>
            body{
                font-family: Arial, sans-serif;
                background-color: #f4f6f9;
                margin: 0;
                padding: 0;
            }

            .container{
                width: 80%;
                max-width: 800px;
                margin: 50px auto;
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
            }

            h1{
                text-align: center;
                color: #2c3e50;
            }

            p{
                text-align: center;
                color: #7f8c8d;
            }

            ul{
                list-style: none;
                padding: 0;
            }

            li{
                background: #3498db;
                color: white;
                margin: 10px 0;
                padding: 15px;
                border-radius: 10px;
            }

            footer{
                text-align: center;
                margin-top: 20px;
                color: gray;
            }
        </style>
    </head>
    <body>

        <div class="container">

            <h1>📋 Sistema de Gestión de Tareas</h1>

            <p>Proyecto desarrollado con Flask, Docker y GitHub Actions</p>

            <ul>
                <li>✅ Hacer deberes</li>
                <li>✅ Estudiar Python</li>
                <li>⏳ Preparar proyecto CI/CD</li>
                <li>📦 Publicar imagen Docker</li>
            </ul>

            <footer>
                Versión 3.0.0
            </footer>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)