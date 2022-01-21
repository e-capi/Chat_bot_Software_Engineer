from Chat_bot_Software_Engineer.SQL.SQL_tools import conn
import sqlite3

def test_sql_connection():
    assert isinstance(conn,sqlite3.Connection)
