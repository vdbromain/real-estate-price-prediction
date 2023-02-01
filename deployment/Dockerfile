#Importing the image we need
#FROM python:3.10.1
#Run the updates of the packages
#RUN pip install --upgrade pip
#Create the directory /app in the container
#WORKDIR /app
#Put the files in the app directory in the container
#COPY . /app.py
#RUN pip --no-cache-dir install -r requirements.txt
#COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt
#Run the python3 command to open app.py in the container
#CMD ["python","app.py"]

#Philippe
#FROM python:3.10.1
#RUN mkdir /app
#COPY requirements.txt /app
#COPY . /app
#WORKDIR /app 
#RUN ls -la /app/*
#RUN python -m pip install --upgrade pip
#RUN pip3 install -r requirements.txt
#EXPOSE 5000
#CMD ["python3", "app.py", "--host=0.0.0.0"]

#Maïté
#FROM python:3.10.1
#WORKDIR /app
#COPY requirements.txt  .
#RUN pip install --upgrade pip &&\
#    pip install --no-cache-dir -r requirements.txt
#COPY .  .
#EXPOSE 5000
#CMD ["python3", "app.py", "--host=0.0.0.0"]

#Heloïse
FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]

#docker build -t predict-app .
#docker run -t -i -p 5000:5000 predict-app