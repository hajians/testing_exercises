import os
import unittest

import sqlalchemy
from testcontainers.postgres import PostgresContainer

from testing_exercises.some_reader.read_db_proper import read_db_proper


class TestReaderDB(unittest.TestCase):

    def setUp(self):
        # Start container and populate it.
        self.pg_container = PostgresContainer("postgres:9.5")
        self.postgres = self.pg_container.start()

        create_table_query = """
            CREATE TABLE PERSONS(
                NAME           TEXT    NOT NULL,
                AGE            INT     NOT NULL
            );
        """
        insert_query = """
            INSERT INTO PERSONS(NAME, AGE) VALUES ('{name}', {age});
        """

        e = sqlalchemy.create_engine(self.postgres.get_connection_url())

        e.execute(create_table_query)
        e.execute(insert_query.format(name="Jack", age=20))
        e.execute(insert_query.format(name="S", age=40))

    def tearDown(self) -> None:
        self.postgres.stop()

    @unittest.skipIf(os.environ.get("CI") == 'true', "Skipping this test in github.")
    def test_reader_db(self):
        # Given
        age = 20
        postgres = self.postgres

        # When
        output = read_db_proper(
            database=postgres.POSTGRES_DB,
            user=postgres.POSTGRES_USER,
            password=postgres.POSTGRES_PASSWORD,
            host=postgres.get_container_host_ip(),
            port=postgres.get_exposed_port(postgres.port_to_expose),
            age=age
        )

        # Then
        assert output.shape == (2, 2)
