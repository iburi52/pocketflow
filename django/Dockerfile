# The build image
FROM python:3.8-slim as builder

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /
RUN pip install --upgrade pip \
 && pip install -r /requirements.txt


# The production image
FROM python:3.8-slim

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

RUN mkdir /code
WORKDIR /code
COPY . /code/

EXPOSE 8080