### docker setup

* Install docker engine using 'docker desktop'.
* Verify docker installation is completed .
    ```doctest
    docker --version
    ```
* Create a dockerfile.
* create a file name 'dockerfile' in the project. write the following in dockerfile for docker image
  * base image 
  * working directory 
  * mention the required packages and dependencies
  * copy rest of the code(copy . .)
  * and 
  * mention the entry point 


* To build my docker image.
    ```doctest
    docker build -t my_flask-app
    ```
* To verify my docker image.
    ```doctest
    docker image ls
    ```
* To run container with docker image.
    ```doctest
    docker run -p 5000:5000 --name my-flask-container my-flask-app
    ```
  
* After succesfully running the web page should display

note : as in the above case unfortunately localhost and and contrainer which is running docker image has diff IP-ADDRESS
      so changes in code:
   Configure MySQL from environment variables
   ```python
      app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'host.docker.internal')
   ```
   So above changes are "host.docker.internal" is replaced in the place of "local host".