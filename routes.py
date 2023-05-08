from flask import Blueprint, jsonify, request
from database import create_conn

api = Blueprint("api", __name__)

@api.route("/", methods=["GET"])
def get_data():
    conn = create_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dbo.Station")
    results = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]

    data = [dict(zip(column_names, row)) for row in results]

    conn.close()

    return jsonify(data)
