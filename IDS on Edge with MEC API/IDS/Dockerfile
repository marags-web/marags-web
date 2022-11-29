FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt
COPY . /app
#EXPOSE 2000
CMD python3 ids_multi.py
