FROM python:3.8.5-alpine
COPY ./ /app
WORKDIR /app
RUN ls -a
RUN pip3 install -r requirements.txt
CMD [ "gunicorn", "--bind", "0.0.0.0:80", "wsgi:app" ]
