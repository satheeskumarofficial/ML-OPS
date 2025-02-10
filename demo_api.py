from flask import Flask

app = Flask(__name__)

@app.route("/hello",methods = ["GET"])
def hello():
    return "<h1> hello AI!!! </h1>"


@app.route("/",methods = ["GET"])
def message():
    return {"message" :"why are you ping me?"}