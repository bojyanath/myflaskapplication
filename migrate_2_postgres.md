# MIGRATING FLASK APPLICATION FROM MYSQL TO POSTGRES
### what we have done so far ?

 *  Flask application which connects to MYSQL database
 *  MySql server installed on local
 *  Flask application connecting to local
 *  We have created RDS instance(postgres)


* [ NOTE : For learning purpose we used MYSQL until now, From here onwards we use POSTGRES as our dev database in AWS(Postgresql Most Widely Used) ]

### So we are migrating flask application from MYSQL to POSTGRES:
### Here we trying to :

#### Migrate our flask application to POSTGRES RDS Instance.
  * For this we have to do the following steps :

    - Check RDS instance up and running
    - Establish a connection with following parameters:
       - url      - (endpoint:dev-achievers-01.cdcue0e6sf3u.us-east-1.rds.amazonaws.com)
       - username - (flaskdevl)
       - password - (flaskdevl01)
       - database - (achievers)
    - make changes in code

* [ NOTE : as we are migrating from MYSQL to POSTGRES, change MYSQL part of code to POSTGRES ]

### The changes in code are following :

#### Mention Dependency - "psycopg2" used to Connect To PostgreSQL Database Server Using Python 
       * import psycopg2


#### We should Initialize the Postgres connection 
       * conn = psycopg2.connect(database="achievers",
                                   user="flaskdevl",
                                   password="flaskdevl01",
                                   host="dev-achievers-01.cdcue0e6sf3u.us-east-1.rds.amazonaws.com", port="5432")


#### We should create the postgres connection
       * cur = conn.cursor()


#### In Postgres the tables are located in schemas, so we should mention the relation to call table: 
       * syntax : schema.table_name
       * ex     : dbo.messages


#### To commit every transaction that modifies data for tables  for  we call bellow method  
       * conn.commit()

 
  




