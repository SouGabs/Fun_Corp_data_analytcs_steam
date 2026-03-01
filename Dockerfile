


FROM python:3.11-slim


WORKDIR /app

COPY . .
 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV PORT=10000  # Porta padrão caso rode localmente sem Render

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]
 
 #Imagem base
 #Diretório de trabalho dentro do container
 #Atualiza pip e instala dependências
 #Definindo variáveis de ambiente (opcional)
 #CMD usando a porta dinâmica do Render