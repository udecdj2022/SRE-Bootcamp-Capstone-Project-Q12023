FROM python:3-alpine
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install -r requirements.txt
#CMD ["python", "api.py"]
ENTRYPOINT python api.py
EXPOSE 8000
# Add your instructions to dockerize the application
# App must run on port 8000
