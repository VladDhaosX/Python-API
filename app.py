from flask import Flask, jsonify, request
import pyodbc

app = Flask(__name__)
app.config["DEBUG"] = True

def create_conn():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=GECIT;'
        'UID=sa;'
        'PWD=Admin2*;'
    )
    return conn

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = create_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dbo.Drivers")
    results = cursor.fetchall()
    column_names = [column[0] for column in cursor.description]

    data = [dict(zip(column_names, row)) for row in results]

    conn.close()

    return jsonify(data)

if __name__ == "__main__":
    app.run()
