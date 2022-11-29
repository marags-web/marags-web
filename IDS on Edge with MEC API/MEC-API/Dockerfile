FROM python:3.8-slim-buster
RUN pip3 install flask
RUN pip3 install requests
COPY . /app
WORKDIR /app
RUN chmod 777 subscribe.json
EXPOSE Service mec-api-latest 
EXPOSE 8080:5000
CMD python3 mec-api.py
