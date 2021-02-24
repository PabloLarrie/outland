FROM python:3

ENV PYTHONUNBUFFERED 1

RUN apt-get update 

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]