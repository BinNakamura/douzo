FROM python:3.11-slim

# 必要なビルドツールをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libssl-dev \
    libpcre2-dev \
 && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリ
WORKDIR /app

# アプリをコピー
COPY . /app

# FlaskとuWSGIをインストール
RUN pip install --no-cache-dir flask uwsgi

# uWSGIを起動
CMD ["uwsgi", "--ini", "app.ini"]
