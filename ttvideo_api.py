from flask import Flask, jsonify, request
from db_utils import fetch_all_affiliates, fetch_videos_by_country, fetch_earnings, add_video, fetch_available_countries

app = Flask(__name__)

@app.route("/affiliates", methods=["GET"])
def get_all_affiliates():
    return jsonify(fetch_all_affiliates())

@app.route("/countries", methods=["GET"])
def get_available_countries():
    return jsonify(fetch_available_countries())

@app.route("/videos/<country>", methods=["GET"])
def get_videos_by_country(country):
    return jsonify(fetch_videos_by_country(country))

@app.route("/earnings", methods=["GET"])
def get_earnings():
    return jsonify(fetch_earnings())

@app.route("/videos/add", methods=["POST"])
def add_new_video():
    new_video = request.get_json()
    result = add_video(new_video)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
