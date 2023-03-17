FROM python:3.9

USER root
WORKDIR /app
COPY app/ /app

RUN apt-get update \
    && pip3 install --no-cache-dir -r requirements.txt

CMD ["python","-u","main.py"]
