FROM python:3.6
MAINTAINER Mubin Shaikh
COPY ./home/mubin/Training-AIHomework/receiverservice/receiverservice.py /opt/
COPY ./home/mubin/Training-AIHomework/receiverservice/requirements.txt /opt
WORKDIR /opt
RUN pip3 --no-cache-dir install -r requirements.txt
EXPOSE 5000
CMD ["python", "receiverservice.py"]
