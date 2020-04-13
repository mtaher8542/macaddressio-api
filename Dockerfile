#publicly available docker image "python" on docker hub will be pulled

FROM python:3.7

MAINTAINER Mohammed Taher "mtaher786@gmail.com"

#creating directory /home/macaddressio in container (linux machine)

RUN mkdir /home/macaddressio

RUN pip install --upgrade pip && \
    pip install requests

#copy files from local directory to container's macaddressio folder

COPY macaddressapi.py /home/macaddressio/macaddressapi.py
COPY find_companyname.py /home/macaddressio/find_companyname.py

#running macaddressapi.py in container

CMD python /home/macaddressio/macaddressapi.py 44:38:39:ff:ef:57
