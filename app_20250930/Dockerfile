# Python の軽量イメージをベースにする
FROM python:3.11-slim

# 作業ディレクトリを作成
WORKDIR /app

# Python 実行時の環境変数
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリ本体とHTML/CSS/JSをコピー
COPY . .

# Flask が待ち受けるポート (Back4App と一致させる)
EXPOSE 5000/tcp

# Gunicorn で app.py の "app" を起動
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
