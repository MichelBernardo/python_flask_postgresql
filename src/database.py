import psycopg2
import psycopg2.pool
from flask import current_app, g


class DatabaseManager:
    def __init__(self):
        self.pool = None

    def init_app(self, app):
        """
            Creates a connections pool when the application is initialized.
        """

        self.pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dsn=app.config['DATABASE_URI']
        )

        # Ensures that connections are closed when the application terminates.
        app.teardown_appcontext(self.close_conn)

    def get_conn(self):
        """
            Obtains a connection from the pool for the current request.
        """

        if 'db_conn' not in g:
            g.db_conn = self.pool.getconn()

        return g.db_conn

    def close_conn(self, e=None):
        """
            Returns the connection to the pool at the end of the request.
        """

        conn = g.pop('db_conn', None)
        if conn is not None:
            self.pool.putconn(conn)


# Global instance that will be imported elsewhere.
db = DatabaseManager()