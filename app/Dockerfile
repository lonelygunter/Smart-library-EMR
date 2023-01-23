FROM python:3.10

WORKDIR /usr/src/app

COPY . .

RUN pip install flask
RUN pip install pymongo

EXPOSE 5050

CMD ["python", "app.py"]

