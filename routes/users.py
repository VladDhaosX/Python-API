from flask import Blueprint, request, jsonify
from models import User

users_blueprint = Blueprint("User", __name__)


@users_blueprint.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@users_blueprint.route("/create", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User.create(data["name"])
    return jsonify(new_user.to_dict()), 201
