import pymssql
from . import exceptions
import sqlalchemy

class Database:

    def __init__(self, server: str, user: str, password: str, database: str = None, as_dict: bool = True,) -> pymssql.Connection:
        self.server = server
        self.user = user
        self.password = password
        self.database = database
        self.as_dict = as_dict

    def connect(self):
        pass

class MsSQLDatabase(Database):

    def __init__(self, server: str, user: str, password: str, database: str = None, as_dict: bool = True, port: int = 1433) -> pymssql.Connection:
        self._connection = None
        self._cursor = None
        self._pool = None
        super().__init__(server, user, password, database, as_dict)
        self.create_pool()

    def __enter__(self):
        self.connect()
        self.get_cursor()
        return self

    def __exit__(self,exception_type,exception_value,exception_traceback):
        self.close_connection()
    
    def get_connection(self):
        c = pymssql.connect(
            server=self.server,
            user=self.user,
            password=self.password,
            database=self.database,
            as_dict=self.as_dict,
            login_timeout=20,
            timeout=20
        )
        return c

    def connect(self):
        self._connection = self._pool.connect()

    @property
    def connection(self):
        return self._connection
    
    @property
    def connected(self) -> bool:
        try:
            conn = self._pool.connect()
            cursor = conn.cursor()
            cursor.execute('SELECT 1 AS test')
            return True
        except pymssql.Error:
            return False

    @property
    def cursor(self):
        return self._cursor
    
    def get_cursor(self):
        if self._connection is None:
            raise exceptions.ConnectionException
        if self._cursor is None:
            self._cursor = self.connection.cursor()

    def create_pool(self):
        if self._pool is None:
            self._pool = sqlalchemy.pool.QueuePool(self.get_connection, max_overflow=10, pool_size=5)

    @property
    def pool(self):
        return self._pool
   
    def execute(self, query: str):
        if self._cursor is None:
            raise exceptions.CursorException
        try:
            self._cursor.execute(query)
        except Exception as e:
            return e
        else:
            return self.fetchall()
        finally:
            self.close_connection()

    def fetchall(self):
        try:
            res = self._cursor.fetchall()
        except Exception as e:
            return e
        else:
            return res
        return 

    def close_connection(self):
        self._connection.close()


if __name__ == '__main__':
    import os
    db = MsSQLDatabase(
            server = os.getenv('DB_SERVER'),
            port=os.getenv('DB_PORT'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            database = os.getenv('DB_DATABASE'))
    with db as conn:
        records = conn.execute("SELECT * FROM DockerTest.dbo.Person")
    print(records)
