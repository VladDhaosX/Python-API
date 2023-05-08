import pyodbc

def create_conn():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=database-2.cwbt7fw41quf.us-east-2.rds.amazonaws.com,1433;"
        "DATABASE=MoniRail;"
        "UID=Admin;"
        "PWD=Va07an08de33;"
    )
    return conn
