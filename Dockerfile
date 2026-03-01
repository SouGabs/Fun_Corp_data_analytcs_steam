FROM python:3.11-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
 
 #Imagem base
 #Diretório de trabalho dentro do container
 #Atualiza pip e instala dependências
 #Definindo variáveis de ambiente (opcional)
 #CMD usando a porta dinâmica do Render