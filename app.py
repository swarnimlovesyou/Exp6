from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Name: Swarnim Jambhrunkar</h1>
    <h2>AppID: 12345</h2>
    <h3>Hobbies: AI/ML, Football, Reading</h3>
    """

if __name__ == "__main__":
    print("Flask app loaded successfully")