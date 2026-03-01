class DatasetError(Exception):
  """Erros relacionados ao carregamento ou estruturas do dataset"""
  pass
class MissingColumnError(DatasetError):
  """Erro de quando uma coluna obrigatória não existe"""
  pass