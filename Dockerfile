FROM python:3
WORKDIR /app
COPY . .
RUN pip install requirements.txt
CMD [ "python","./main.py" ]
