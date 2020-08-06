import mysql.connector

conn=mysql.connector.connect(host="127.0.0.1", user="root", password="", database="tinder")

mycursor=conn.cursor()

#Lines to create Database. No longer needed
#mycursor.execute("CREATE DATABASE tinder")
#conn.commit()



#Step 2 Create a table
#user_id - Int --> Primary Key --> Not Null -- Auto_Increment
#name - Varchar -- Not Null
#email - Varchar -- Not Null
#password - Varchar -- Not Null


#Creating Table
mycursor.execute("CREATE TABLE proposals (proposal_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,romeo INT NOT NULL,juliet INT NOT NULL)")
conn.commit()


#Create
#mycursor.execute("INSERT INTO users (user_id, name, email, password) VALUES (NULL, 'Rohit Sharma', 'rohit@gmail.com', '23456')")
#conn.commit()


#Retrieve
#mycursor.execute("SELECT * FROM users")
#data=mycursor.fetchall()
#print(data)

#for i in data:
 #   print(i[1],i[-1])

#mycursor.execute("SELECT * FROM users WHERE user_id<2")
#data=mycursor.fetchall()
#print(data)

#mycursor.execute("SELECT * FROM users WHERE email LIKE 'rohit@gmail.com'")
#data=mycursor.fetchall()
#print(data)


#Update
#mycursor.execute("UPDATE users SET password='virat' WHERE user_id=1")
#conn.commit()

#mycursor.execute("UPDATE users SET password='00000'")
#conn.commit()

#Delete
#mycursor.execute("DELETE FROM users WHERE user_id=2")
#conn.commit()
