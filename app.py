from flask import Flask, request, jsonify
from Type_Advantage import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/attack", methods=["POST"])
def attack_route():
    data = request.json
    return jsonify({
        "multiplier": attack(data["attackers"], data["defenders"])
    })

@app.route("/coverage", methods=["POST"])
def coverage_route():
    return jsonify(coverage(request.json["moves"]))

@app.route("/defence", methods=["POST"])
def defence_route():
    return jsonify(defence(request.json["types"]))

if __name__ == "__main__":
    app.run()
