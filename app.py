from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>ALAyHiWA</title>
        <style>
            body {
                background: #080816;
                color: #00ffff;
                font-family: Arial;
                text-align: center;
                padding-top: 100px;
            }
            h1 { font-size: 50px; }
            p { color: white; }
        </style>
    </head>
    <body>
        <h1>ALAyHiWA</h1>
        <p>Welcome to my website!</p>
        <p>Our social world starts here.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
