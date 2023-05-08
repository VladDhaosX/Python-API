from flask import Blueprint, request, jsonify
from models import station_request

station_requests_blueprint = Blueprint("station_requests", __name__)


@station_requests_blueprint.route("/", methods=["GET"])
def get_station_requests():
    station_requests = station_request.query.all()
    return jsonify([request.to_dict() for request in station_requests])


@station_requests_blueprint.route("/create", methods=["POST"])
def create_station_request():
    data = request.get_json()
    new_request = station_request.create(
        data["request_status_id"],
        data["station_id"],
        data["user_id"]
    )
    return jsonify(new_request.to_dict()), 201
