from flask import Blueprint, jsonify, request
from database import db
from models import Station

api = Blueprint("api", __name__)


@api.route("/", methods=["GET"])
def get_data():
    stations = Station.query.all()
    data = [
        {
            "Id": station.Id,
            "Station": station.Station,
            "Name": station.Name,
            "StatusId": station.StatusId,
            "CreatedDate": station.CreatedDate,
        }
        for station in stations
    ]

    return jsonify(data)
