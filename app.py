from flask import Flask, jsonify, request
import pyodbc

app = Flask(__name__)
app.config["DEBUG"] = True

def create_conn():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=database-2.cwbt7fw41quf.us-east-2.rds.amazonaws.com,1433;'
        'DATABASE=MoniRail;'
        'UID=Admin;'
        'PWD=Va07an08de33;'
    )
    return conn

@app.route('/', methods=['GET'])
def get_data():
    conn = create_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dbo.Station")
    results = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]

    data = [dict(zip(column_names, row)) for row in results]

    conn.close()

    return jsonify(data)

if __name__ == "__main__":
    app.run()
