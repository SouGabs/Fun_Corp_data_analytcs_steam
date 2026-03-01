from sqlalchemy import MetaData, Table, Column, Integer, String, Float, Text

metadata = MetaData()

games = Table(
    "games",
    metadata,
    Column("appid", Integer, primary_key=True),
    Column("name", String),
    Column("release_date", String),
    Column("estimated_owners", String),
    Column("peak_ccu", Integer),
    Column("required_age", Integer),
    Column("price", Float),
    Column("dlc_count", Integer),
    Column("about_the_game", Text),
)