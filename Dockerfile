FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

RUN python manage.py collectstatic --noinput

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
