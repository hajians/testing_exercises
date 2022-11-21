from unittest import mock
import pandas as pd
from testing_exercises.some_reader.read_db import get_table


def create_test_pg_table():
    return None, None


@mock.patch("testing_exercises.some_reader.read_db.pd.read_sql")
@mock.patch("testing_exercises.some_reader.read_db.psycopg2")
def test_get_table(psycopg2_mock, read_sql_mock):
    # Given
    # Create a Postgres Table and return dbname and user
    dbname, user = create_test_pg_table()
    read_sql_mock.return_value = pd.DataFrame()
    date = "2022-11-25"

    # When
    df = get_table(dbname=dbname, user=user, date=date)

    # Then verify what you need to test
    assert isinstance(df, pd.DataFrame)
