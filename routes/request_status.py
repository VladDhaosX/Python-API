from flask import Blueprint, request, jsonify
from models import request_status

request_status_blueprint = Blueprint("request_status", __name__)


@request_status_blueprint.route("/", methods=["GET"])
def get_request_status():
    request_status = request_status.query.all()
    return jsonify([status.to_dict() for status in request_status])


@request_status_blueprint.route("/create", methods=["POST"])
def create_request_status():
    data = request.get_json()
    new_status = request_status.create(data["status_key"], data["name"])
    return jsonify(new_status.to_dict()), 201
