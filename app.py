from flask import Flask, request, jsonify
from Type_Advantage import *

app = Flask(__name__)

@app.route("/attack", methods=["POST"])
def attack_route():
    data = request.json
    result = attack(data["attackers"], data["defenders"])
    return jsonify({"multiplier": result})

@app.route("/coverage", methods=["POST"])
def coverage_route():
    data = request.json
    result = coverage(data["moves"])
    return jsonify(result)

@app.route("/defence", methods=["POST"])
def defence_route():
    data = request.json
    result = defence(data["types"])
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
