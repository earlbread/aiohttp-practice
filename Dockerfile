FROM python:3.5
MAINTAINER waydi1@gmail.com
RUN apt-get -qqy update
RUN apt-get install -qqy nginx && pip install pipenv
COPY config/aiohttp_practice.nginx /etc/nginx/sites-enabled/aiohttp_practice.conf
COPY . /app
WORKDIR /app
RUN pipenv install
EXPOSE 8080
CMD ./start.sh
