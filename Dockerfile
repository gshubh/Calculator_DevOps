FROM python:3
ADD calculator.py /
CMD [ "python", "./calculator.py" ]
