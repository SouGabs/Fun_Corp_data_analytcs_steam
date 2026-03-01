import requests
import os

URL = "https://brpucrs-my.sharepoint.com/:x:/g/personal/gabriel_brambila_edu_pucrs_br/IQCbZyf1jWiiR4aCipuP1w8iAcxohLRXIFcGnIlxiDmVnv0?e=HHlEYl"
OUTPUT_PATH = "steam_games.csv"

def download():
    if not os.path.exists(OUTPUT_PATH):
        print("Baixando arquivo...")
        r = requests.get(URL, stream=True)
        with open(OUTPUT_PATH, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Download finalizado.")

if __name__ == "__main__":
    download()