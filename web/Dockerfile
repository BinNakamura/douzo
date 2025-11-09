FROM python:3.10-slim

WORKDIR /app

# ビルドツールを追加して uWSGI をインストール
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y build-essential python3-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y build-essential python3-dev && apt-get autoremove -y

COPY . .

# uWSGI で UNIX ソケット経由で起動
CMD ["uwsgi", "--socket", "/tmp/uwsgi.sock", "--module", "app:app", "--chmod-socket=666", "--master", "--processes", "4", "--threads", "2"]
