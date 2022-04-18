FROM python

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

CMD [ "python", "manage.py", "runserver" ]
