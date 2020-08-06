from tkinter import *
from tkinter import messagebox
from database import Database

class Quiz:

    def __init__(self):

        self.db=Database()
        
        self.load_login_window()

    def load_login_window(self):

        self._root = Tk()

        self._root.title("QUIZ Login")
        self._root.minsize(400, 800)
        self._root.maxsize(1600, 900)
        self._root.config(background="#000000")

        self._label1 = Label(self._root, text="KBC", fg="#fff", bg="#000000")
        self._label1.config(font=("Arial", 30))
        self._label1.pack(pady=(30, 30))

        self._username = Label(self._root, text="Username", fg="#fff", bg="#000000")
        self._username.config(font=("Times", 16))
        self._username.pack(pady=(10, 10))

        self._usernameInput = Entry(self._root)
        self._usernameInput.pack(pady=(5, 25), ipady=10, ipadx=30)

        self._password = Label(self._root, text="Password", fg="#fff", bg="#000000")
        self._password.config(font=("Times", 16))
        self._password.pack(pady=(10, 10))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(5, 25), ipady=10, ipadx=30)

        self._login = Button(self._root, text="Login", bg="#fff", width=25, height=2,
                             command=lambda: self.check_login())
        self._login.pack()

        self._reg = Button(self._root, text="Sign Up", bg="#fff", width=25, height=2,
                             command=lambda: self.regWindow())
        self._reg.pack(pady=(10,10))

        self._root.mainloop()

    def check_login(self):
        username=self._usernameInput.get()
        password=self._passwordInput.get()

        data=self.db.check_login(username,password)

        
        if len(data)==0:
            
            messagebox.showerror("Error","Invalid Credentials")
        else:
            self.user_id=data[0][0]
            self.is_logged_in=1
            self.login_handler()

    def regWindow(self):

        self.clear()

        self._name = Label(self._root, text="Name", fg="#fff", bg="#000000")
        self._name.config(font=("Times", 16))
        self._name.pack(pady=(5, 5))

        self._nameInput = Entry(self._root)
        self._nameInput.pack(pady=(5, 5), ipady=10, ipadx=20)

        self._username = Label(self._root, text="Username", fg="#fff", bg="#000000")
        self._username.config(font=("Times", 16))
        self._username.pack(pady=(5, 5))

        self._usernameInput = Entry(self._root)
        self._usernameInput.pack(pady=(5, 5), ipady=10, ipadx=20)

        self._password = Label(self._root, text="Password", fg="#fff", bg="#000000")
        self._password.config(font=("Times", 16))
        self._password.pack(pady=(5, 5))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(5, 5), ipady=10, ipadx=20)

        
        self._reg = Button(self._root, text="Sign Up", bg="#fff", width=25, height=2, command=lambda: self.reg_handler())
        
        self._reg.pack(pady=(10,10))

    def reg_handler(self):

        flag=self.db.register(self._nameInput.get(),self._usernameInput.get(),self._passwordInput.get())

        if flag==1:
            
            messagebox.showinfo("Success","Registered Successfully. Login to proceed")
            self._root.destroy()
            self.load_login_window()
        else:
            messagebox.showerror("Error","Try again!")
                

    def mainWindow(self,data,flag=0,index=0):
        
        # Display info about the user
        if flag==1:
            name = "Name: " + str(data[index][1])
            username = "Username: " + str(data[index][2])
            score = "Score: " + str(data[index][4])

            name_label = Label(self._root, text=name, fg="#fff", bg="#000000")
            name_label.config(font=("Arial", 16))
            name_label.pack(pady=(20, 10))

            username_label = Label(self._root, text=username, fg="#fff", bg="#000000")
            username_label.config(font=("Arial", 16))
            username_label.pack(pady=(5, 10))

            score_label = Label(self._root, text=score, fg="#fff", bg="#000000")
            score_label.config(font=("Arial", 16))
            score_label.pack(pady=(5, 10))

        else:
            name = "Name: " + str(data[index][1])
            username = "Username: " + str(data[index][2])
            score = "Score: " + str(data[index][4])

            name_label = Label(self._root, text=name, fg="#fff", bg="#000000")
            name_label.config(font=("Arial", 16))
            name_label.pack(pady=(20, 10))

            username_label = Label(self._root, text=username, fg="#fff", bg="#000000")
            username_label.config(font=("Arial", 16))
            username_label.pack(pady=(5, 10))

            score_label = Label(self._root, text=score, fg="#fff", bg="#000000")
            score_label.config(font=("Arial", 16))
            score_label.pack(pady=(5, 10))

            self._start = Button(self._root, text="Start Quiz", bg="#fff", width=25, height=2, command=lambda: self.start_quiz())
        
            self._start.pack(pady=(10,10))

    def start_quiz(self):
        data = self.db.fetch_userdata(self.user_id)
        update=1
        self.db.participated(update,self.user_id)
        self.load_question1()

    def load_question1(self):

        self.clear()

        self._q1 = Label(self._root, text="Which of these movies does not feature Tom Hanks?", fg="#fff", bg="#000000")
        self._q1.config(font=("Times", 16))
        self._q1.pack(pady=(10, 10))

        self._a1 = Button(self._root, text="a) Big", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question2())
        self._a1.pack(pady=(10,10))
        self._a2 = Button(self._root, text="b) Forrest Gump", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question2())        
        self._a2.pack(pady=(10,10))
        self._a3 = Button(self._root, text="c) You've Got Mail", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question2())
        self._a3.pack(pady=(10,10))
        self._a4 = Button(self._root, text="d) The Prestige", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question2(flag=1))
        self._a4.pack(pady=(10,10))

    def load_question2(self,flag=0):

        self.clear()

        self._q2 = Label(self._root, text="In the Avengers movie, what is the name of Thor's hammer?", fg="#fff", bg="#000000")
        self._q2.config(font=("Times", 16))
        self._q2.pack(pady=(10, 10))

        self._a1 = Button(self._root, text="a) Glock 26", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question3())
        self._a1.pack(pady=(10,10))
        self._a2 = Button(self._root, text="b) Mjölnir", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question3(flag=1))
        self._a2.pack(pady=(10,10))
        self._a3 = Button(self._root, text="c) Batarang", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question3())
        self._a3.pack(pady=(10,10))
        self._a4 = Button(self._root, text="d) Gungnir", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question3())
        self._a4.pack(pady=(10,10))
        if flag==1:
            self.db.update_score(self.user_id,flag=1)
        
    def load_question3(self,flag=0):

        self.clear()

        self._q3 = Label(self._root, text="What was the name of the jewel Cal gave to Rose in The 'Titanic' ? ", fg="#fff", bg="#000000")
        self._q3.config(font=("Times", 16))
        self._q3.pack(pady=(10, 10))

        self._a1 = Button(self._root, text="a) Blood Diamond", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question4())
        self._a1.pack(pady=(10,10))
        self._a2 = Button(self._root, text="b) Isadora", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question4())
        self._a2.pack(pady=(10,10))
        self._a3 = Button(self._root, text="c) Heart Of The Ocean", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question4(flag=1))
        self._a3.pack(pady=(10,10))
        self._a4 = Button(self._root, text="d) Omega Seamaster", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question4())
        self._a4.pack(pady=(10,10))
        if flag==1:
            self.db.update_score(self.user_id,flag=1)

    def load_question4(self,flag=0):

        self.clear()

        self._q4 = Label(self._root, text="What is the first foreign language film ever to win Academy Award for Best Picture?", fg="#fff", bg="#000000")
        self._q4.config(font=("Times", 16))
        self._q4.pack(pady=(10, 10))

        self._a1 = Button(self._root, text="a) Parasite", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question5(flag=1))
        self._a1.pack(pady=(10,10))
        self._a2 = Button(self._root, text="b) Roma", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question5())
        self._a2.pack(pady=(10,10))
        self._a3 = Button(self._root, text="c) Amour", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question5())
        self._a3.pack(pady=(10,10))
        self._a4 = Button(self._root, text="d) The Postman", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question5())
        self._a4.pack(pady=(10,10))
        if flag==1:
            self.db.update_score(self.user_id,flag=1)

    def load_question5(self,flag=0):

        self.clear()

        self._q5 = Label(self._root, text="For which 1964 musical blockbuster did Julie Andrews win Academy Award for Best Actress?", fg="#fff", bg="#000000")
        self._q5.config(font=("Times", 16))
        self._q5.pack(pady=(10, 10))

        self._a1 = Button(self._root, text="a) Sound of Music", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question6())
        self._a1.pack(pady=(10,10))
        self._a2 = Button(self._root, text="b) Mary Poppins", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question6(flag=1))
        self._a2.pack(pady=(10,10))
        self._a3 = Button(self._root, text="c) Star!", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question6())
        self._a3.pack(pady=(10,10))
        self._a4 = Button(self._root, text="d) Darling Lili", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question6())
        self._a4.pack(pady=(10,10))
        if flag==1:
            self.db.update_score(self.user_id,flag=1)

    def load_question6(self,flag=0):

        self.clear()

        self._q6 = Label(self._root, text="What island is Jurassic Park on?", fg="#fff", bg="#000000")
        self._q6.config(font=("Times", 16))
        self._q6.pack(pady=(10, 10))

        self._a1 = Button(self._root, text="a) Isla Nublar", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question7(flag=1))
        self._a1.pack(pady=(10,10))
        self._a2 = Button(self._root, text=" b) Isla Sorna", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question7())
        self._a2.pack(pady=(10,10))
        self._a3 = Button(self._root, text="c) Isla Tacano", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question7())
        self._a3.pack(pady=(10,10))
        self._a4 = Button(self._root, text="d) Isla Matanceros", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question7())
        self._a4.pack(pady=(10,10))
        if flag==1:
            self.db.update_score(self.user_id,flag=1)

    def load_question7(self,flag=0):

        self.clear()

        self._q7 = Label(self._root, text="The movies Pet Semetary and IT are based on books written by which author?", fg="#fff", bg="#000000")
        self._q7.config(font=("Times", 16))
        self._q7.pack(pady=(10, 10))

        self._a1 = Button(self._root, text="a) JK Rowling", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question8())
        self._a1.pack(pady=(10,10))
        self._a2 = Button(self._root, text="b) Nicholas Sparks", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question8())
        self._a2.pack(pady=(10,10))
        self._a3 = Button(self._root, text="c) Gillian Flynn", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question8())
        self._a3.pack(pady=(10,10))
        self._a4 = Button(self._root, text="d) Stephen King", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question8(flag=1))
        self._a4.pack(pady=(10,10))
        if flag==1:
            self.db.update_score(self.user_id,flag=1)
        
    def load_question8(self,flag=0):

        self.clear()

        self._q8 = Label(self._root, text="Kevin McAllister is a character from which movie series?", fg="#fff", bg="#000000")
        self._q8.config(font=("Times", 16))
        self._q8.pack(pady=(10, 10))

        self._a1 = Button(self._root, text="a) Spiderman", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question9())
        self._a1.pack(pady=(10,10))
        self._a2 = Button(self._root, text="b) Toy Story", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question9())
        self._a2.pack(pady=(10,10))
        self._a3 = Button(self._root, text="c) Home Alone", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question9(flag=1))
        self._a3.pack(pady=(10,10))
        self._a4 = Button(self._root, text="d) Ice Age", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question9())
        self._a4.pack(pady=(10,10))
        if flag==1:
            self.db.update_score(self.user_id,flag=1)
        
    def load_question9(self,flag=0):

        self.clear()

        self._q9 = Label(self._root, text="Who played the role of Mrs. Doubtfire?", fg="#fff", bg="#000000")
        self._q9.config(font=("Times", 16))
        self._q9.pack(pady=(10, 10))

        self._a1 = Button(self._root, text="a) John Travolta", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question10())
        self._a1.pack(pady=(10,10))
        self._a2 = Button(self._root, text="b) Robin Williams", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question10(flag=1))
        self._a2.pack(pady=(10,10))
        self._a3 = Button(self._root, text="c) Robert De Niro", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question10())
        self._a3.pack(pady=(10,10))
        self._a4 = Button(self._root, text="d) Pierce Brosnan", bg="#fff", width=25, height=2,
                             command=lambda: self.load_question10())
        self._a4.pack(pady=(10,10))
        if flag==1:
            self.db.update_score(self.user_id,flag=1)

    def load_question10(self,flag=0):

        self.clear()

        self._q10 = Label(self._root, text="In The Lion King, what is the name of Simba's evil uncle?", fg="#fff", bg="#000000")
        self._q10.config(font=("Times", 16))
        self._q10.pack(pady=(10, 10))

        self._a1 = Button(self._root, text="a) Scar", bg="#fff", width=25, height=2,
                             command=lambda: self.end_quiz(flag=1))
        self._a1.pack(pady=(10,10))
        self._a2 = Button(self._root, text="b) Jafar", bg="#fff", width=25, height=2,
                             command=lambda: self.end_quiz())
        self._a2.pack(pady=(10,10))
        self._a3 = Button(self._root, text="c) Shere Khan", bg="#fff", width=25, height=2,
                             command=lambda: self.end_quiz())
        self._a3.pack(pady=(10,10))
        self._a4 = Button(self._root, text="d) Gaston", bg="#fff", width=25, height=2,
                             command=lambda: self.end_quiz())
        self._a4.pack(pady=(10,10))
        if flag==1:
            self.db.update_score(self.user_id,flag=1)

    def end_quiz(self,flag=0):
        self.clear()
        if flag==1:
            self.db.update_score(self.user_id,flag=1)
        data = self.db.fetch_userdata(self.user_id)
        score = int(data[0][4] // 10)
        result ="Your " + str(score) + "/10 questions were correct"
        self._p = Label(self._root, text="Thanks for participating!!", fg="#fff", bg="#000000")
        self._p.config(font=("Times", 16))
        self._p.pack(pady=(5, 5))
        self._p = Label(self._root, text=result, fg="#fff", bg="#000000")
        self._p.config(font=("Times", 16))
        self._p.pack(pady=(5, 5))
        self._p = Label(self._root, text="Click on EXIT", fg="#fff", bg="#000000")
        self._p.config(font=("Times", 16))
        self._p.pack(pady=(5, 5))
        self._exit = Button(self._root, text="Exit", bg="#fff", width=25, height=2, command=lambda: self.logout())
        
        self._exit.pack(pady=(10,10))
        
        

    def view_scores(self):
        self.clear()
        data = self.db.leaderboard()
      
        for index in range (0,5):
            
            rank = str(data[index][1])+ "        " + str(data[index][4])

            rank_label = Label(self._root, text=rank, fg="#fff", bg="#000000")
            rank_label.config(font=("Arial", 16))
            rank_label.pack(pady=(20, 10))



    def login_handler(self):
      
        self.clear()
        self.headerMenu()
        data = self.db.fetch_userdata(self.user_id)
        if data[0][5]==1:
            flag=1
        else:
            flag=0
        self.mainWindow(data,flag)


    def clear(self):
        for i in self._root.pack_slaves():
            print(i.destroy())

    
    def logout(self):
        self.is_logged_in=0
        self._root.destroy()
        self.load_login_window()

    def headerMenu(self):
        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile", command=lambda: self.login_handler())
        filemenu.add_command(label="Edit Profile", command=lambda: self.edit_profile())
        filemenu.add_command(label="View Leaderboard", command=lambda: self.view_scores())
        filemenu.add_command(label="LogOut", command=lambda : self.logout())

    def edit_profile(self):

        # fetch data
        data=self.db.fetch_userdata(self.user_id)

        self.clear()

        self._username = Label(self._root, text="Username", fg="#fff", bg="#000000")
        self._username.config(font=("Times", 16))
        self._username.pack(pady=(5, 5))

        self._usernameInput = Entry(self._root)
        self._usernameInput.insert(0, data[0][2])
        self._usernameInput.pack(pady=(5, 5), ipady=10, ipadx=20)

        self._password = Label(self._root, text="Password", fg="#fff", bg="#000000")
        self._password.config(font=("Times", 16))
        self._password.pack(pady=(5, 5))

        self._passwordInput = Entry(self._root)
        self._passwordInput.insert(0, data[0][3])
        self._passwordInput.pack(pady=(5, 5), ipady=10, ipadx=20)        

        self.save=Button(self._root, text="Update Info", command=lambda: self.update_info())
        self.save.pack(pady=(5,5))

    def update_info(self):

        flag=self.db.update_profile(self._usernameInput.get(),self._passwordInput.get(),self.user_id)

        if flag==1:
            messagebox.showinfo("Success","Profile Updated")
        else:
            messagebox.showerror("Error","Try Again!")
            

obj=Quiz()

