FROM python:3.11-slim

WORKDIR /app

# uWSGI のビルドに必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    gcc \
    libpcre3-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Pythonモジュールインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコピー
COPY . .

# uWSGI 起動
CMD ["uwsgi", "--ini", "app.ini"]
