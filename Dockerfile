FROM python:3
ADD calculator.py /
CMD [ "python3", "./calculator.py", "-p 8180"]
  
