FROM python:3.8-slim-buster
RUN pip3 install requests
COPY . /app
WORKDIR /app
#EXPOSE 8000
RUN chmod 777 subscribe.json
CMD python3 httpreq.py
