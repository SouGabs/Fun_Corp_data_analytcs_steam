import requests
import os

URL = "https://drive.google.com/file/d/1tyHpcXmddtJ12oxBqAkeJmRG2r8B7_w2/view?usp=sharing"
OUTPUT_PATH = "steam.zip"

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