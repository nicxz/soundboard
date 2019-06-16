from tkinter import filedialog
from tkinter import *
from functools import partial
import tkSnack
import pickle
import os


win = Tk()
win.winfo_toplevel().title("Soundboard")
win.geometry("550x300") # Width x Height
tkSnack.initializeSnack(win)
button_identities = []
audiofiles = {}


def write_config():
    pickle_out = open("config.txt", "wb")
    pickle.dump(audiofiles, pickle_out)
    pickle_out.close()


def read_config():
    global audiofiles
    try:
        audiofiles = pickle.load(open("config.txt", "rb"))
        print(audiofiles)
    except Exception:
        pickle.dump(3, open("config.txt", "wb"))


def action(n):
    # function to get the index and the identity (bname), then play sound
    global audiofiles
    print(n)
    bname = (button_identities[n])
    if (var.get() == "OFF"):
        # play sound
        #bname.configure(text="clicked")
        snd = tkSnack.Sound()
        #snd.read('sound'+str(n)+'.wav')
        print("Value of audiofiles[n] is:")
        print(audiofiles.get(n, 'nix'))
        snd.read(audiofiles.get(n, 'nix'))
        snd.play(blocking=0)
        # sound done
        # bname.configure(text=n)
    else:
        print("Setup mode reached")
        audiofiles[n] = filedialog.askopenfilename(initialdir="/home/frank/programming/audioboard/", title="Select file", filetypes=[("Audio files", "*.wav *.mp3 ")])
        write_config()


def toggle():
    if var.get() == "ON":
        print("Setup mode on...")
    else:
        print("Setup mode off...")


read_config()
for i in range(9):
    # creating the buttons in the left column, assigning a unique argument (i) to run the function (change)
    if (audiofiles.get(i, 'nix') != 'nix'):
        button = Button(win, width=10, text=str(i) + " : " + os.path.basename(audiofiles.get(i, 'nix')), bg="blue", command=partial(action, i)).place(x=0, y=(i)*33)
    else:
        button = Button(win, width=10, text=str(i), bg = "yellow", fg = "black", command = partial(action, i)).place(x=0, y=(i) * 33)
    #button.pack()
    # add the button's identity to a list:
    button_identities.append(button)

for j in range(10, 19):
    # creating the buttons in the right column, assigning a unique argument (j) to run the function (change)
    button = Button(win, width=10, text=str(j), command=partial(action, j)).place(x=200, y=(j-10)*33)
    if (audiofiles.get(j, 'nix') != 'nix'):
        button = Button(win, width=10, text=str(j) + " : " + os.path.basename(audiofiles.get(j, 'nix')), bg="blue", command=partial(action, j)).place(x=200, y=(j-10)*33)
    else:
        button = Button(win, width=10, text=str(j), bg = "yellow", fg = "black", command = partial(action, j)).place(x=200, y=(j-10) * 33)
    #button.pack()
    # add the button's identity to a list:
    button_identities.append(button)

# setup button

# setupButton = Button(win, width=10, text="Setup", relief="raised", command=toggleSetup).place(x=400, y=7*33)
    w = Label(win, text="Setup: ").place(x=400, y=7*33)
    var = StringVar()
    setupButton = Checkbutton(win, onvalue="ON", offvalue="OFF", width=4,
                            indicatoron=False,
                            variable=var, textvariable=var,
                            selectcolor="green", background="red",
                            command=toggle).place(x=460, y=7*33)
    var.set("OFF")


# quit button
quitButton = Button(win, width=10, text="Quit", command=win.destroy).place(x=400, y=8*33)


win.mainloop()
