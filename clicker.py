import tkinter as tk
from tkinter import ttk
from tkinter import *
from pynput.mouse import Controller, Button
import time
import keyboard
from pynput.keyboard import Listener
import mouse
from pynput.keyboard import Controller as Cntrl
global repeats
global numberofcomandsnumber
global turnoff
global stopvariable
global timern
import multiprocessing
numberofcomandsnumber = 0
selected_key = "Esc"
true_selected_key = "Esc"
selected_time = 0.5
time_sleep = 2
x = 1
keyboardcontroler = Cntrl()
mousecontroler = Controller()
mousepos = (800, 600)
placeholder = ""
y = "◙"
z = "○"
commandqueue = ""

def Clicker(Time, mousebutton):
    mouse = Controller()
    time.sleep(time_sleep)
    selected_time = Time
    selected_time = float(selected_time)
    mousebutton = mousebutton.split(" ")[0]
    pressed_button = "Button." + mousebutton.lower()
    z = 1
    x = int(round(time.time() * 1000))
    y = x + selected_time
    while z == 1:
        while x <= y:
            if keyboard.is_pressed(true_selected_key):
                z = 0
                break
            x = int(round(time.time() * 1000))
        mousecontroler.click(eval(pressed_button))
        x = int(round(time.time() * 1000))
        y = x + selected_time


def Presser(Time, keyboardbutton):
    try:
        time.sleep(time_sleep)
        selected_time = Time
        selected_time = float(selected_time)
        keyboardbutton = "'" + keyboardbutton + "'"
        z = 1
        x = int(round(time.time() * 1000))
        y = x + selected_time
        while z == 1:
            while x <= y:
                if keyboard.is_pressed(true_selected_key):
                    z = 0
                    break
                x = int(round(time.time() * 1000))
            keyboard.press(eval(keyboardbutton))
            x = int(round(time.time() * 1000))
            y = x + selected_time
    except:
        return False


def killbuttonrecorder():
    def on_press(key):
        if key == key:
            global selected_key
            selected_key = key
            return False
    with Listener(on_press=on_press) as listener:
        listener.join()


def changekillbutonlabel():
    global true_selected_key
    true_selected_key = str(selected_key)
    x = len(true_selected_key)
    if x >= 4:
        true_selected_key = true_selected_key[4:]
    else:
        true_selected_key = true_selected_key[1]
    killbutton2.configure(text=true_selected_key)


def mousepositionfinder():
    while True:
        if mouse.is_pressed("left"):
            global mousepos
            mousepos = mouse.get_position()
            mousepos = str(mousepos)
            mousepos = mousepos[:-1]
            mousepos = mousepos[1:]
            return mousepos


def changeposlabel():
    mouseactualpositionlabel.configure(text=mousepos)


def combinefun2():
    killbuttonrecorder()
    changekillbutonlabel()


def combinefun():
    mousepositionfinder()
    changeposlabel()


def addingnewmousewhatthingsdo(key, function, time, position):
    global numberofcomandsnumber
    if key and function and position and time != "":
        time = int(time)
        time = time / 1000
        time = str(time)
        while len(key) != 13:
            key = key + " "
        while len(function) != 12:
            function = function + " "
        while len(position) != 12:
            position = position + " "
        finallist = key + function + position + time
        listbox.insert(END, finallist)
        global commandqueue
        posx = position.split(", ")[0]
        posy = position.split(", ")[1]
        posy = posy.split(" ")[0]
        key = key.lower()
        key = key.split(" ")[0]
        function = function.lower()
        function = function.split(" ")[0]
        commandqueue = commandqueue + "time.sleep(" + time + ")" + y + "mouse.move(-10000, -10000)" + y + "mouse.move(" + posx + ", " + posy + ")" + y + "mousecontroler." + function + "(Button." + key + ")" + y
        numberofcomandsnumber = numberofcomandsnumber + 1


def addingnewkeyboardwhatthingsdo(key, function, time, position):
    global numberofcomandsnumber
    origkey = key
    time = int(time)
    time = time / 1000
    time = str(time)
    if key and function and time != "":
        try:
            while len(key) < 13:
                key = key + " "
            if len(key) > 13:
                newkey = key[:10]
                newkey =newkey + "..."
            while len(function) != 24:
                function = function + " "
            if len(key) <= 13:
                finallist = key + function + time
            else:
                finallist = newkey + function + time
            listbox.insert(END, finallist)
            global commandqueue
            function = str(function)
            function = function.lower()
            function = function.split(" ")[0]
            function = "keyboard." + function
            if len(origkey) > 1:
                function = "keyboardcontroler.type"
            key = str(key)
            key = key.split(" ")[0]
            time = str(time)
            commandqueue = commandqueue + "time.sleep(" + time + ")" + y + function + "('" + key + "')" + y
            numberofcomandsnumber = numberofcomandsnumber + 1
        except:
            pass


def removaall():
    global commandqueue
    commandqueue = ""
    listbox.delete(0,'end')


def removelastwidget():
    global numberofcomandsnumber
    listbox.delete(numberofcomandsnumber - 1)


def removelast():
    removelastwidget()
    global commandqueue
    global numberofcomandsnumber
    if commandqueue != "":
        newcommandqueue = commandqueue.split(y)
        numberofcommands2 = len(newcommandqueue)
        firstletter = newcommandqueue[numberofcommands2 - 2]
        firstletter = firstletter[0]
        if firstletter == "k":
            del newcommandqueue[numberofcommands2-2]
            del newcommandqueue[numberofcommands2-3]
            commandqueue = y.join(newcommandqueue)
            if numberofcommands2 == 3:
                commandqueue = ""
        else:
            del newcommandqueue[numberofcommands2 - 2]
            del newcommandqueue[numberofcommands2 - 3]
            del newcommandqueue[numberofcommands2 - 4]
            del newcommandqueue[numberofcommands2 - 5]
            commandqueue = y.join(newcommandqueue)
            if numberofcommands2 == 5:
                commandqueue = ""
        numberofcomandsnumber = numberofcomandsnumber - 1
        print(numberofcomandsnumber)
    else:
        return False


def executecode():
    global stopvariable
    commandsvariable = 0
    g = commandqueue.split(y)
    for i in g:
        try:
            someshit = g[commandsvariable]
            someshit1 = someshit[0]
            someshittime = someshit.split("(")[1]
            someshittime = someshittime.split(")")[0]
            if someshit1 == "t":
                sometime = someshittime
                sometime = float(sometime)
                sometime = sometime * 1000
                x = int(round(time.time() * 1000))
                d = x + sometime
                while x <= d:
                    if keyboard.is_pressed(selected_key):
                        stopvariable = 0
                        break
                    x = int(round(time.time() * 1000))
                commandsvariable = commandsvariable + 1
            else:
                if keyboard.is_pressed(selected_key):
                    stopvariable = 0
                    break
                exec(g[commandsvariable])
                if keyboard.is_pressed(selected_key):
                    stopvariable = 0
                    break
                commandsvariable = commandsvariable + 1
        except:
            return False


def executetimes(times, repeats):
    try:
        if repeats == 1:
            for i in range(1):
                executecode()
        if repeats == 2:
            times = int(times)
            for i in range(times):
                executecode()
        if repeats == 3:
            global stopvariable
            stopvariable = 1
            while stopvariable == 1:
                executecode()

    except:
        return False


def recordkeyboard():
    global commandqueue
    global timernkey
    while True:
        recordedkey = keyboard.read_key()
        if recordedkey == selected_key:
            break
        else:
            timernkey = int(round(time.time() * 1000))
            timeforcommandqueue = timernkey - timern
            commandqueue = commandqueue + "time.sleep(" + timeforcommandqueue + ")" + y + "keyboard.press(" + recordedkey + ")" + y




def recordmouse():
    global commandqueue
    global timernmouse
    while True:
        if mouse.is_pressed("left"):
            buttonmouse = "left"
            recordedmousepos = mouse.get_position()
            timernmouse = int(round(time.time() * 1000))
            timemousecommandqueue = timernmouse - timern
            commandqueue = commandqueue + "time.sleep(" + timemousecommandqueue + ")" + y + "mouse.move(" + recordedmousepos + ")" + y + "mouse.click(Button="
        if mouse.is_pressed("right"):
            buttonmouse = "right"
            recordedmousepos = mouse.get_position()
            timernmouse = int(round(time.time() * 1000))
        if keyboard.is_pressed(selected_key):
            break


def recordall():
    global timern
    timern = int(round(time.time() * 1000))
    if __name__ == '__main__':
        p1 = multiprocessing.Process(target=recordmouse)
        p2 = multiprocessing.Process(target=recordkeyboard)
        p1.start()
        p2.start()
        p1.join()
        p2.join()


root = tk.Tk()
root.title("Clicker")
root.geometry("500x700")
mainlabel = tk.Label(root, bd=1, relief="solid")
mainlabel.place(relwidth=1, relheight=1, relx=0, rely=0)

mouselabel = tk.Label(mainlabel, bd=1, text="Mouse", relief="solid")
mouselabel.place(relwidth=0.2, relheight=0.05)

mousekeylabelinfo = tk.Label(mainlabel)
mousekeylabelinfo.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.075)
mousekeylabelinfotext = tk.Label(mousekeylabelinfo, text="Choose key")
mousekeylabelinfotext.place(relwidth=0.6, relheight=1, relx=0, rely=0)
mousekeylabelinfocombobox = ttk.Combobox(mousekeylabelinfo, values=["Left click", "Right click"])
mousekeylabelinfocombobox.place(relwidth=0.2, relheight=1, relx=0.725, rely=0)
mousekeylabelinfocombobox.current(0)

mouselabelinfo = tk.Label(mainlabel)
mouselabelinfo.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.125)
mouselabelinfotext = tk.Label(mouselabelinfo, text="Click every (ms)")
mouselabelinfotext.place(relwidth=0.6, relheight=1, relx=0, rely=0)
mouselabelinfoentry = tk.Entry(mouselabelinfo, bd=1, relief="solid")
mouselabelinfoentry.place(relwidth=0.15, relheight=1, relx=0.6, rely=0)
mouselabelinfobutton = tk.Button(mouselabelinfo, text="Click!", bd=1, relief="solid", command=lambda: Clicker(mouselabelinfoentry.get(), mousekeylabelinfocombobox.get()))
mouselabelinfobutton.place(relwidth=0.1, relheight=1, relx=0.9, rely=0)
mousekeylabelinfo = tk.Label(mainlabel)

keyboardlabel = tk.Label(mainlabel, bd=1, text="Keyboard", relief="solid")
keyboardlabel.place(relwidth=0.2, relheight=0.05, rely=0.2)

keyboardkeylabelinfo = tk.Label(mainlabel)
keyboardkeylabelinfo.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.275)
keyboardkeylabelinfotext = tk.Label(keyboardkeylabelinfo, text="Choose key")
keyboardkeylabelinfotext.place(relwidth=0.6, relheight=1, relx=0, rely=0)
keyboardkeylabelinfoentry = tk.Entry(keyboardkeylabelinfo, bd=1, relief="solid")
keyboardkeylabelinfoentry.place(relwidth=0.2, relheight=1, relx=0.725, rely=0)

keyboardlabelinfo = tk.Label(mainlabel)
keyboardlabelinfo.place(relwidth=0.8, relheight=0.05, relx=0.1, rely=0.325)
keyboardlabelinfotext = tk.Label(keyboardlabelinfo, text="Press every (ms)")
keyboardlabelinfotext.place(relwidth=0.6, relheight=1, relx=0, rely=0)
keyboardlabelinfoentry = tk.Entry(keyboardlabelinfo, bd=1, relief="solid")
keyboardlabelinfoentry.place(relwidth=0.15, relheight=1, relx=0.6, rely=0)
keyboardlabelinfobutton = tk.Button(keyboardlabelinfo, text="Press!", bd=1, relief="solid", command=lambda: Presser(keyboardlabelinfoentry.get(), keyboardkeylabelinfoentry.get()))
keyboardlabelinfobutton.place(relwidth=0.1, relheight=1, relx=0.9, rely=0)

endkeylabel = tk.Label(mainlabel, text="Kill button")
endkeylabel.place(relheight=0.05, relwidth=0.3, relx=0.05, rely=0.4)
endkeybutton = tk.Button(mainlabel, bd=1, relief="solid", text="Record", command=lambda: combinefun2())
endkeybutton.place(relheight=0.05, relwidth=0.3, relx=0.3, rely=0.4)
killbutton = tk.Label(mainlabel, text="Current: ")
killbutton.place(relheight=0.05, relwidth=0.15, relx=0.65, rely=0.4)
killbutton2 = tk.Label(mainlabel, text="Esc")
killbutton2.place(relheight=0.05, relwidth=0.1, relx=0.78, rely=0.4)


eventslabel = tk.Label(mainlabel, bd=1, relief="solid")
eventslabel.place(relwidth=0.6, relheight=0.5, relx=0.06, rely=0.47)
scrollbar = Scrollbar(eventslabel)
scrollbar.place(anchor="ne", relheight=0.73, relx=1, rely=0.2)
listbox = Listbox(eventslabel, yscrollcommand=scrollbar.set, bd=1, relief="solid", font=("Consolas", "8"))
listbox.place(relwidth=0.95, relheight=0.73, rely=0.2)
scrollbar.config(command=listbox.yview)
eventstitle = tk.Label(eventslabel, text="Events", bd=1, relief="solid")
eventstitle.place(relwidth=0.3, relheight=0.1, relx=0.35)
removelastbutton = tk.Button(eventslabel, text="Remove last", bd=1, relief="solid", command=lambda: removelast())
removelastbutton.place(relwidth=0.35, relheight=0.1)
removeallbutton = tk.Button(eventslabel, text="Remove all", bd=1, relief="solid", command=lambda: removaall())
removeallbutton.place(relwidth=0.35, relheight=0.1, relx=0.65)
whatthingsdokey = tk.Label(eventslabel, text="Key", bd=1, relief="solid")
whatthingsdokey.place(rely=0.1, relwidth=0.25, relheight=0.1)
whatthingsdofunction = tk.Label(eventslabel, text="Function", bd=1, relief="solid")
whatthingsdofunction.place(rely=0.1, relwidth=0.25, relheight=0.1, relx=0.25)
whatthingsdoposition = tk.Label(eventslabel, text="Position", bd=1, relief="solid")
whatthingsdoposition.place(rely=0.1, relwidth=0.25, relheight=0.1, relx=0.5)
whatthingsdotime = tk.Label(eventslabel, text="Time", bd=1, relief="solid")
whatthingsdotime.place(rely=0.1, relwidth=0.25, relheight=0.1, relx=0.75)


finaladding = tk.Label(eventslabel)
finaladding.place(rely=0.93, relwidth=1, relheight=0.07)
repeats = IntVar()
once = ttk.Radiobutton(finaladding, text='Once', variable=repeats, value=1)
once.place(relx=0, relheight=1)
howmanytimes = ttk.Radiobutton(finaladding, text='          Times', variable=repeats, value=2)
howmanytimes.place(relx=0.2, relheight=1)
untilstopped = ttk.Radiobutton(finaladding, text='Until stopped', variable=repeats, value=3)
untilstopped.place(relx=0.5, relheight=1)
howmanytimesentry = tk.Entry(finaladding, bd=1, relief="solid")
howmanytimesentry.place(relwidth=0.1, relheight=1, relx=0.265, rely=0)
finaladdbutton = tk.Button(finaladding, bd=1, relief="solid", text="Execute", command=lambda: executetimes(howmanytimesentry.get(), repeats.get()))
finaladdbutton.place(relwidth=0.17, relheight=1, rely=0, relx=0.83)


addingeventslabel = tk.Label(mainlabel, bd=1, relief="solid")
addingeventslabel.place(relwidth=0.25, relheight=0.45, relx=0.69, rely=0.47)

addmouseevents = tk.Label(addingeventslabel)
addmouseevents.place(relwidth=1, relheight=0.5)

mouselabelevents = tk.Label(addmouseevents, text="Mouse")
mouselabelevents.place(relheight=0.34, relwidth=1)

mouseeventshouse = tk.Label(addmouseevents)
mouseeventshouse.place(relwidth=1, relheight=0.55, rely=0.34)


mouseeventskey = tk.Label(mouseeventshouse, bd=1, relief="solid")
mouseeventskey.place(relwidth=0.5, relheight=0.5, relx=0, rely=0)
mousekeylabel = tk.Label(mouseeventskey, text="Key", font=("Helvetica", "8"))
mousekeylabel.place(relwidth=0.4, relheight=0.5, relx=0.1, rely=0)
mousekeyselection = ttk.Combobox(mouseeventskey, font=("Helvetica", "7"), values=["Left click", "Right click"])
mousekeyselection.place(relwidth=1, relheight=0.4, relx=0, rely=0.55)
mousekeyselection.current(0)


mouseeventsfunction = tk.Label(mouseeventshouse, bd=1, relief="solid")
mouseeventsfunction.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0)
mousefunctionlabel = tk.Label(mouseeventsfunction, text="Function", font=("Helvetica", "8"))
mousefunctionlabel.place(relwidth=0.8, relheight=0.5, relx=0.05, rely=0)
mousefunctionselection = ttk.Combobox(mouseeventsfunction, font=("Helvetica", "8"), values=["Click", "Press", "Release"])
mousefunctionselection.place(relwidth=0.9, relheight=0.4, relx=0.05, rely=0.55)
mousefunctionselection.current(0)


mouseeventsposition = tk.Label(mouseeventshouse, bd=1, relief="solid")
mouseeventsposition.place(relwidth=0.5, relheight=0.5, relx=0, rely=0.5)
mousepositionlabel = tk.Label(mouseeventsposition, text="Position", font=("Helvetica", "8"))
mousepositionlabel.place(relwidth=1, relheight=0.3, relx=0, rely=0)
mousepositionbutton = tk.Button(mouseeventsposition, bd=1, relief="solid", font=("Helvetica", "8"), text="Configure", command=lambda: combinefun())
mousepositionbutton.place(relwidth=0.9, relheight=0.4, relx=0.05, rely=0.3)
mouseactualpositionlabel = tk.Label(mouseeventsposition, text="")
mouseactualpositionlabel.place(rely=0.7, relheight=0.3, relwidth=1)

mouseeventstime = tk.Label(mouseeventshouse, bd=1, relief="solid")
mouseeventstime.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0.5)
mousetimelabel = tk.Label(mouseeventstime, text="Time (ms)", font=("Helvetica", "7"))
mousetimelabel.place(relwidth=0.8, relheight=0.5, relx=0.05, rely=0)
mousetimeentry = tk.Entry(mouseeventstime, bd=1, relief="solid")
mousetimeentry.place(relwidth=0.9, relheight=0.4, relx=0.05, rely=0.55)

mouseeventsadd = tk.Button(addmouseevents, bd=1, relief="solid", text="Add", command=lambda: addingnewmousewhatthingsdo(mousekeyselection.get(), mousefunctionselection.get(), mousetimeentry.get(), mouseactualpositionlabel.cget("text")))
mouseeventsadd.place(rely=0.89, relheight=0.11, relwidth=1)

addkeyboardevents = tk.Label(addingeventslabel)
addkeyboardevents.place(relwidth=1, relheight=0.5, rely=0.5)
keyboardlabelevents = tk.Label(addkeyboardevents, text="Keyboard")
keyboardlabelevents.place(relheight=0.34, relwidth=1)
keyboardeventshouse = tk.Label(addkeyboardevents)
keyboardeventshouse.place(relwidth=1, relheight=0.55, rely=0.34)

keyboardeventskey = tk.Label(keyboardeventshouse, bd=1, relief="solid")
keyboardeventskey.place(relwidth=0.5, relheight=0.5, relx=0, rely=0)
keyboardkeylabel = tk.Label(keyboardeventskey, text="Key(s)", font=("Helvetica", "8"))
keyboardkeylabel.place(relwidth=0.6, relheight=0.5, relx=0.1, rely=0)
keyboardkeyentry = tk.Entry(keyboardeventskey, font=("Helvetica", "7"), bd=1, relief="solid")
keyboardkeyentry.place(relwidth=0.9, relheight=0.4, relx=0.05, rely=0.55)

keyboardeventsfunction = tk.Label(keyboardeventshouse, bd=1, relief="solid")
keyboardeventsfunction.place(relwidth=0.5, relheight=0.5, relx=0.5, rely=0)
keyboardfunctionlabel = tk.Label(keyboardeventsfunction, text="Function", font=("Helvetica", "8"))
keyboardfunctionlabel.place(relwidth=0.8, relheight=0.5, relx=0.05, rely=0)
keyboardfunctionselection = ttk.Combobox(keyboardeventsfunction, font=("Helvetica", "8"), values=["Press"])
keyboardfunctionselection.place(relwidth=0.9, relheight=0.4, relx=0.05, rely=0.55)
keyboardfunctionselection.current(0)

keyboardeventstime = tk.Label(keyboardeventshouse, bd=1, relief="solid")
keyboardeventstime.place(relwidth=1, relheight=0.5, rely=0.5)
keyboardtimelabel = tk.Label(keyboardeventstime, text="Time (ms)", font=("Helvetica", "7"))
keyboardtimelabel.place(relwidth=0.8, relheight=0.5, relx=0.05, rely=0)
keyboardtimeentry = tk.Entry(keyboardeventstime, bd=1, relief="solid")
keyboardtimeentry.place(relwidth=0.9, relheight=0.35, relx=0.05, rely=0.5)

keyboardeventsadd = tk.Button(addkeyboardevents, bd=1, relief="solid", text="Add", command=lambda : addingnewkeyboardwhatthingsdo(keyboardkeyentry.get(), keyboardfunctionselection.get(), keyboardtimeentry.get(), placeholder))
keyboardeventsadd.place(rely=0.89, relheight=0.11, relwidth=1)

recordallbuton = tk.Button(mainlabel, text="Record all", bd=1, relief="solid")
recordallbuton.place(relwidth=0.25, relheight=0.04, relx=0.69, rely=0.93)

root.mainloop()


