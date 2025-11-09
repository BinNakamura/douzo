FROM python:3.10-slim

WORKDIR /app

# ビルドツールと依存ライブラリを追加
RUN apt-get update && \
    apt-get install -y build-essential python3-dev libexpat1 && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uwsgi", "--socket", "/tmp/uwsgi.sock", "--module", "app:app", "--chmod-socket=666", "--master", "--processes", "4", "--threads", "2"]
