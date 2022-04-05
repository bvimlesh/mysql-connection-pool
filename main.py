from mysql.connector import pooling

class SQLPool(object):
    db_pool = None
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SQLPool, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def create_pool(cls, pool_name="dbpool", pool_size=10):
        con_pool = pooling.MySQLConnectionPool(
            pool_name=pool_name,
            pool_size=pool_size,
            pool_reset_session=True,
            **{
            "host": "*",
            "port": "*",
            "user": "*",
            "password": "*"
        })
        return con_pool

    @classmethod
    def pool(cls):
        if cls.db_pool is None:
            cls.db_pool = cls.create_pool(cls)
            print("sql pool creation done")
        return cls.db_pool

    def close(cls, conn, cursor):
        cursor.close()
        conn.close()