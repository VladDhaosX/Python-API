from flask import Flask, jsonify, request, redirect
from routes import api

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def index():
    return redirect("/api")

app.register_blueprint(api, url_prefix="/api")

if __name__ == "__main__":
    app.run()
