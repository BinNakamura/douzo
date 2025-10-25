# app/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# 必要なパッケージをインストール（libpcre3 系ではなく libpcre2 系を使用）
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpcre2-8-0 \
    libpcre2-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Python パッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリをコピー
COPY . .

# uWSGI を起動
CMD ["uwsgi", "--ini", "app.ini"]
