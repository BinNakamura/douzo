FROM python:3.11-slim

# 作業ディレクトリ
WORKDIR /web

# 必要パッケージ
RUN apt-get update && apt-get install -y build-essential gcc libpcre3-dev libssl-dev && rm -rf /var/lib/apt/lists/*

# requirements.txt を使う場合
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# 最小構成では Flask + uWSGI
RUN pip install --no-cache-dir flask uwsgi

# アプリケーションコピー
COPY ./ ./

# uWSGI 起動コマンド
CMD ["uwsgi", "--ini", "app.ini"]
