FROM ubuntu:18.04
RUN apt-get update
ADD calculator.py /
CMD [ "python3", "./calculator.py"]
EXPOSE 8180
