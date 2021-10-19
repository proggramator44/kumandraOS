from tkinter import *
log = Tk()
log.geometry('120x110')
l1 = Label(log, text='username', width=8, height=1)
e1 = Entry(log)
l2 = Label(log, text='password', width=8, height=1)
e2 = Entry(log)
def nextt():
    entrget = e1.get()
    ent2 = e2.get()
    s = str(entrget)
    s2 = str(ent2)
    data = open('userdata.txt', 'a')
    data.write(s +'\n', s2 + '\n')
    data.close()
    log.destroy

b1 = Button(log, text='next-->', command=nextt)
l1.pack()
e1.pack()
l2.pack()
e2.pack()

b1.pack()
log.mainloop()
