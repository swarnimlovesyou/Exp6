from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Name: Swarnim Jambhrunkar</h1>
    <h2>AppID: 2409789</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)