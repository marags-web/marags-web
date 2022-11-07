FROM python:3.8-slim-buster
RUN pip3 install requests
COPY . /app
WORKDIR /app
#EXPOSE 8000
CMD python3 httpreq.py
