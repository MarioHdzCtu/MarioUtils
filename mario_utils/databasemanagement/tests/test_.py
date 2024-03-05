import pytest
import src
import os
import pymssql

def test_db_error():
    with pytest.raises(pymssql._pymssql.OperationalError):
        db = src.MsSQLDatabase(
            server = os.getenv('DB_SERVER'),
            port=os.getenv('DB_PORT'),
            user = os.getenv('DB_USER_ERROR'),
            password = os.getenv('DB_PASSWORD_ERROR'),
            database = os.getenv('DB_DATABASE'))
        with db as conn:
            res = conn.execute('SELECT * FROM DockerTest.dbo.Person')
            
def test_db_success():
    db = src.MsSQLDatabase(
            server = os.getenv('DB_SERVER'),
            port=os.getenv('DB_PORT'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            database = os.getenv('DB_DATABASE'))
    assert db.connected