# Importing module 
import mysql.connector
import datetime

#Importing internal functions
from functions import ca
from functions import wd

# Creating connection object
db = mysql.connector.connect(user='root',database='Bank',password='12345678', port=3306)

cursor = db.cursor() 


s=int(input("We welcome you to Bank-O-Bank's online portal\nEnter- 1 to create account|2 to view account|3 to deposit|4 to withdraw"))

if s==1:
    ca()

if s==4:
    wd()

db.commit()
db.close()