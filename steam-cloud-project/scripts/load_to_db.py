import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

CSV_PATH = "steam.csv"

def load():
    for chunk in pd.read_csv(CSV_PATH, chunksize=50000):
        chunk = chunk.rename(columns={
            "AppID": "appid",
            "Name": "name",
            "Release date": "release_date",
            "Estimated owners": "estimated_owners",
            "Peak CCU": "peak_ccu",
            "Required age": "required_age",
            "Price": "price",
            "DLC count": "dlc_count",
            "About the game": "about_the_game"
        })

        chunk.to_sql("games", engine, if_exists="append", index=False)

    print("Carga concluída.")

if __name__ == "__main__":
    load()