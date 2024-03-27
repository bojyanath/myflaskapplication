# Create a docker image with simple hello world python program.

* Step 1 : created a python file "hello.py"
    * code in hello.py
```python # (This program prints Hello, world! )
print ('Hello,this is a test to my Python and docker knowledge')
```
* Step 2 : created a docker file with all the commands a user could call on the command line to assemble an image.
```dockerfile
#base image
FROM python:3.9-slim
#working directory in  container
WORKDIR /app
#Copy the rest of the application code
COPY . .
#entry point to run application
CMD ["python", "hello.py"]
```   
     
* Step 3 : Build a docker image with below docker command.
```dockerfile ( below "my_docker_image" is image tagname)
   docker build -t my_docker_image .
```
* Step 4 : final step run the container where we want to run our image.
```dockerfile ("my_python_container" is container name)
docker run -p 5000:5000 --name my_python_container new_docker_image
``` 
* our output is displayed in the terminal as " Hello,this is a test to my Python and docker knowledge "