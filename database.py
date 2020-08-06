import mysql.connector

class Database:

    def __init__(self):
        # connect to the database
        try:
            self._conn=mysql.connector.connect(host="127.0.0.1", user="root", password="", database="quizapp")
            self._mycursor=self._conn.cursor()
        except:
            print("Could not connect to database")
            exit()

    def check_login(self, username, password):

        # Perform login
        self._mycursor.execute(
            "SELECT * FROM users WHERE username LIKE '{}' AND password LIKE '{}'".format(username, password))
        data = self._mycursor.fetchall()

        return data

    def participated(self,update,user_id):

        self._mycursor.execute("UPDATE users SET participated={} WHERE user_id='{}'".format(update,user_id))
        self._conn.commit()

    def fetch_userdata(self, user_id):

        self._mycursor.execute("SELECT * FROM users WHERE user_id LIKE {}".format(user_id))
        data = self._mycursor.fetchall()

        return data

    
    def update_profile(self,username,password,user_id):
        try:
            self._mycursor.execute("UPDATE users SET username='{}', password='{}' WHERE user_id='{}'".format(username,password,user_id))
            self._conn.commit()
            return 1
        except:
            return 0

    def register(self,name,username,password):
        try:
            self._mycursor.execute("""INSERT INTO users(user_id,name,username,password) VALUES(NULL, '{}','{}','{}')""".format(name,username,password))
            self._conn.commit()
            return 1
        except:
            return 0

    def leaderboard(self):
            self._mycursor.execute("SELECT * FROM users ORDER BY score DESC")
            data = self._mycursor.fetchall()
            return data

    def update_score(self,user_id,flag=0):
            if flag==1:
                self._mycursor.execute("UPDATE users SET score=score+10 WHERE user_id='{}'".format(user_id))
                self._conn.commit()



