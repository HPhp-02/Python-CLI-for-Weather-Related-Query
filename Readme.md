# Setting up of Environment
First run the Table_script.sql in your sql server so that necessary table get formed<br>

Run following code in command line of the editor<br>

``` bash
  pip install pymysql
  pip install requests
  pip install sqlite3
  pip install time
```

In the code enter your API key and for URL OpenWeather API is already written<br>

# Datadase Schema
## First
There is a Table in your main database in the Table_script<br>
It create table with schema User , Password<br>
## Second
Every Time when user register there is a table formed in your connected database<br>
The schema of this database is Timestamp,Location and Weather is store logs of the user<br>

# How to run
First enter username and password and database for your SQL server<br>
Then Register and Login<br>
After You can either see Weather or your previous logs<br>
















