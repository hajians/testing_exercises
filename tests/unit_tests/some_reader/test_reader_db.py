import pytest

from testing_exercises.some_reader.read_db import get_table


def create_test_pg_table():
    return None, None


@pytest.mark.skip(reason="This test is for presentation.")
def test_get_table():
    # Given
    # Create a Postgres Table and return dbname and user
    dbname, user = create_test_pg_table()
    date = "2022-11-25"

    # When
    df = get_table(dbname=dbname, user=user, date=date)

    # Then verify what you need to test
    assert True