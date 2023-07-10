FROM python:3.8
LABEL authors="aishwaryadhanawade"

WORKDIR /app

ADD . /app

RUN pip install -r requirement.txt

CMD ["uwsgi", "uwsgi.ini"]
