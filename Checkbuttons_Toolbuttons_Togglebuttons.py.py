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



def checker():
    #Getting the value of the var1 variable
    if var1.get() == 1:
        my_label.config(text="Checked!!!")
    else:
        my_label.config(text="Unchecked!!!")


#A Label
my_label=tb.Label(text="Click the checkbutton below",font=('Helvetica',12))

my_label.place(x=50,y=20)



#A checkButton

#Checking for conditions using integer if its 1 do this if its 0 do that
var1 =IntVar()


#Uisng the onvalue and offvalue for the conditions 
check =tb.Checkbutton(bootstyle="primary",text="Check me out",variable=var1,onvalue=1,offvalue=0,command=checker)

check.place(x=70,y=80)



#Tool Button

var2 =IntVar()

check2 =tb.Checkbutton(text="Tool Button",bootstyle="danger,toolbutton",variable=var2,onvalue=1,offvalue=0,command=checker)
check2.place(x=70,y=120)


#Outline
var3 =IntVar()

check3 =tb.Checkbutton(text="Tool Button",bootstyle="danger,toolbutton,outline",variable=var3,onvalue=1,offvalue=0,command=checker)
check3.place(x=70,y=160)




#Round Toggle Button
var4 =IntVar()

check4 =tb.Checkbutton(text="Rounded Button",bootstyle="success,round-toggle",variable=var4,onvalue=1,offvalue=0,command=checker)
check4.place(x=70,y=210)


#Square Toggle Button

var4 =IntVar()

check4 =tb.Checkbutton(text="Square Button",bootstyle="warning,square-toggle",variable=var4,onvalue=1,offvalue=0,command=checker)
check4.place(x=70,y=260)




root.mainloop()