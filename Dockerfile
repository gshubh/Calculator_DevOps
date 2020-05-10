FROM ubuntu:18.04
RUN apt-get update && \
    apt-get install -y wget bash zip rsync python3-venv python3-dev build-essential
ADD calculator.py /
CMD [ "python", "./calculator.py"]
EXPOSE 8180
