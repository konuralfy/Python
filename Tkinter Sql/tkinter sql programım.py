from tkinter import *
import sqlite3
import tkinter.messagebox

############### DATABASE CONNECTION AND CREATE TABLE ##############

baglan = sqlite3.connect("veriler")
cursor = baglan.cursor()

def tablo():
    cursor.execute("CREATE TABLE IF NOT EXISTS uyeler('kullanici_adi','sifre')")
    baglan.commit()

tablo()

##################### MAIN MENU OF PROGRAM #######################

class Program():
    def __init__(self):
        pencere = Tk()
        pencere.title("Try",)
        pencere.geometry("400x400")
        pencere.configure(background="black")

        yazi = Label(pencere)
        yazi.config(text="Hosgeldiniz",background = "black",foreground= "white", font =("fixedsys","20"),fg="red")
        yazi.pack(padx = 40, pady=40)

        buton = Button(pencere)
        buton.config(text="Sign Up!", command =sign_up, background = "gray6", foreground="green3",activebackground ="green4",activeforeground="gray6", height ="1",width="15")
        buton.pack(padx = 10, pady=10)

        buton = Button(pencere)
        buton.config(text="Sign In", command=sign_in,background = "gray6", foreground="green3",activebackground ="green4",activeforeground="gray6",height ="1",width="15")
        buton.pack(padx = 10, pady=10)

        buton = Button(pencere)
        buton.config(text="Delete User", command=delete_user,background = "gray6", foreground="green3",activebackground ="green4",activeforeground="gray6",height ="1",width="15")
        buton.pack(padx = 10, pady=10)

        buton = Button(pencere)
        buton.config(text="Update Password", command=update_password,background = "gray6", foreground="green3",activebackground ="green4",activeforeground="gray6",height ="1",width="15")
        buton.pack(padx = 10, pady=10)

        buton = Button(pencere)
        buton.config(text="User Informations", command=user_informations,background = "gray6", foreground="green3",activebackground ="green4",activeforeground="gray6",height ="1",width="15")
        buton.pack(padx = 10, pady=10)

        mainloop()

########### BASE CLASS FOR TOP LEVEL AND SIGN UP CLASS ###########

class sign_up():
    def __init__(self):
        self.window = Toplevel()
        self.window.title("Sign Up!")
        self.window.geometry("300x300")
        self.yazi = Label(self.window)
        self.yazi.config(text="Username")
        self.yazi.pack()
        self.username = Entry(self.window)
        self.username.pack()
        self.yazi2 = Label(self.window)
        self.yazi2.config(text="Password")
        self.yazi2.pack()
        self.password = Entry(self.window)
        self.password.pack()
        self.signup = Button(self.window)
        self.signup.config(text="Sign Up !", command= self.veriekle)
        self.signup.pack()

    def veriekle(self):
        cursor.execute("INSERT INTO uyeler VALUES('{}','{}')".format(self.username.get(), self.password.get()))
        baglan.commit()
        tkinter.messagebox.showinfo("Sign Up!","Üye Kaydınız Oluşturuldu")
        self.window.lift()

###################### SIGN IN CLASS ############################

class sign_in(sign_up):
    def __init__(self):
        super(sign_in, self).__init__()
        self.window.title("Sign In!")
        self.signup.config(text="Sign In !", command= self.girisyap)

    def girisyap(self):
        cursor.execute("SELECT kullanici_adi FROM uyeler WHERE kullanici_adi='{}'".format(self.username.get()))
        data = str(cursor.fetchone()[0])
        cursor.execute("SELECT sifre FROM uyeler WHERE kullanici_adi='{}'".format(self.username.get()))
        data2 = str(cursor.fetchone()[0])
        if (self.username.get() == data) and (self.password.get() == data2):
            tkinter.messagebox.showinfo("Sign In","Hoşgeldiniz {}".format(self.username.get()))
        self.window.lift()

################# DELETE USER CLASS ##############################

class delete_user(sign_up):
    def __init__(self):
        super(delete_user,self).__init__()
        self.window.title("Delete User!")
        self.signup.config(text="Delete User !", command= self.verisil)

    def verisil(self):
        cursor.execute("SELECT sifre FROM uyeler WHERE kullanici_adi='{}'".format(self.username.get()))
        silinecek_sifre = str(cursor.fetchone()[0])
        if (self.password.get() == silinecek_sifre):
            cursor.execute("DELETE FROM uyeler WHERE kullanici_adi='{}'".format(self.username.get()))
            baglan.commit()
        tkinter.messagebox.showinfo("Delete User","Üye Kaydınız Silinmiştir")
        self.window.lift()

################## UPDATE PASSWORD CLASS #########################

class update_password(sign_up):
    def __init__(self):
        super(update_password,self).__init__()
        self.window.title("Update Password!")
        self.yazi2.config(text="New Password")
        self.signup.config(text="Update Password!", command= self.sifreyenile)
    def sifreyenile(self):
        cursor.execute("UPDATE uyeler SET sifre='{}' WHERE kullanici_adi='{}'".format(self.password.get(), self.username.get()))
        baglan.commit()
        tkinter.messagebox.showinfo("Update Password","Şifreniz Başarıyla Değiştirilmiştir")
        self.window.lift()

##################### USER INFORMATION CLASS ########################

class user_informations():
    def __init__(self):
        self.window = Toplevel()
        self.window.title("User Informations!")
        self.window.geometry("300x300")
        cursor.execute("SELECT COUNT(*) FROM uyeler")
        rows = int(cursor.fetchone()[0])
        cursor.execute("SELECT kullanici_adi,sifre FROM uyeler")
        for i in range(rows):
            ks = list(cursor.fetchone())
            info = Label(self.window)
            info.config(text = "Kullanıcı Adı: {} | Şifre: {}\n".format(ks[0],ks[1]))
            info.pack()


Program()
