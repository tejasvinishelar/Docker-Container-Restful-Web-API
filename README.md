#RESTful webservice using Docker

Created a RESTful Web service that displays data of students in JSON format using two get routes: 
   
* /students
   
* /students/studentId
    
Steps to run RESTful web service:

* Create the project with app.py and JSON file in a single folder.
  The templates folder consists of the index.html file which displays the json result on the webpage

* A Docker Image is created by running the following command: -
 "docker build -t students-image:latest ."

* You can check the image created using "docker images". You will find the image students-image under the list.

* Run the created students-image image inside a container using the following command
  "docker run -d -p 5000:5000 --name students-container students-image" 

* Check running docker container by "docker ps"

* App will now be running at the following address: -
  http://192.168.99.100:5000/students
  
* For specific Id use the following url
  http://192.168.99.100:5000/students/111 --- 111 is the id you wish to search
