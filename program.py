
from tkinter import *
import re

def callback():
    temp = E1.get()
    print(temp)
    if (temp == ""):
        title2.configure(text ="*** กรุณา ใส่ รหัสผ่าน ***",fg='red')
    elif(" " in temp):
        title2.configure(text ="*** รหัสผ่านห้ามมี ช่องว่าง ***" ,fg='red' )
    elif(re.search("[ก-ฮ]", temp)):
        title2.configure(text ="*** รหัสต้องเป็นภาษาอังกฤษ ตัวเลข หรือ อักขระพิเศษเท่านั้น ***" ,fg='red' )
    elif(len(temp) < 8):
        title2.configure(text ="*** รหัสต้องมีมากกว่า 8 ***" , fg='red')
    else:
        title2.configure(text ="กำลังคำนวน",fg='white')
        
# Top level window
frame = Tk()
frame.title("ปลุกความ secure ในตัวคุณ")
frame.geometry('1000x500')
frame.resizable(width=False, height=False)
frame.configure(bg='black')
# Function for getting Input
# from textbox and printing it 
# at label widget

title = Label(frame, text='ปลุกความ secure ในตัวคุณ !!!',font=('Georgia 60'),fg='white',bg='black')
title.place(x=30, y= 70) 
secure = Label(frame, text='secure',font=('Georgia 60'),fg='yellow green',bg='black')
secure.place(x=290, y= 70) 
title2 = Label(frame, text='*** กรุณา ใส่ รหัสผ่าน ***',font=('Georgia 15'),fg='white',bg='black')
title2.place(x=148, y= 220) 

E1 = Entry(frame, bd = 5,font=('Georgia 20'), width=40,show = "•")
E1.place(x=150, y=250) 

MyButton1 = Button(frame, text="Submit",font=('Georgia 10') ,width=13 ,height= 2, command=callback)
MyButton1.place(x=730, y=300)


frame.mainloop()