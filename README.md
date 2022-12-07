# MamaAI

# A simple python web application build with FastAPI

## A simple python web application built with FastAPI which takes in two dates as arguments and returns a list of all the objects that would approach earth between the given two dates. 

## Running the application 
1. Clone this repo 
2. Run docker `build -t ImageName` 
3. Run the following command `docker run -p 80:80 ImageName/`
This will run the web app at local host, port 80. 

## Input and output 
The web app takes in two arguments in the format "YYYY-MM-DD". The first is the start date and the latter is the end date. The end date has to be within 7 days of the start date. 
When run succesfully, the output will be a json array of asteroids that will be approaching earth between the given dates sorted by the closest approach distance. 
