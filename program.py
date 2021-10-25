
from tkinter import *
from PIL import Image, ImageTk
import re
import math, time, difflib

def slope(posX, posY) -> list:
    Sx = Sy = Sxx = Syy = Sxy = 0.0

    for x, y in zip(posX, posY):
        Sx += x
        Sy += y
        Sxx += (x * x)
        Syy += (y * y)
        Sxy += (x * y)

    det = (Sxx * len(posX)) - (Sx * Sx)
    return [((Sxy * len(posX)) - (Sy * Sx)) / det, ((Sxx * Sy) - (Sx * Sxy)) / det]

def pearson(raw_u:list, raw_v:list) -> float:
    lst_u, lst_v = list(raw_u), list(raw_v)
    u_bar, v_bar = (sum(lst_u) / len(lst_u)), (sum(lst_v) / len(lst_v))

    remainder = sum([(u - u_bar) * (v - v_bar) for u, v in zip(lst_u, lst_v)])
    u_divider, v_divider = math.sqrt(sum([pow((u - u_bar), 2) for u in lst_u])), math.sqrt(sum([pow((v - v_bar), 2) for v in lst_v]))

    try:
        return remainder / (u_divider * v_divider)
    except ZeroDivisionError:
        return 0.0

def find_keyword(keyword:str,temp) -> list:
    with open("rockyou.txt", "r", encoding = "latin-1") as file:
        lst_keyword = [line.replace("\n", "") for line in file if keyword in line]

    if lst_keyword != []:
        return lst_keyword
    else:
        with open("rockyou.txt", "r", encoding = "latin-1") as file:
            lst_data = [line.replace("\n", "") for line in file]
        lst_keyword = difflib.get_close_matches(temp, lst_data)
        return lst_keyword

def compare(string_1:str, string_2:str):
    print("COMPARE:", string_1, "|", string_2)

    # string to ascii list
    txt_1, txt_2 = [ord(index) for index in string_1], [ord(index) for index in string_2]
    
    # swap short string to "txt_1"
    if len(txt_1) > len(txt_2):
        txt_1, txt_2 = txt_2, txt_1

    slope_1, slope_2 = slope(range(len(txt_1)), txt_1), slope(range(len(txt_2)), txt_2)
    print(f"EQ1: y = { round(slope_1[0], 4) }x + { round(slope_1[1], 4) }", "|", f"EQ2: y = { round(slope_2[0], 4) }x + { round(slope_2[1], 4) }")

    # pearson
    lst_result = []
    for window in range(len(txt_2)):
        if len(txt_2[window:(window + len(txt_2))]) >= len(txt_1):
            result = pearson(txt_1, txt_2[window:(window + len(txt_1))])
            lst_result.append(float(result))
            print(f"PEARSON: { string_1 } | { string_2[window:(window + len(txt_1))] } =", result)
    
    value_max = max(lst_result)
    sampling = ((value_max * len(txt_1)) + sum(lst_result) - value_max) / len(txt_2)
    print(f"Sampling: { sampling }%")

    print("=" * 20)
    return lst_result


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
        texT = checkpassword(temp)
        Value.configure(text=texT)
        title2.configure(text ="คำนวนเสร็จสิ้น",fg='white')

        

def hide_pass():
    if(var1.get() == 1):
        E1.configure(show="")
    else:
        E1.configure(show="•")

def checkpassword(temp):

    password = temp
    start = time.time()
    lst_keyword = find_keyword(password,temp)
    end = time.time()
        
    for keyword in lst_keyword:
        lst_compare = compare(password, keyword)

    print(f"SIMILAR: { len(lst_keyword) } word(s)", f"TIME: { round(end - start, 4) }s", sep = "\n")

    lst_similarity = []
    for _ in range(5):
        try:
            keyword_min = min(lst_keyword, key = len)
            lst_keyword.remove(keyword_min)
            lst_similarity.append(keyword_min)
        except ValueError:
            break

    if lst_similarity != []:
        print(f"TOP KEYWORD:", ", ".join(lst_similarity))
        return((f"TOP KEYWORD:", ", ".join(lst_similarity)))
    




     

# Top level window
frame = Tk()
frame.title("ปลุกความ secure ในตัวคุณ")
frame.geometry('1000x700')
frame.resizable(width=False, height=False)
frame.configure(bg='black')

image = Image.open("F:\code\python\datasture\project\hidden.png")
 
# Resize the image using resize() method
resize_image = image.resize((15, 15))
eye = ImageTk.PhotoImage(resize_image)


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

var1 = IntVar()
Checkbutton(frame, text="show password", variable=var1 ,command= hide_pass,fg='green',bg='black').place(x=850, y=260)

Value = Label(frame, text= "",font=('Georgia 15'),fg='white',bg='black')
Value.place(x=150, y= 375) 



frame.mainloop()