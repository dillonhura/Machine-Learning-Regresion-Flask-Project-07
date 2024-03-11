FROM python:3.10

WORKDIR /app

ADD data /app/data
ADD models /app/models
ADD server /app/server

ADD requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

ENV AWS_ACCESS_KEY_ID=minio
ENV AWS_SECRET_ACCESS_KEY=minio123
ENV MLFLOW_S3_ENDPOINT_URL=http://minio:9000

CMD [ "python", "/app/server/regression.py" ]
