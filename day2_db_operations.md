** DAY-2 DB OPERATIONS

1. Connected to Database from Dbeaver.
2. Created new table " achievers_day 2" with column name & int in "achievers" database.
```mysql
SYNTAX: CREATE TABLE DB_name.table_name(colums1,column2);
EX    : CREATE TABLE achievers.achiever_day2(name varchar(10),age int(20));
```
3.Next inserted records using below records.
```mysql
SYNTAX: INSERT INTO TABLE_NAME(column1,column2)values('value1','value2');
EX    : INSERT INTO achievers_day2(name,age)VALUES('nani','27'),('bob','28'),('prem','30');
```
4.Displayed all records by running select query.
```mysql
SYNTAX: SELECT * FROM table_name;
EX    : SELECT * FROM achievers_day2;
````
