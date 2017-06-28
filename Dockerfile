FROM tiangolo/uwsgi-nginx-flask:flask

# WORKDIR app
#
# COPY * /app/app/

EXPOSE 80

COPY ./app /app
