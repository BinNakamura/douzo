FROM python:3.11-slim

WORKDIR /web

# 基本ツールとビルド依存をインストール
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Flask と uWSGI をインストール
RUN pip install --no-cache-dir flask uwsgi

COPY . .

CMD ["uwsgi", "--ini", "app.ini"]
