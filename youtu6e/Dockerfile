FROM python
RUN mkdir /code
ADD . /code/
WORKDIR /code
RUN pip install -r /code/requirements.txt
COPY scripts/start*.sh /

EXPOSE 8000

CMD ["sh", "/start_prod.sh"]
