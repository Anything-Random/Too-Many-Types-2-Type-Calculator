from flask import Flask, request, jsonify, render_template
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

@app.route("/team-coverage", methods=["POST"])
def team_coverage_route():
    data = request.json
    pokemons = data.get("pokemons", [])

    results = {
        "individual": [],
        "total": None
    }

    # Calculate each active pokemon
    for moves in pokemons:
        if moves:
            results["individual"].append(coverage(moves))
        else:
            results["individual"].append(None)

    # Calculate the full team if there's at least one move
    active_pokes = [p for p in pokemons if p]
    if active_pokes:
        results["total"] = team_coverage(active_pokes)

    return jsonify(results)

@app.route("/defence", methods=["POST"])
def defence_route():
    return jsonify(defence(request.json["types"]))

@app.route("/pokemon-list", methods=["GET"])
def pokemon_list_route():
    return jsonify(get_all_pokemon_names())

@app.route("/get-types", methods=["POST"])
def get_types_route():
    pokemon_name = request.json.get("pokemon")
    types = pokemon_to_types(pokemon_name)
    return jsonify({"types": types})

if __name__ == "__main__":
    app.run()