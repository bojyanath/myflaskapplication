# Externalize application configuration using environment variables.
* We have to change the details in the code using environment variable.
* Where environment variable are key-value pairs that contain data that can be used by processes running inside a Docker container.
* Using set command export the Environment Variables.
  * Linux
    * In linux we use "EXPORT" to declare the environment variable.
  * Command prompt
    * In Command prompt we use "SET" to declare the environment variable.
  * Docker
    * In Docker we use "ENV" to declare the environment variable.
* declare inside thr docker image which runs in the container.
 - declare the values
   - ENV DB_USER="flaskdevl"
   - ENV DB_USEWR_PSWD="flaskdevl01"
   - ENV DB_HOST="dev-achievers-01.cdcue0e6sf3u.us-east-1.rds.amazonaws.com"

* run the application.