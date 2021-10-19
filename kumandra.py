print('----------importing functions----------')
from pygame import mixer
print('importing socket...')
import socket
print('importing time...')
from time import*
print('importing ptatogui')
import pyautogui
print('imorting tkinter...')
from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog
from tkinter import filedialog
from PIL import ImageTk
print('imorting webbrowser..')
from webbrowser import open_new, open_new_tab
print('import os...')
import os
print('import sys...')
from sys import exit
print('compiuter name =', socket.gethostname())
print('Kumandra 1.4')
print('starting  system...')
sys = Tk()
back = 'cyan'
sys.geometry('1366x770')
c = Canvas(sys, width=1370, height=730, bg=back)

def exitt():
    from playsound import playsound
    playsound('shutdown.wav')
    sys.destroy()
    print('bye-bye')
    print()
    exit()
c.pack()
taskbar = c.create_rectangle(0, 704, 1500, 1000, fill='gray')

assis = Button(sys, text='  erik')
assis.place(x=40, y=706)
def back():
    global sys
    a = Tk()
    l1 = Label(a, text='if you compiuter have a problem you can return to W-os 1.1')
    l1.pack()
    b1 = Button(a, text='return', command=ret)
    b1.pack()
    a.mainloop()
def set1():
    ste = Tk()
    ste.geometry('600x700')
    bakcol = Button(ste, text='Recovery', command=back)
    bakcol.place(x=10, y=10)
    ste.mainloop()

def onest(event):
    s = str(pyautogui.position())
    x1 = s[s.find('=')+1 : s.find(',')]
    y1 = s[s.rfind('=')+1 : s.find(')')]
    x = int(x1)
    y = int(y1)
    emmenu.post(x=x, y=y)
sys.bind('<Button-3>', onest)
emmenu = Menu(tearoff=0)
emmenu.add_command(label='exit', command=exitt)
emmenu.add_command(label='recovery', command=set1)
#b,a,u,r stroka
def menu():
    gomenu.post(x=0, y=700)

def wiki():
    wik = Tk()
    wik.geometry('200x100')
     
    e1 = Entry(wik)
    e1.pack()
    def w():
        wisea = e1.get()
        open_new_tab('en.wikipedia.org/wiki/' + str(wisea))
    b1 = Button(wik, text='search --->', command=w)
    
    b1.pack()
#stol 
notepad = ImageTk.PhotoImage(file="notepad.gif")
play = ImageTk.PhotoImage(file="player.gif")
def note():
    global e1
    note = Tk()
    note.title('notepad')
    e1 = Text(note, width=100, height=10)
    e1.pack()
    def openfile():
        global e1
        path = filedialog.askopenfile(initialdir="/", title="Select file",
                    filetypes=(("txt files", "*.txt"),("all files", "*.*")))
        e1.insert(0.0, path)
    mainmenu = Menu(note) 
    note.config(menu=mainmenu)
    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label='open...', command=openfile)
    mainmenu.add_cascade(label='file', menu=filemenu) 
def player():
    os.system('main.exe')

notepad2 = Button(sys, image=notepad, command=note)
player = Button(sys, image=play, command=player)
notepad2.place(x=10, y=10)
player.place(x=50, y=10)
#stolend
def ret():
    global sys
    import subprocess
    subprocess.call("C:\\Users\\Mirko\\Desktop\\pyt\\sysdisk\\kumandra.exe")
    sys.destroy()
    exit()


def web():
    open_new('google.com')
def dirct():
    dirc = Tk()
    dirc.geometry('730x900')
    file = Entry(dirc)
    file.place(x=100, y=0)
    go = Button(dirc, text='search', command=go)
    go.place(x=140, y=20)
    def go() :
        global file
        f = file.get()
        open(f)

def shell():
    os.system("C:\\Users\\Mirko\\Desktop\\pyt\\sysdisk\\wesh.exe")
def calc():
    import math
    window = Tk()
    window.geometry('260x280')
    window.title('calculator')
    e1 = Entry(window, justify=RIGHT, font=('Arial Baltic',15))
    e1.grid(row=0, column=0, columnspan=4)

    def addnum(num):
        value = e1.get()+str(num)
        e1.delete(0, END)
        e1.insert(0, value)
    def addoper(oper):
        value = e1.get()
        if value[-1] in '+-/*':
            value = value[:-1] 
        e1.delete(0, END)
        e1.insert(0, value + oper)
    def showrisu():
         value = e1.get()
         if value[-1] in '+-/*':
             oper2 = value[-1] 
             value = value[:-1]  + oper2 + value[:-1]
         e1.delete(0, END)
         e1.insert(0, eval(value))
     
    Button(window, text='1', command= lambda: addnum(1), font=('Arial Baltic',15)).grid(row=1, column=0,stick='wens')
    Button(window, text='2', command= lambda: addnum(2), font=('Arial Baltic',15)).grid(row=1, column=1,stick='wens')
    Button(window, text='3', command= lambda: addnum(3), font=('Arial Baltic',15)).grid(row=1, column=2,stick='wens')
    Button(window, text='4', command= lambda: addnum(4), font=('Arial Baltic',15)).grid(row=2, column=0,stick='wens')
    Button(window, text='5', command= lambda: addnum(5), font=('Arial Baltic',15)).grid(row=2, column=1,stick='wens')
    Button(window, text='6', command= lambda: addnum(6), font=('Arial Baltic',15)).grid(row=2, column=2,stick='wens')
    Button(window, text='7', command= lambda: addnum(7), font=('Arial Baltic',15)).grid(row=3, column=0,stick='wens')
    Button(window, text='8', command= lambda: addnum(8), font=('Arial Baltic',15)).grid(row=3, column=1,stick='wens')
    Button(window, text='9', command= lambda: addnum(9), font=('Arial Baltic',15)).grid(row=3, column=2,stick='wens')
    Button(window, text='0', command= lambda: addnum(0), font=('Arial Baltic',15)).grid(row=4, column=1,stick='wens')
    
    Button(window, text='+', command= lambda: addoper('+'), font=('Arial Baltic',15)).grid(row=1, column=3,stick='wens')
    Button(window, text='-', command= lambda: addoper('-'), font=('Arial Baltic',15)).grid(row=2, column=3,stick='wens')
    Button(window, text='/', command= lambda: addoper('/'), font=('Arial Baltic',15)).grid(row=3, column=3,stick='wens')
    Button(window, text='*', command= lambda: addoper('*'), font=('Arial Baltic',15)).grid(row=4, column=3,stick='wens')
    
    Button(window, text='=', command=showrisu, font=('Arial Baltic',15)).grid(row=4, column=2,stick='wens')


    window.grid_columnconfigure(0,minsize=60)
    window.grid_columnconfigure(1,minsize=60)
    window.grid_columnconfigure(2,minsize=60)
    window.grid_columnconfigure(3,minsize=60)
    window.grid_rowconfigure(1,minsize=60)
    window.grid_rowconfigure(2,minsize=60)
    window.grid_rowconfigure(3,minsize=60)
    window.grid_rowconfigure(4,minsize=60)

    winmenu = Menu(window)
    window.config(menu=winmenu)
    
    vidmenu = Menu(winmenu, tearoff=0)
    vidmenu.add_command(label="обычный")
    vidmenu.add_command(label="инженерскй")
    winmenu.add_cascade(label="Вид", menu=vidmenu)



    window.mainloop()
def actuve():
    act = Tk()
    act.geometry('800x800')
    c = Canvas(act, width=800, height=800, bg=back)
def funsear():
    fun = Tk()
    e1 = Entry(fun)
    def f():
        global e1
        t = e1.get()
        if t == 'calc':
            calc()
        if t == 'wshe':
            shell()
        if t == 'webb':
            web()
        if t == 'wikip':
            wiki()
        if t == 'exit':
            exitt()
    b1 = Button(fun, text='get', command=f)
    e1.pack()
    b1.pack()
            
go = Button(sys, text='go!', bg='green', activebackground='red',width=3, height=1, command=menu)
go.place(x=0, y=706)
gomenu = Menu(tearoff=0)
gomenu.add_command(label='file manager', command=dirct)
gomenu.add_command(label='web browser', command=web)
gomenu.add_command(label='calculator', command=calc)
gomenu.add_command(label='search in wiki', command=wiki)
gomenu.add_command(label='steggins', command=set1)
gomenu.add_command(label='WEshell', command=shell)
gomenu.add_separator()
sysmenu = Menu(gomenu, tearoff=0)
sysmenu.add_command(label='open...', command=funsear)  
gomenu.add_cascade(label='system administration', menu=sysmenu)
packmenu = Menu(gomenu, tearoff=0)
packmenu.add_command(label='kumandra active+', command=actuve)
gomenu.add_cascade(label='packs for system', menu=packmenu)
gomenu.add_separator()
gomenu.add_command(label='Exit', command=exitt)

    

sys.mainloop()
#while True:
#   timee = localtime()
#   timetex = c.create_text(1200, 710, text=timee, fill='red')

                                                                           
                                                                        
                                                                        


                                                                                                                                                                       



















                                                                                                                                                                       
