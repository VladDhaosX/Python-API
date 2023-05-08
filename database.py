from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "mssql+pyodbc://Admin:Va07an08de33@database-2.cwbt7fw41quf.us-east-2.rds.amazonaws.com:1433/MoniRail?driver=ODBC+Driver+17+for+SQL+Server"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
