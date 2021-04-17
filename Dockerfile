FROM alpine:latest
MAINTAINER jsvazic@gmail.com
FROM python:3.7

COPY . /app/

RUN pip install --upgrade pip && \
    pip3 install -r /app/requirements.txt

WORKDIR /app/Tiredful_API/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
