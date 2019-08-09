FROM python:3.6.9-stretch
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir /src
RUN mkdir /static
WORKDIR /src

ADD ./src /src
RUN pip install --upgrade pip
RUN pip install -r requirements.pip
CMD python manage.py collectstatic --no-input;python manage.py migrate; gunicorn skeleton.wsgi -b 0.0.0.0:8000 & celery worker -A skeleton.celery
