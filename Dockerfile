FROM tiangolo/uwsgi-nginx-flask:flask

WORKDIR app

COPY * /app/app/

# COPY ./app /app
