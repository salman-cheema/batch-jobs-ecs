FROM ubuntu:16.04
WORKDIR /employee
RUN apt-get update
RUN apt install python3 -y
RUN apt-get install -y python3-pip
RUN apt-get install -y  python3-psycopg2
RUN python3 -m pip install --upgrade pip
RUN pip3 install psycopg2
RUN pip3 install sqlalchemy
RUN pip3 install boto3
RUN pip3 install pandas
COPY . /employee
RUN ls /usr/bin/python*
RUN python3 --version
CMD ["python3", "employee.py"]
