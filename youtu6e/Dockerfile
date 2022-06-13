FROM python
RUN mkdir /code
ADD . /code/
WORKDIR /code
RUN pip3 install -r /code/youtu6e/requirements.txt
COPY scripts/start*.sh /

EXPOSE 8000

CMD ["sh", "/start_prod.sh"]
