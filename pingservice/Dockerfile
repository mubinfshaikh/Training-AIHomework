FROM python:3.6
MAINTAINER Mubin Shaikh
COPY ./home/mubin/pingservice.py /opt/
COPY ./home/mubin/requirements.txt /opt
WORKDIR /opt
RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 5000
CMD ["python", "pingservice.py"]
