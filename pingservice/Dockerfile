FROM python:3.6.9
COPY . /codebase
WORKDIR /codebase
RUN pip install -r requirements.txt
EXPOSE  5000
CMD ["python", "pingservice.py"]
