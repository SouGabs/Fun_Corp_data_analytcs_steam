import requests
import os

URL = "https://huggingface.co/datasets/GabrielABS/meu-dataset-api/resolve/main/steam_games.csv"
OUTPUT_PATH = "steam_games.csv"

def download():
    if not os.path.exists(OUTPUT_PATH):
        print("Baixando arquivo...")
        
        r = requests.get(URL, stream=True)
        r.raise_for_status()
        
        with open(OUTPUT_PATH, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print("Download finalizado.")
    else: 
        print("Arquivo já existe")

if __name__ == "__main__":
    download()