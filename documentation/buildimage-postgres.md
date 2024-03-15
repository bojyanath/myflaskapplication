# Build docker image with Postgres changes and run in a container.

### the process is same as the below attached file and add couple of changes to it as mentioned below.
       [ https://github.com/bojyanath/myflaskapplication/blob/fa02d47b36f1d602ac09f45df4344222aaaf2992/day6-run-docker.md ]

  * add the dependencies need to install for postgres
     * (RUN pip intall psycopg2-binary)
  * in dockerfile and updated python code(postgres).

### create a new docker image.
     * docker build -t my-flask-app .


### run container
     * docker run -p 5000:5000 --name my-flask-container my-flask-app
