import psycopg2
from psycopg2 import pool

# --- Option 1: Kết nối đơn giản (dành cho app nhỏ) ---
def get_db_connection():
    """
    Create and return a new PostgreSQL database connection.
    Update these parameters with your actual database credentials.
    """
    return psycopg2.connect(
        host="localhost",
        database="Tasks",
        user="nghiavu",
        password="123456"
    )

# --- Option 2: Connection Pool (hiệu quả hơn cho app lớn) ---
# db_pool = psycopg2.pool.SimpleConnectionPool(
#     1, 10,
#     host="localhost",
#     database="Tasks",
#     user="nghiavu",
#     password="123456"
# )

# def get_db_connection():
#     return db_pool.getconn()

# def release_db_connection(conn):
#     db_pool.putconn(conn)