import psycopg2
import pandas as pd

def read_db_proper(
        database: str,
        user: str,
        password: str,
        host: str,
        port: str,
        age: int
):
    with psycopg2.connect(database=database, user=user, password=password, host=host, port=port) as conn:
        df = pd.read_sql("SELECT * FROM PERSONS;", con=conn)

    return df