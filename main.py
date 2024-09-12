import pymysql
import requests
import sqlite3
import time
from datetime import datetime

user = input("username for the Database\n")
password =input("Password for the Database\n")
database = input("Input your Database name\n")

API="your_api_key"

def log(user1):
   mydb = pymysql.connect(host='localhost', user=user, password=password,database=database)
   mycursor=mydb.cursor()
   query = f"SELECT timestamp, location, weather FROM {user1};"
   mycursor.execute(query)
   result = mycursor.fetchall()
   # if len(mycursor)==0:
   #    print("No Logs")
   #    return
   print("Your Logs")
   for i in result:
    print(f"Timestamp :{i[0]} Location : {i[1]} Weather : {i[2]}")


def search(user1):
          mydb = pymysql.connect(host='localhost', user=user, password=password,database=database)
          mycursor=mydb.cursor()
          location=input("Please enter a location for weather\n");
          import requests

# Replace with your actual API key
          api_key = API
          city = f"{location}"
          url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Making the GET request
          response = requests.get(url)
         #  print(response.json());
# Checking if the request was successful
          if response.status_code == 200:
           weather_data = response.json()
           print(f"Weather in {city}:\n")
           print(f"Temperature: {weather_data['main']['temp']}°C\n")
           print(f"Weather: {weather_data['weather'][0]['description']}\n")
           print(f"humidity: {weather_data['main']['humidity']}\n")
           print(f"Wind Speed : {weather_data['wind']['speed']}\n")
           weather = f"Temperature: {weather_data['main']['temp']}°C"+" "+f"Weather: {weather_data['weather'][0]['description']}"+" "+f"humidity: {weather_data['main']['humidity']}"+" "+f"Wind Speed : {weather_data['wind']['speed']}"
           timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
           sql = f"INSERT INTO {user1} (timestamp,location,weather) VALUES (%s, %s,%s)"
           mycursor.execute(sql, (timestamp,city,weather))
           mydb.commit()
          else:
           print(f"Failed to retrieve data:{response.status_code}")


def login():
   _user=input("Enter your Username\n")
   _password=input("Enter your Password\n") 
   
   mydb = pymysql.connect(host='localhost', user=user, password=password,database=database)
   
   mycursor=mydb.cursor()

   mycursor.execute("Select * from users")
    
   result=mycursor.fetchall()
   flag=0
   ind=result[0]
   for row in result:
      if row[0]==_user and row[1]==_password:
        ind=row
        flag=1
        break;
   
   if flag==1:
      while True :
         what_to_check=input('Want to check Weather write : "Weather" or want to your Weather Logs write:"Logs"\n').lower()
         if what_to_check=='weather':
           search(_user)
         elif what_to_check=="logs":
            log(_user)
         else : 
            print("Wrong Choice")
            continue
         want_to_search=input('Do you want to search more write "YES" or "NO" ').lower()
         if want_to_search == "no":
            return
   else :
      print("Please Register")
   mydb.commit()
   
   mycursor.close()
   mydb.close()

def register():
 try:
   user1=input("Enter your Username\n")
   _password=input("Enter your Password\n")

   mydb = pymysql.connect(host='localhost', user='root', password='Harshit@12345',database=database)
   
   mycursor=mydb.cursor()
   m1=mydb.cursor()
   mycursor.execute("Select user from users")
    
   result=mycursor.fetchall()
   flag=1
   for row in result:
      if row[0]==user1:
         print("Username already Existed")
         flag=0
   if flag==1:
    sql = "INSERT INTO users (user, pass) VALUES (%s, %s)"
    mycursor.execute(sql, (user1, _password))

    print("You have Succesfully Registered")
    TableName =f"CREATE TABLE {user1} (timestamp VARCHAR(255) NOT NULL,location VARCHAR(255) NOT NULL,Weather VARCHAR(1000) NOT NULL);"
    m1.execute(TableName)

   mydb.commit()
   
   mycursor.close()
   mydb.close()
 except pymysql.err.OperationalError as e:
    if "Unknown database" in str(e):
        print(f"Error: The database '{database}' does not exist.")
    else:
        print(f"OperationalError: {e}")
  
   
   

   



print("Welcome to this Weather CLI")
while True:
 choice = input("Press 1 for Register and 2 for Login 3 for closing app \n")
 
 if choice == '1':
    register()
 elif choice == '2':
    login()
 elif choice=='3':
    print("Thanks for visiting")
    break
 else:
    print("wrong choice")
 continue;


  

