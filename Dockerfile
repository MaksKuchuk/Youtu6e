FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED 1
WORKDIR /youtu6e
COPY requirements.txt /youtu6e/
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt
COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]
ADD . /youtu6e/