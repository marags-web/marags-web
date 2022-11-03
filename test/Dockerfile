FROM python:3.8-slim-buster
RUN pip3 install flask
RUN pip3 install requests
COPY . /app
WORKDIR /app
EXPOSE 5000:5000
CMD python3 sample-rest.py
