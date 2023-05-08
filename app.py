from flask import Flask, redirect
from database import init_db
from routes.stations import stations_blueprint
from routes.users import users_blueprint
from routes.request_status import request_status_blueprint
from routes.station_requests import station_requests_blueprint

app = Flask(__name__)
init_db(app)

app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def index():
    return redirect("/api")


app.register_blueprint(stations_blueprint, url_prefix="/api/stations")
app.register_blueprint(users_blueprint, url_prefix="/api/users")
app.register_blueprint(request_status_blueprint, url_prefix="/api/request-status")
app.register_blueprint(station_requests_blueprint, url_prefix="/api/station-requests")

if __name__ == "__main__":
    app.run()
