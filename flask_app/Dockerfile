FROM python:3.7

LABEL Author="Cameron Cooper"
LABEL E-mail="cameron.w.cooper@gmail.com"
LABEL version="0.0.1b"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP flask_app
ENV FLASK_ENV "development"

ADD . /flask_app
WORKDIR /flask_app
RUN pip install -r requirements.txt

WORKDIR ../

EXPOSE 5000
CMD flask run --host=0.0.0.0