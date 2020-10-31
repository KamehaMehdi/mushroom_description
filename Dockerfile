FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt --use-feature=2020-resolver

CMD [ "python", "app.py"]
