FROM python:3.8-slim-buster
RUN pip3 install pyzmq
COPY . /app
WORKDIR /app
EXPOSE 2000
CMD python3 sub.py

