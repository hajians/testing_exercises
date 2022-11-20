import psycopg2
import pandas as pd


def get_table(dbname: str,
              user: str,
              date: str = None) -> pd.DataFrame:
    conn_str = f"dbname={dbname} user={user}"
    query = f"SELECT * FROM MY_TABLE WHERE DATE='{date}'"

    with psycopg2.connect(conn_str) as conn:
        df = pd.read_sql(sql=query, con=conn)

    return df
