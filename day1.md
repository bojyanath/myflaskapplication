## DAY 1 - Database setup for loca;
1. Started mysql server  using XAMPP.
2. Connected to the server using Dbeaver.
3. Found achiever database missing in mysql server.
```mysql
syntax : show database;
```
4. Create new database as achiever.
 ```mysql
syntax : CREATE DATABASE <DB_NAME>;
 EX : CREATE DATABASE achiever;
```
5. Achiever database is created.
5. Found no tables in achiever.
```mysql
syntax : show tables;
```
6. create new table messages in achiever.

```mysql
Syntax : CREATE TABLE <TABLE_NAME> (COLUMN1 DATATYPE);
Ex : CREATE TABLE messages (message varchar(225));
```