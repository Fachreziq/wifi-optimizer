from flask import Flask, render_template, request, jsonify
import time

from algorithms.hill_climbing import hill_climbing
from algorithms.simulated_annealing import simulated_annealing
from algorithms.genetic_algorithm import genetic_algorithm

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/optimize", methods=["POST"])
def optimize():

    data = request.get_json()

    width = int(data["width"])
    height = int(data["height"])
    routers = int(data["routers"])
    radius = int(data["radius"])

    algorithm = data["algorithm"]

    start_time = time.time()

    if algorithm == "Hill Climbing":

        result, score = hill_climbing(
            width,
            height,
            routers,
            radius
        )

    elif algorithm == "Simulated Annealing":

        result, score = simulated_annealing(
            width,
            height,
            routers,
            radius
        )

    elif algorithm == "Genetic Algorithm":

        result, score = genetic_algorithm(
            width,
            height,
            routers,
            radius
        )

    else:

        return jsonify({
            "error": "Algoritma tidak valid"
        }), 400

    execution_time = time.time() - start_time

    return jsonify({
        "routers": result,
        "score": round(score, 2),
        "time": round(execution_time, 4),
        "algorithm": algorithm
    })


@app.route("/compare", methods=["POST"])
def compare():

    data = request.get_json()

    width = int(data["width"])
    height = int(data["height"])
    routers = int(data["routers"])
    radius = int(data["radius"])

    results = []

    # Hill Climbing
    start = time.time()

    _, hc_score = hill_climbing(
        width,
        height,
        routers,
        radius
    )

    hc_time = time.time() - start

    results.append({
        "name": "Hill Climbing",
        "score": round(hc_score, 2),
        "time": round(hc_time, 4)
    })

    # Simulated Annealing
    start = time.time()

    _, sa_score = simulated_annealing(
        width,
        height,
        routers,
        radius
    )

    sa_time = time.time() - start

    results.append({
        "name": "Simulated Annealing",
        "score": round(sa_score, 2),
        "time": round(sa_time, 4)
    })

    # Genetic Algorithm
    start = time.time()

    _, ga_score = genetic_algorithm(
        width,
        height,
        routers,
        radius
    )

    ga_time = time.time() - start

    results.append({
        "name": "Genetic Algorithm",
        "score": round(ga_score, 2),
        "time": round(ga_time, 4)
    })

    return jsonify(results)


@app.errorhandler(404)
def not_found(error):

    return jsonify({
        "error": "Halaman tidak ditemukan"
    }), 404


@app.errorhandler(500)
def server_error(error):

    return jsonify({
        "error": "Terjadi kesalahan pada server"
    }), 500


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )