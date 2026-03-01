from sqlalchemy import text
from app.database import engine

def get_top_expensive(limit=5):
    query = text("""
        SELECT name, price
        FROM games
        ORDER BY price DESC
        LIMIT :limit
    """)

    with engine.connect() as conn:
        result = conn.execute(query, {"limit": limit}).fetchall()

    return result


def get_free_games(limit=10):
    query = text("""
        SELECT name
        FROM games
        WHERE price = 0
        LIMIT :limit
    """)

    with engine.connect() as conn:
        result = conn.execute(query, {"limit": limit}).fetchall()

    return result