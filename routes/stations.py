from flask import Blueprint, request, jsonify
from models import station

stations_blueprint = Blueprint("stations", __name__)


@stations_blueprint.route("/", methods=["GET"])
def get_stations():
    stations = station.query.all()
    return jsonify([station.to_dict() for station in stations])


@stations_blueprint.route("/create", methods=["POST"])
def create_station():
    data = request.get_json()
    new_station = station.create(
        data["station"], data["name"], data["status_id"]
    )
    return jsonify(new_station.to_dict()), 201
