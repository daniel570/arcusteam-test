FROM python:latest

COPY . /opt/clonex/app

WORKDIR /opt/clonex/app

RUN pip install flask mysql-connector-python flask-cors

RUN apt update; apt install at -y

ENTRYPOINT ["python"]

CMD ["app.py"]
