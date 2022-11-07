FROM python:3.8-slim-buster
RUN pip3 install flask
RUN pip3 install requests
COPY . /app
WORKDIR /app
EXPOSE Service simple-webapp-flask
EXPOSE 8080:5000
CMD python3 test.py
