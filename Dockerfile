# 1. 軽量なPythonの環境をベースにする
FROM python:3.11-slim

# 2. コンテナ内の作業フォルダを /app に設定
WORKDIR /app

# 3. あなたのPythonプログラム（app.py）をコンテナ内にコピー
COPY sql-test.py .

# 4. アプリが使うポート（8080）を開放
EXPOSE 8080

# 5. コンテナ起動時にプログラムを実行
CMD ["python", "sql-test.py"]
