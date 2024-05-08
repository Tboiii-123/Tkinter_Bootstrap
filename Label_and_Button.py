#To access the website on ttkbootstrap
#Search on ttkbootstrap.readocs.io on the web and click on started
#We first start with intsalling ttkbootsttrap in out pc
#pip install ttkbootstrap
from tkinter import *

#It is to make the attribute value be in capital letter and not be in a  strinf
from ttkbootstrap.constants import *

import ttkbootstrap as tb



# Seeting a root in ttkbootstrap
#The themename is an attribute storing different colors,part of the names are
# superhero cyborg minty united darkly vapor flatly lumen pulse sandstone solar cosmo lumen simplex cerculean morph yeti
#literal
root =tb.Window(themename='cyborg')

root.title("Bootstratp in Python")
root.geometry("500x360")




#Creating a function for the Button
counter=0

def changer():
    global counter
    counter+=1
    if counter % 2==0:
        my_label.config(text="Hello world")
    else:
        my_label.config(text="Good Bye World!")
    



# Creating Label in Bootsrtap Tkinter

#bootstyle is for styling the widget uisng bootstrap
#colors like  danger,default,light,dark,sucess,info etc
#They are all in bootstrap website
my_label =tb.Label(text="Hello world!",font=('Helvetica',18),bootstyle="danger")

my_label.place(x=2,y=10)


#Adding the inverse Attribute
my_label2 =tb.Label(text="Hello world!",font=('Helvetica',28),bootstyle="danger,inverse")

my_label2.place(x=230,y=10)



#Creating a button
my_button =tb.Button(text="Click me",bootstyle="primary",command=changer)

my_button.place(x=2,y=90)


#Adding outline attribute
my_button2 =tb.Button(text="Click me",bootstyle="primary,outline")

my_button2.place(x=100,y=90)






root.mainloop()

