import mysql.connector

conn=mysql.connector.connect(host="127.0.0.1", user="root", password="", database="quizapp")

mycursor=conn.cursor()

#Lines to create Database. No longer needed
#mycursor.execute("CREATE DATABASE quizapp")
#conn.commit()



#Creating table
#user_id - Int --> Primary Key --> Not Null -- Auto_Increment
#name - Varchar -- Not Null
#username - Varchar -- Not Null
#password - Varchar -- Not Null
#score - Int -- Not NULL
#participated - Int -- Not NULL


#Creating Users
mycursor.execute("CREATE TABLE users (user_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,name VARCHAR(255) NOT NULL,username VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL,score INT NOT NULL,participated INT NOT NULL)")
conn.commit()
