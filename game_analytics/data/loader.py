import pandas as pd
from game_analytics.core.schema import REQUIRED_COLUMNS
from game_analytics.core.exceptions import MissingColumnError

class CSVLoader:
  """Responsável por carregar e normalizar datasets
  """
  def __init__(self, filepath: str):
    self.filepath = filepath

  def load(self) -> pd.DataFrame:
    df = pd.read_csv(self.filepath)

    self._validate(df)
    df = self._normalize(df)

    return df

  def _validate(self, df: pd.DataFrame):
    
    for col in REQUIRED_COLUMNS:
      if col not in df.columns:
        raise MissingColumnError(f'Coluna obrigatória ausente:{col}')

  def _normalize(self, df:DataFrame) -> pd.DataFrame:
    
    df["Release date"] = pd.to_datetime(df["release date"], errors = "coerce") 
    df["release_year"] = df["Release date"].dt.year
    df["is_free"] = df["price"] == 0

    return df

""" Aqui garantimos que:
Datas foram convertidas
Ano foi extraido
Criamos um flag de gratuito
Por enquanto nenhuma coluna original foi removida
"""