FROM  redhat/ubi8

RUN yum install python3 -y

RUN pip3 install flask

COPY dev.py  /dev.py

CMD [ "python3" , "/dev.py" ]
