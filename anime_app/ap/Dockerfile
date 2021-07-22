
FROM python:3.9-slim

WORKDIR /usr/app

# 変更の可能性があるものは個別にCOPYするべし
COPY flaskr .

RUN apt update && pip3 install --no-cache-dir -r ./requirements.txt \
  && rm -rf /var/lib/apt/lists/*

# CMDは一回しか実行されない
# CMD ["sleep", "infinity"]
CMD ["python3", "views.py"]

