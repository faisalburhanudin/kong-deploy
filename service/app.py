from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({
        "message": "Hello world"
    })


app.run(host="0.0.0.0", port="5000")
