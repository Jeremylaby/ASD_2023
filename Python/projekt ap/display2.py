import tkinter as tk
from tkinter import ttk
import json
class login_App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-topmost',1)
        self.title("Siłka loguj się")
        self.geometry("500x300")
        #self.iconbitmap('Hero_Jeremy.ico')
        self.resizable(False,False)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=3)
        self.create_widgets()
    def __init2__(self):
        self.title("Siłka loguj się")
        self.geometry("500x300")
        self.iconbitmap('Hero_Jeremy.ico')
        self.resizable(False,False)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=3)
        self.create_widgets()
    def create_widgets(self):
        self.login=tk.StringVar()
        self.login_label=ttk.Label(self,text="Podaj Login: ",font=('Arial',15))
        self.login_label.grid(column=0,row=0,padx=5,pady=10)
        self.login_entry=ttk.Entry(self,width=20,font=('Arial',10),textvariable=self.login)
        self.login_entry.grid(column=1,row=0,padx=5,pady=10,sticky='W')
        self.password=ttk.Entry(self)
        self.login_button=ttk.Button(self,text="Zaloguj",command=self.check_login)
        self.login_button.grid(column=1,row=1,sticky='w',padx=5,pady=10)
    def No(self):
        self.frame.grid_forget()
        self.__init2__()
    def get_current_value(self):
        return '{: .2f}'.format(self.current_value.get())

    def add_user(self):
        login=self.login.get()
        Imie=self.imie_entry.get()
        Nazwisko=self.nazwisko_entry.get()
        Email=self.email_entry.get()
        waga=self.waga_entry.get()
        password1=self.password1_entry.get()
        password2=self.password2_entry.get()
        informations=[Imie,Nazwisko,Email,waga]
        for information in informations:
            if " " in information:return
            if len(information)==0: return
        for i in range(10):
            if str(i) in Imie:
                print("zle imie")
                return
            if str(i) in Nazwisko:
                print("zle nazwisko")
                return
        if  "@gmail.com" != Email[-10:]:
            print("zly email")
            return
        if len(password1)<6:
            print("za krótkie hasło")
            return
        if password1!=password2:
            print("nie to haslo")
            return    
        try:
            waga=float(waga)
        except ValueError:
            print("zla waga")
            return
        if waga <30 or waga>200:
            return
                
                
        print("wszystko git",waga)
        return
        with open('user_data.json', 'r') as file:
            data = json.load(file)
        data['Persons'][login]={}
        data['Persons'][login]['login']=login
        data['Persons'][login]['Imie']=input("Podaj imie: ")
        data['Persons'][login]['Nazwisko']=input("Podaj Nazwisko: ")
        data['Persons'][login]['Email']=input("Podaj Email: ")
        password1=True
        password2=False
        while password1!=password2 or len(password1)<6:
            password1=input("Podaj Haslo: ")
            password2=input("Powtorz Haslo: ")
        data['Persons'][login]['Password']=password1
        data['Persons'][login]['Treningi']={}
        with open('user_data.json', 'w') as file:
            json.dump(data, file, indent=4)
        print("Uzytkownik dodany pomyslnie")
    def slider_changed(self,event):
        self.waga2_label.configure(text=self.get_current_value())
    def display_data(self):
        self.current_value= tk.DoubleVar()
        self.frame.grid_forget()
        self.login_label.grid_forget()
        self.login_entry.grid_forget()
        self.geometry("400x600")
        self.title("Siłka dodaj użytkownika")
        self.frame=ttk.LabelFrame(self,text="Dodawanie użytkonika",)
        self.frame.pack(padx=10,pady=10,expand=True,fill='both')

        self.imie_label=ttk.Label(self.frame,text="Imię: ",font=('Arial',15))
        self.imie_label.grid(column=0,row=0,padx=5,pady=10,sticky='E')

        self.imie_entry=ttk.Entry(self.frame,width=30)
        self.imie_entry.grid(column=1,row=0,padx=5,pady=10)

        self.nazwisko_label=ttk.Label(self.frame,text="Nazwisko: ",font=('Arial',15))
        self.nazwisko_label.grid(column=0,row=1,padx=5,pady=10,sticky='E')

        self.nazwisko_entry=ttk.Entry(self.frame,width=30)
        self.nazwisko_entry.grid(column=1,row=1,padx=5,pady=10)

        self.email_label=ttk.Label(self.frame,text="Email: ",font=('Arial',15))
        self.email_label.grid(column=0,row=2,padx=5,pady=10,sticky='E')

        self.email_entry=ttk.Entry(self.frame,width=30)
        self.email_entry.grid(column=1,row=2,padx=5,pady=10)

        self.waga_label=ttk.Label(self.frame,text="Waga: ",font=('Arial',15))
        self.waga_label.grid(column=0,row=3,padx=5,pady=10,sticky='E')

        self.waga_entry= ttk.Spinbox(self.frame,from_=30.0,to=200.0,increment=0.1,textvariable=self.current_value,wrap=True)
        self.waga_entry.grid(column=1,row=3,padx=5,pady=10)

        self.password1_label=ttk.Label(self.frame,text="Hasło: ",font=('Arial',15))
        self.password1_label.grid(column=0,row=4,padx=5,pady=10,sticky='E')

        self.password1_entry=ttk.Entry(self.frame,width=30,show="*")
        self.password1_entry.grid(column=1,row=4,padx=5,pady=10)

        self.password2_label=ttk.Label(self.frame,text="Powtórz: ",font=('Arial',15))
        self.password2_label.grid(column=0,row=5,padx=5,pady=10,sticky='E')

        self.password2_entry=ttk.Entry(self.frame,width=30,show="*")
        self.password2_entry.grid(column=1,row=5,padx=5,pady=10)

        self.login_button=ttk.Button(self.frame,text="Zaloguj",command=self.add_user)
        self.login_button.grid(column=1,row=6,padx=0,pady=10,sticky='e')
        

    def display_y_n(self):
        self.login_button.grid_forget()
        text="Dodać użytkownika o nicku: "+self.login.get()
        self.frame=ttk.LabelFrame(self,text=text)
        self.frame.grid(column=1,row=1,sticky='w',padx=5,pady=10,columnspan=1)
        self.Yes_button=ttk.Button(self.frame,text="Tak",command=self.display_data)
        self.Yes_button.grid(column=0,row=0,padx=10,pady=10)
        self.No_button=ttk.Button(self.frame,text="Nie",command=self.No)
        self.No_button.grid(column=1,row=0,padx=10,pady=10)
    def check_login(self):
        login=self.login.get()
        if " " in login:return
        if login:
            self.login_entry.config(state='disabled')
            with open('user_data.json', 'r') as file:
                data = json.load(file)
            if not login in data['Persons']:
                self.display_y_n()
if __name__=='__main__':
    app=login_App()
    app.mainloop()