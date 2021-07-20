
FROM python:3.9-slim

WORKDIR /usr/app

COPY flaskr .

RUN apt update && pip3 install --no-cache-dir -r ./requirements.txt \
  && rm -rf /var/lib/apt/lists/*

# CMD ["sleep", "infinity"]
CMD ["python3", "views.py"]
