import os
from tkinter import*
from tkinter import filedialog
import pyperclip
from pprint import pprint
from tkinter import messagebox 
import os.path

root = Tk()
root.title("ПросмотрФайлов bySavelev))))))")
root.geometry("800x600")
C = Canvas(root, bg="blue", height=800, width=600)
filename = PhotoImage(file = "1.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
message=StringVar()
message1=StringVar()
z=IntVar()

def path():
    root.filename =  filedialog.askdirectory()
    message=root.filename
    dirField.insert(0,message)


def list1():
     spam1=[]
     text1=Text(root)
     text1.place(x=20,y=280, height=280, width=720, bordermode=OUTSIDE)
     for file in os.listdir(message.get()):
         text1.insert(CURRENT ,file+"\n")
         if z.get()==1:
             pyperclip.copy(file)
             spam = pyperclip.paste()
             spam1.append(spam)
     spam1=str(spam1)
     pyperclip.copy(spam1)
     print(spam1)

     
            


def path2():
    spam1=[] 
    text1=Text(root) 
    text1.place(x=20,y=280, height=280, width=720, bordermode=OUTSIDE) 
    for top, dirs, files in os.walk(message.get()):
        top=top.replace(message.get(),"")
        text1.insert(1.0 ,"\n"+"(Файлы в папке: "+top+")\n")
        for nm in files:
            text1.insert(1.0 ,"Имя файла: "+nm+"\n")
            if z.get()==1:
               bufer=str(top+nm)
               print(bufer)
               spam1.append(bufer)
    spam1=str(spam1)
    pyperclip.copy(spam1)
            

def search():
    dirField1=Entry(textvariable=message1)
    message_button4 = Button(text="Поиск", command=search2)
    label1 = Label(text="Введите расширение файла", fg="#eee", bg="#333")
    label2 = Label(text="Выберите путь ", fg="#eee", bg="#333")
    
    dirField1.place(x=400,y=350, anchor="c", height=30, width=350, bordermode=OUTSIDE)
    message_button4.place(x=400,y=540, anchor="c", height=30, width=350, bordermode=OUTSIDE)
    label1.place(x=400,y=310, anchor="c", height=30, width=350, bordermode=OUTSIDE)
    label2.place(x=50,y=125, height=30, width=150, bordermode=OUTSIDE)

def search2():
    dirField1=Entry(textvariable=message1)
    dirField1.place(x=400,y=450, anchor="c", height=30, width=350, bordermode=OUTSIDE)

    text1=Text(root)
    text1.place(x=20,y=250, height=300, width=720, bordermode=OUTSIDE)
    for file in os.listdir(message.get()):
        if file.endswith(message1.get()):
             text1.insert(CURRENT ,file+"\n")
             print(os.path.join("/mydir", file))
    
     

message_button = Button(text="Выбрать Путь", command=path)
message_button1 = Button(text="Вывести список файлов в данном катологе", command=list1)
Check1=Checkbutton(root,text="Скопировать список в буфер обмена?",variable=z,onvalue=1, offvalue=0, padx=0, pady=0)
message_button2 = Button(text="Вывести список файлов из данного каталога и вложенных", command=path2)
message_button3 = Button(text="Поиск файла по расшерению в данном каталоге", command=search)
dirField=Entry(textvariable=message)




message_button.place(x=400,y=140, anchor="c", height=30, width=350, bordermode=OUTSIDE)
message_button1.place(x=400,y=175, anchor="c", height=30, width=350, bordermode=OUTSIDE)
message_button2.place(x=400,y=210, anchor="c", height=30, width=350, bordermode=OUTSIDE)
message_button3.place(x=400,y=245, anchor="c", height=30, width=350, bordermode=OUTSIDE)
dirField.place(x=400,y=100, anchor="c", height=30, width=250, bordermode=OUTSIDE)
Check1.place(x=650,y=100, anchor="c", height=30, width=230, bordermode=OUTSIDE)


root.mainloop()
