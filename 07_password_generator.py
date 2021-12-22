#import modules
import random
import string
from tkinter import *


#total characters that we need
characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')
#current generated password
out_now = list()


#generate new password
def generate_random_password():

    global out_now
    #default password length
    if len_var.get():
        length = int(len_var.get())
    else:
        length = 10

    #first shuffle in list
    random.shuffle(characters)
    password = []
    #select random chars
    for i in range(length):
        password.append(random.choice(characters))
    #second shuffle throwing the list
    random.shuffle(password)
    #create password
    out = ''.join(password)
    out_now.clear()
    out_now.append(out)
    #print password into main page
    out_var.set(out)
    root.update()


#copy created password into clipboard
def clipper():
    root.clipboard_clear()
    root.clipboard_append(out_now[0])


# create Front-End
root = Tk()
root.geometry('350x350')
root.title('Password Ganerator')
#main page text
Label(root, text = 'Please Enter Your Password Length:', font = 'arial 10 bold').place(x = 45, y = 30)

#output label settings
out_var = StringVar()
Label(root, textvariable = out_var, font = 'arial 20').place(x = 45, y = 90)

#Entry box configs
len_var = StringVar()
Entry(root, width = 30, textvariable = len_var).place(x = 60, y = 60)

#"generate" button
create_button = Button(root, text = 'Generate', width = 15, command = generate_random_password)
create_button.place(x = 90, y = 200)

#"copy to clipboard" button
copy_button = Button(root, text = 'Copy to clipboard', command = clipper, width = 15)
copy_button.place(x = 90, y = 230)

#run main page
root.mainloop()
