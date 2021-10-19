from tkinter import *
from pygame import mixer
from tkinter import filedialog


mixer.init()
root = Tk()


def p_song():
    pass
def n_song():
    pass
def play():
    song = song_box.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()
    song_state['text'] = "Воспроизведение"
def pause():
    mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    song_state['text'] = "Остановлено"
def stop():
    pass
def o_file():
    song = filedialog.askopenfilename(initialdir='tracks/', title="Выберите песню!", filetypes=(("mp3 Files", "*.mp3"),))
    song_box.insert(END, song)
def o_folder():
    print('not aviable :(')


master_frame = Frame(root)
master_frame.pack()

info_frame = Frame(master_frame)
info_frame.grid(row=0, column=0)

controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0)

file_frame = Frame(master_frame)
file_frame.grid(row=0, column=5)

song_state = Label(info_frame, width=60, text="Остановлено", font="Arial 8 bold")
song_state.grid(row=0, column=0)

song_box = Listbox(info_frame, width=60, selectbackground="blue")
song_box.grid(row=1, column=0)

p_button = Button(controls_frame, text='<-', width=5, command=p_song)
n_button = Button(controls_frame, text='->', width=5, command=n_song)
play_button = Button(controls_frame, text='|>', width=5, command=play)
pause_button = Button(controls_frame, text='||', width=5, command=pause)
stop_button = Button(controls_frame, text='[]', width=5, command=stop)

p_button.grid(row=0, column=0)
n_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=3)
stop_button.grid(row=0, column=4)

ofile_b = Button(file_frame, width=15, text='Открыть файл', command=o_file)
ofolder_b = Button(file_frame, width=15, text='Открыть папку', command=o_folder)

ofile_b.grid(row=0, column=0)
ofolder_b.grid(row=1, column=0)

root.mainloop()

