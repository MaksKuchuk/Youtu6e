FROM python
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
COPY scripts/start*.sh /
ADD . /code/

EXPOSE 8000

CMD ["sh", "/start_prod.sh"]
