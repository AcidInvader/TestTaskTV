FROM python:3.11-alpine3.15

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=Europe/Moscow \
    LANG=C.UTF-8

RUN apk add --update --no-cache curl postgresql-dev gcc python3-dev musl-dev openssl libffi-dev openssl-dev build-base

RUN pip install --upgrade pip
COPY ./ost/requirements.txt ./ost/entrypoint.sh .
RUN pip install -r requirements.txt

RUN chmod +x /usr/src/app/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]