# Multi-frame tkinter application v2.3
import tkinter as tk
from tkinter import ttk
import math, time, difflib, threading, json, sys, secrets
import numpy 

# Implement the default Matplotlib key bindings.

password = "";
timecal = 0;

file_name = "rockyou.txt"
# file_name = "rockpol.txt"

def passwordGenerater(passwordInput:str, lenghtPasswordGen:int = 15 , haveLowerChar:bool = True, haveUpperChar:bool = True, haveNum:bool = True, haveSpacialChar:bool = True, wantedNoOfPassword:int = 10):
    """
    A = U * S * V.transpose()
    A_INVERSE = V * inv(S) * transpose(U)

    used ascii is in range (33 - 126)
    SpacialChar = 33-47, 58-64, 91-96, 123-126
    Num = 48-57
    UpperChar = 65-90
    LowerChar = 97-122
    """
    # rand_num = numpy.array([[secrets.SystemRandom().randrange(-10000, 10000) for i in range(len(passwordInput))] for j in range(len(passwordInput))])
    # print(rand_num)
    
    lst_spacialChar = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)] + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]
    lst_num = [chr(i) for i in range(48,58)]
    lst_upper = [chr(i) for i in range(65,91)]
    lst_lower = [chr(i) for i in range(97,123)]
    allCharacter = [lst_spacialChar, lst_num, lst_upper, lst_lower]
    countLoop = 0
    can_inverse = False
    checkIfNewAssign = False
    while not can_inverse:
        countLoop += 1
        if countLoop > 5:
            checkIfNewAssign = True
            # print("countLoop",countLoop)
            new_password_pass = False
            while not new_password_pass:
                new_password = ""
                checkbook = [False, False, False,False] # spacialChar, num, upper, lower
                for i in range(lenghtPasswordGen): # len(passwordInput)
                    new_password += secrets.choice(secrets.choice(allCharacter))
                for i in new_password:
                    if False in checkbook:
                        if i in lst_spacialChar:
                            checkbook[0] = True
                        elif i in lst_num:
                            checkbook[1] = True
                        elif i in lst_upper:
                            checkbook[2] = True
                        elif i in lst_lower:
                            checkbook[3] = True
                    else:
                        passwordInput = new_password
                        new_password_pass = True
                        break
        
        list_pw = [ord(i) for i in passwordInput]
        list_pwR = list_pw.copy()
        list_pwR.reverse()
        count_rand = 10 # secrets.SystemRandom().randrange(2, 10)
        list_rand_pos_pw = [[[list_pw[secrets.SystemRandom().randrange(0, len(list_pw))] if secrets.SystemRandom().randrange(0, 1) == 0 else list_pw[secrets.SystemRandom().randrange(0, len(list_pw))] for i in range(len(list_pw)) ] for j in range(len(list_pw))] for j in range(count_rand)]
        index_list_pos_pw = secrets.SystemRandom().randrange(0, count_rand - 1)
        using_list_rand_pos_pw = list_rand_pos_pw[index_list_pos_pw]
        # test_using = [[chr(int(row[i])) for i in range(len(using_list_rand_pos_pw))]for row in using_list_rand_pos_pw]
        # print(test_using)
        using_list_rand_pos_pw_T = [[row[i] for row in using_list_rand_pos_pw]for i in range(len(using_list_rand_pos_pw))]

        row_can_inverse = True
        for i in range(len(using_list_rand_pos_pw)):
            if row_can_inverse:
                for j in range(i, len(using_list_rand_pos_pw)):
                    if (using_list_rand_pos_pw[i] == using_list_rand_pos_pw[j]) and (i != j):
                        row_can_inverse = False
                        break
                    elif i == j == len(using_list_rand_pos_pw) - 1:
                        row_can_inverse = True
            else:
                break
        
        col_can_inverse = True
        for i in range(len(using_list_rand_pos_pw_T)):
            if col_can_inverse:
                for j in range(i, len(using_list_rand_pos_pw_T)):
                    if (using_list_rand_pos_pw_T[i] == using_list_rand_pos_pw_T[j]) and (i != j):
                        col_can_inverse = False
                        break
                    elif i == j == len(using_list_rand_pos_pw_T) - 1:
                        col_can_inverse = True
            else:
                break
        can_inverse = ((col_can_inverse) and (row_can_inverse))

    # if checkIfNewAssign:
    #     # print("Your password may be too hard to use for generating passwords from matrix inversed by SVD.")
    #     # print(f"Now, we random the new password \"{passwordInput}\" instead.\n")
        
    #     # checkIfNewAssign = False

    A = numpy.array(using_list_rand_pos_pw)
    U, S, V_TRANSPOSE = numpy.linalg.svd(A, full_matrices=True)
    S_INVERSE = numpy.diag(numpy.array([(1/i) for i in S])) # or numpy.linalg.inv(TEMP_S)
    A_INVERSE = numpy.dot(numpy.dot(numpy.transpose(V_TRANSPOSE), S_INVERSE), numpy.transpose(U))

    # password Generator
    genPassword = []
    for i in range(wantedNoOfPassword):
        lst_have = [haveSpacialChar, haveNum, haveUpperChar, haveLowerChar]
        sum_left = lenghtPasswordGen
        # print(sum_left)
        while (sum_left != 0) or (True in lst_have):
            sum_left = lenghtPasswordGen
            lst_have = [haveSpacialChar, haveNum, haveUpperChar, haveLowerChar]
            rand_index = []
            for index in range(4):
                rand_index.append([secrets.SystemRandom().randrange(0, 1000), index])
            rand_index.sort()
            for i in range(4):
                # print("rand_index[i][1]",rand_index[i][1])
                if lst_have[rand_index[i][1]]:
                    if i != 3:
                        if sum_left == 1:
                            temp_rand_1_sumleft = sum_left
                        elif sum_left > 1:
                            temp_rand_1_sumleft = secrets.SystemRandom().randrange(1, sum_left)
                        else:
                            continue
                            # sum_left -= lenghtPasswordGen * 2# make sum_left < 0
                    else:
                        if sum_left > 0:
                            temp_rand_1_sumleft = sum_left
                        else:
                            continue
                            # sum_left -= lenghtPasswordGen * 2
                    if temp_rand_1_sumleft >= 1:
                        rand_index[i].append(temp_rand_1_sumleft)
                        sum_left -= temp_rand_1_sumleft
                        lst_have[rand_index[i][1]] = False
                    else:
                        continue
                else:
                    rand_index[i].append(0)

        R1_A_INVERSE = numpy.reshape(A_INVERSE, (len(passwordInput) ** 2), order = "F")

        temp_li_index_genpassword = [i for i in range(lenghtPasswordGen)]
        li_genpassword = [None for i in range(lenghtPasswordGen)]

        for ri in rand_index:
            for _ in range(ri[2]):
                index_choice = secrets.choice(temp_li_index_genpassword)
                li_genpassword[index_choice] = ri[1]
                temp_li_index_genpassword.remove(index_choice)
        # print(li_genpassword)
        
        temp_li_index_genpassword = [i for i in range(lenghtPasswordGen)]
        li_output = [None for _ in range(lenghtPasswordGen)]
        s = ""
        for _ in range(lenghtPasswordGen):
            index_choice = secrets.choice(temp_li_index_genpassword)
            # if li_genpassword[index_choice] == 0:
            temp_li_index_genpassword.remove(index_choice)
            li_output[index_choice] = allCharacter[li_genpassword[index_choice]][int(R1_A_INVERSE[secrets.SystemRandom().randrange(0, len(passwordInput)**2) - 1] * 10000.0) % len(allCharacter[li_genpassword[index_choice]])]
        # print(li_output)
        for i in li_output:
            s += i
        genPassword.append(s)
    # print(genPassword)
    
    return list([checkIfNewAssign,passwordInput,genPassword])
def pearson(raw_u:list, raw_v:list) -> float:
    lst_u, lst_v = list(raw_u), list(raw_v)
    u_bar, v_bar = (sum(lst_u) / len(lst_u)), (sum(lst_v) / len(lst_v))

    remainder = sum([(u - u_bar) * (v - v_bar) for u, v in zip(lst_u, lst_v)])
    u_divider, v_divider = math.sqrt(sum([pow((u - u_bar), 2) for u in lst_u])), math.sqrt(sum([pow((v - v_bar), 2) for v in lst_v]))

    try:
        return remainder / (u_divider * v_divider)
    except ZeroDivisionError:
        return 0.0

def cosine(raw_u:list, raw_v:list):
    lst_u, lst_v = list(raw_u), list(raw_v)

    remainder = sum([(u) * (v) for u, v in zip(lst_u, lst_v)])
    u_divider, v_divider = math.sqrt(sum([pow((u), 2) for u in lst_u])), math.sqrt(sum([pow((v), 2) for v in lst_v]))
    try:
        return remainder / (u_divider * v_divider)
    except ZeroDivisionError:
        return 1.0

def lcs(keyword:str) -> list:
    temp = len(keyword)//2
    li_lcs = [keyword]
    for i in range(temp):
        fs = i+1
        last = 0
        while(fs >= 0):
            li_lcs.append(keyword[fs:len(keyword)-last])
            fs -= 1
            last += 1
    return li_lcs
            
def find_keyword(keyword:str) -> list:    
    lst_lcs = lcs(keyword)
    with open(file_name, "r", encoding = "latin-1") as file:
        lst_keyword = [line.replace("\n", "") for line in file if [True for index in lst_lcs if index in line] != []] #
        
    if lst_keyword != []:
        with open("similarity.json") as file:
            data = json.load(file)
        data["KEYWORD"] = lst_keyword
        with open("similarity.json", "w") as file:
            json.dump(data, file)
    if len(lst_keyword) < 100:
        processs = threading.Thread(target = find_keyword_similarity, args = [keyword])
        processs.start()
        # animation_waiting(processs)
        # processs.join()

        with open("similarity.json") as file:
            data = json.load(file)
        for dat in data["KEYWORD"]:
            if dat not in lst_keyword:
                lst_keyword.append(data)
    return lst_keyword

def find_keyword_similarity(keyword:str):
    with open(file_name, "r", encoding = "latin-1") as file:
        lst_data = [line.replace("\n", "") for line in file]
    lst_keyword = difflib.get_close_matches(keyword, lst_data)

    with open("similarity.json") as file:
        data = json.load(file)
    data["KEYWORD"] = lst_keyword
    with open("similarity.json", "w") as file:
        json.dump(data, file)

def animation_waiting(process:threading.Thread):
    while process.is_alive():
        chars = "/—\|" 
        for char in chars:
            sys.stdout.write('\r' + 'LOADING ' + char)
            time.sleep(.1)
            sys.stdout.flush()

def isStringSameChar(text:int):
    t = text[0]
    same = True
    for i in text:
        if i != t:
            same = False
    return same

def pearson(raw_u:list, raw_v:list) -> float:
    lst_u, lst_v = list(raw_u), list(raw_v)
    u_bar, v_bar = (sum(lst_u) / len(lst_u)), (sum(lst_v) / len(lst_v))

    remainder = sum([(u - u_bar) * (v - v_bar) for u, v in zip(lst_u, lst_v)])
    u_divider, v_divider = math.sqrt(sum([pow((u - u_bar), 2) for u in lst_u])), math.sqrt(sum([pow((v - v_bar), 2) for v in lst_v]))

    try:
        return remainder / (u_divider * v_divider)
    except ZeroDivisionError:
        return 1.0

def getBestLcsWindow(lst_lcs:list, string_data:str, password:str, value_only = None):
    lst_samplingVal_of_each = []
    for lcs1 in lst_lcs:
        lst_result = []
        if len(lcs1) <= len(string_data) and len(string_data) <= math.ceil(len(lcs1) * 2):
            if not value_only:
                print(lcs1 , "|", string_data)
            # string to ascii list
            txt_1, txt_2 = [ord(index) for index in lcs1], [ord(index) for index in string_data]
            # pearson
            for window in range(len(txt_2) - len(txt_1) + 1):
                if not isStringSameChar(password):
                    result = pearson(txt_1, txt_2[window:(window + len(txt_1))])
                else:
                    result = cosine(txt_1, txt_2[window:(window + len(txt_1))])
                lst_result.append(float(result))
                if not value_only:
                    # print("PEARSON: =", result)
                    print(f"PEARSON: { lcs1 } | { string_data[window:(window + len(txt_1))] } =", result)
            value_max = max(lst_result)
            sampling = (((value_max * len(lcs1)) + sum(lst_result) - value_max) / len(string_data)) * (len(lcs1)/len(password)) * (len(lcs1)/len(string_data))
            lst_samplingVal_of_each.append([sampling, string_data, lcs1])
            if not value_only:
                print(sampling)
    if lst_samplingVal_of_each != []:
        return max(lst_samplingVal_of_each)
    else:
        return None


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()



class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg='black')
        tk.Label(self, text="คำชี้แจง", font=("FC Ekaluck", 40), fg="white",bg='black').pack(padx=0, pady=20, side=tk.TOP)

        tk.Label(self, text="\
             ปลุกความ Secure ในตัวคุณ! จัดทำขึ้นเพื่อตรวจสอบความปลอดภัยของรหัสผ่าน\n\
        เมื่อนำมาเทียบกับชุดข้อมูลของรหัสผ่านที่เคยรั่วไหลเป็นจำนวนมาก โดยใช้หลักการและ\n\
        เหตุผลในการคำนวณทางคณิตศาสตร์เพื่อไม่ให้ผู้ประสงค์ร้ายสามารถคาดเดา รหัสผ่าน\n\
        และเข้าถึงข้อมูลส่วนตัวได้รวมทั้งเสนอแนะการตั้งรหัสผ่านที่ปลอดภัยด้วย \n\n\n\
        *ทางโปรแกรมจะไม่ทำการเก็บข้อมูลรหัสผ่านหรือส่งข้อมูลรหัสผ่านของท่าน*", font=("FC Ekaluck", 20), fg="white",bg='black',justify="left").pack(padx=20, pady=60, side=tk.TOP)

        tk.Button(self, text='รับทราบ', font=("FC Ekaluck", 20),width=30, height=2,command=lambda: master.switch_frame(PageOne)).pack(padx=20, pady=20, side=tk.TOP)




        # tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        # tk.Button(self, text="Open page one",
        #           command=lambda: master.switch_frame(PageOne)).pack()
        # tk.Button(self, text="Open page two",
        #           command=lambda: master.switch_frame(PageTwo)).pack()

# class PageOne(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
#         tk.Button(self, text="Return to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()

class PageOne(tk.Frame):
    def gonext(self, master,data,temp):
        if len(data) < 8 :
           temp.configure(text ="กรุณากรอกรหัสผ่านใหม่ (รหัสผ่านต้องมากกว่า 8 ตัว)")
        elif " " in data:
            temp.configure(text ="กรุณากรอกรหัสผ่านใหม่ (ในรหัสผ่านต้องไม่มีช่องว่าง)")
        else:
            temp.configure(text ="กำลังคำนวณ",fg="white")
            temp.pack()
            global password
            password = data
            master.switch_frame(PageTwo)
        
    def __init__(self, master):
        tk.Frame.__init__(self, master,bg='black')
        tk.Label(self, text="ปลุกความ secure ในตัวคุณ !!!", font=("FC Ekaluck", 55), fg="white",bg='black').pack(padx=0, pady=50, side=tk.TOP)
        temp = tk.Label(self, text="", font=("FC Ekaluck", 15), fg="red",bg='black')
        temp.pack(padx=0, pady=2, side=tk.TOP,anchor=tk.W)
        x = tk.Entry(self, bd = 5,font=('Georgia 20'), width=35,show = "•")
       #tk.Button(self, text='คำนวน', font=("FC Ekaluck", 20),width=15, height=1, command=lambda: master.switch_frame(PageTwo) ).pack(padx=5, pady=50, side = tk.BOTTOM ,anchor=tk.W)
        tk.Button(self, text='คำนวณ', font=("FC Ekaluck", 20),width=15, height=1, command=lambda:self.gonext(master,x.get(),temp)).pack(padx=5, pady=50, side = tk.BOTTOM ,anchor=tk.W)
        
        x.pack(padx=0, pady=0 ,side=tk.LEFT, anchor=tk.W )
        
        self.var = tk.IntVar()
        tk.Checkbutton(self, text="show password", variable=self.var ,command=lambda:x.configure(show="" ) if self.var.get() == 1 else x.configure(show="•" ), fg='green',bg='black').pack(padx=5, pady=0 ,side=tk.LEFT,anchor=tk.W)
        #tk.Button(self, text='รับทราบ', font=("FC Ekaluck", 20),width=15, height=1,command="x").pack(padx=5, pady=5, side = tk.BOTTOM ,anchor=tk.SW)

class PageTwo(tk.Frame):
    def Genpass(self,Length_of_gen_password,have_lowerChar,have_upperChar,have_numberChar,have_spacialChar,numpassword,tab):
        global password

        print("password :",password)
        print("Length_of_gen_password :",Length_of_gen_password)
        print("have_lowerChar :",have_lowerChar)
        print("have_upperChar :",have_upperChar)
        print("have_numberChar :",have_numberChar)
        print("have_spacialChar :",have_spacialChar)
        print("numpassword :",numpassword)
        if(bool(have_lowerChar) or bool(have_upperChar) or bool(have_numberChar) or bool(have_spacialChar)):
            
            temp = (passwordGenerater(str(password),int(Length_of_gen_password),bool(have_lowerChar),bool(have_upperChar),bool(have_numberChar),bool(have_spacialChar),int(numpassword)))
            print(temp)
            count = 1
            for i in range(10):
                w = tk.Text(tab, height=1, borderwidth=0)
                w.insert(1.0, "                                                                       ")
                w.grid(column = 0, row = count,padx =  5,pady = 0,sticky='S')
                w.configure(state="disabled")
                count += 1

            count = 1
            for i in temp[2]:

                w = tk.Text(tab, height=1, borderwidth=0)
                w.insert(1.0, temp[2][count-1])
                w.grid(column = 0, row = count,padx =  5,pady = 0,sticky='S')
                w.configure(state="disabled")
                count += 1


            
            
        else:
            count = 1
            for i in range(10):
                w = tk.Text(tab, height=1, borderwidth=0)
                w.insert(1.0, "                                                                       ")
                w.grid(column = 0, row = count,padx =  5,pady = 0,sticky='S')
                w.configure(state="disabled")
                count += 1
            
            w = tk.Text(tab, height=1, borderwidth=0)
            w.insert(1.0, "*** การสร้างรหัสผ่านจำเป็นต้องเลือกอย่างน้อย 1 ตัวเลือก ***")
            w.grid(column = 0, row = 1,padx =  5,pady = 0,sticky='S')
            w.configure(state="disabled")
            count += 1
            
        #print(passwordGenerater("password",8,True,True,True,True,2))
        



    def __init__(self, master):
        
        tk.Frame.__init__(self, master,bg='black')
        global password

        #print("page2",password)
        starttime = time.time()
        lst_keyword = find_keyword(password)
        lst_lcs = list(set(lcs(password)))
        lst_data_similarity = []
        for keyword in lst_keyword:
            data_similarity = getBestLcsWindow(lst_lcs, keyword, password, True)
            if data_similarity is not None:
                lst_data_similarity.append(data_similarity)
        endtime = time.time()

        print("time =",endtime-starttime)
        similiarPasswordCount = len(lst_data_similarity)
        top_5_max_similarity = []


        if similiarPasswordCount <= 5:
            num = similiarPasswordCount
        else:
            num = 5
        if num == 0:
            print("No Similiar Password")
        else:
            #print(f"Your password is similiar with other {similiarPasswordCount} passwords")
            # print(f"Top {num} Password similar with \"{password}\" :")
            for _ in range(5):
                if lst_data_similarity != []:
                    temp_max = max(lst_data_similarity)
                    top_5_max_similarity.append(temp_max)
                    lst_data_similarity.remove(temp_max)
                    # print("{}. \"{}\"\twith Keyword \"{}\"\t\tSimilarity = {:.4f}%".format(countPrint,temp_max[1],temp_max[2],temp_max[0]*100))

            print(top_5_max_similarity)

    


        #tk.Label(self, text=str(top_5_max_similarity), font=("FC Ekaluck", 15), fg="red",bg='black').pack()
        tk.Button(self, text='กลับ', font=("FC Ekaluck", 15),width=15, height=1, command=lambda:master.switch_frame(PageOne)).pack(padx=0, pady=0, side = tk.BOTTOM ,anchor=tk.E)
        tabControl = ttk.Notebook(self, width=650, height=200) 
        tab1 = ttk.Frame(tabControl, width=650, height=200)
        # tab2 = ttk.Frame(tabControl, width=650, height=200)
        tab3 = ttk.Frame(tabControl, width=650, height=200)
        tab4 = ttk.Frame(tabControl, width=650, height=200)

        tabControl.add(tab1, text ='รหัสผ่านที่มีความคล้าย')
        # tabControl.add(tab2, text ='กราฟ')
        tabControl.add(tab3, text ='เครื่องมือสร้างรหัสผ่าน')
        tabControl.add(tab4, text ='รหัสผ่านที่สร้างขึ้น')

        tabControl.pack(padx=0, pady=40 ,side=tk.BOTTOM,anchor=tk.W)

        temp = ""
        count  = 1
        if(len(top_5_max_similarity ) == 0):
            temp += "ไม่มีรหัสผ่านที่คล้ายกับรหัสผ่านของคุณ"
        else:
            for i in top_5_max_similarity:
                temp += str(count) +".) "+str(i[1]) + "    "+ "{:.12f}".format(round(i[0], 10)* 100.0)  + "%" 
                if(count <= 4):
                    temp += "\n"
                count += 1

        ttk.Label(tab1, text =temp, font=("FC Ekaluck", 22)).grid(column = 0, row = 0,padx = 20,pady = 5,sticky='W')  
        temp1 = "รหัสผ่านของคุณคล้ายคลึงกับอีก "+str(similiarPasswordCount)+" รหัสผ่าน\n"
        temp1 += "เวลาการคำนวน "+str(endtime-starttime)+" วินาที"
        ttk.Label(tab1, text =temp1, font=("FC Ekaluck", 15)).grid(column = 0, row = 1,padx = 20,pady = 0,sticky='W')  
        # ttk.Label(tab2, text ="Garph", font=("FC Ekaluck", 22)).grid(column = 0, row = 0,padx = 20,pady = 20)  
        
        ttk.Label(tab3, text ="ตัวเลือกการสร้างรหัสผ่าน", font=("FC Ekaluck", 15)).grid(column = 0, row = 0,padx =  5,pady = 10,sticky='W')
       
        
        self.lowerChar = tk.BooleanVar()
        lowerCharCheck = ttk.Checkbutton(tab3,text='ตัวอักษรพิมพ์เล็ก (a-z)',command=lambda:print(self.lowerChar.get()),variable= self.lowerChar ,onvalue=True,offvalue=False)
        lowerCharCheck.grid(column = 0, row = 1,padx = 5,pady = 0,sticky='W')

        self.upperChar = tk.BooleanVar()
        upperCharCheck = ttk.Checkbutton(tab3,text='ตัวอักษรพิมพ์ใหญ่ (A-Z)',command=lambda:print(self.upperChar.get()),variable= self.upperChar ,onvalue=True,offvalue=False)
        upperCharCheck.grid(column = 0, row = 2,padx = 5,pady = 0,sticky='W')

        self.Num = tk.BooleanVar()
        Numcheck = ttk.Checkbutton(tab3,text='ตัวเลข (0-9)',command=lambda:print(self.Num.get()),variable= self.Num ,onvalue=True,offvalue=False)
        Numcheck.grid(column = 0, row = 3,padx = 5,pady = 0,sticky='W')

        self.spacialChar = tk.BooleanVar()
        spacialCharCheck = ttk.Checkbutton(tab3,text='ตัวอักขระพิเศษ',command=lambda:print(self.spacialChar.get()),variable= self.spacialChar ,onvalue=True,offvalue=False)
        spacialCharCheck.grid(column = 0, row = 4,padx = 5,pady = 0,sticky='NW')
    
        tk.Label(tab3, text ="ความยาวของรหัสผ่าน", font=("FC Ekaluck", 13)).grid(column = 2, row = 0,padx =  5,pady = 0,sticky='S')
        self.v1 = tk.IntVar()
        length_input = tk.Scale(tab3, from_=8, to=50, orient=tk.HORIZONTAL, length= 300,showvalue=True,variable = self.v1).grid(column = 2, row = 1,padx = 5,pady = 0,sticky='W')
        
        tk.Label(tab3, text ="จำนวนรหัสผ่านที่ต้องการให้สร้าง", font=("FC Ekaluck", 13)).grid(column = 2, row = 2,padx =  5,pady = 0,sticky='S')
        self.v2 = tk.IntVar()

        length_input2 = tk.Scale(tab3, from_=1, to=10, orient=tk.HORIZONTAL, length= 300,showvalue=True,variable = self.v2).grid(column = 2, row = 3,padx = 5,pady = 0,sticky='W')
        
        
        textpassgen = tk.Label(tab4, text ="รหัสผ่านที่สร้าง", font=("FC Ekaluck", 13)).grid(column = 0, row = 0,padx =  5,pady = 0,sticky='W')
        
        
        btn = tk.Button(tab3, bg='#000000',fg='#b7f731',relief='flat',text='สร้างรหัสผ่าน',width=20,command=lambda:self.Genpass(self.v1.get(),self.lowerChar.get(),self.upperChar.get(),self.Num.get(),self.spacialChar.get(),self.v2.get(),tab4)).grid(column = 5, row = 4,padx = 5,pady = 10,sticky='W')
        
        #tk.Button(self, text='คำนวน', font=("FC Ekaluck", 20),width=15, height=1, command=lambda:print("X")).grid(column = 0, row = 5,padx = 5,pady = 0,sticky='W')

        #passwordGenerater(password, noGen, lowerChar, upperChar, noChar, spacialChar, numberofGenPassword)
        # print(passwordGenerater("1223213123"))
        # button = tk.Button(tab2, text="Quit", command=tab2.quit)
        # button.pack(side=tk.BOTTOM)
        
        
        
        tk.Label(self, text="ปลุกความ secure ในตัวคุณ !!!", font=("FC Ekaluck", 40), fg="white",bg='black').pack(padx=0, pady=15, side=tk.TOP,anchor=tk.W)
        x = tk.Entry(self, bd = 5,font=('Georgia 20'), width=35,show = "•")
        x.insert(0,password)
        x.pack(padx=0, pady=0 ,side=tk.LEFT, anchor=tk.W )    
        self.var = tk.IntVar()
        tk.Checkbutton(self, text="show password", variable=self.var ,command=lambda:x.configure(show="" ) if self.var.get() == 1 else x.configure(show="•" ), fg='green',bg='black').pack(padx=5, pady=0 ,side=tk.LEFT,anchor=tk.W)

if __name__ == "__main__":
    app = SampleApp()

    app.title("PAP.exe")
    app.geometry('1000x500')
    app.resizable(width=False, height=False)
    app.configure(bg='black')

    app.mainloop()  