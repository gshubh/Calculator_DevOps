FROM ubuntu:18.04
RUN apt-get update && apt-get install python3.6
ADD calculator.py /
CMD [ "python", "./calculator.py"]
EXPOSE 8180
