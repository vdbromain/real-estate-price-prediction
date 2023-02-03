#Importing an image from dockerhub to create my own image
FROM python:3.10
#Defining the work directory for the docker's container
WORKDIR /app
#Copy the requirements.txt file in the work directory
COPY requirements.txt .
#Launch the pip upgrading
RUN python -m pip install --upgrade pip
#Launch the installation of the requirements listed in the requirements.txt
RUN pip install -r requirements.txt
#Copy everything from the local directory to the work directory
COPY . .
#Defining the port 5000 as the port Docker must use
EXPOSE 5000
#Launch the python file app.py
CMD ["python", "app.py"]

#docker build -t predict-app . #Creating the docker's image
#docker run -t -i -p 5000:5000 predict-app #Creating the docker's container from the image