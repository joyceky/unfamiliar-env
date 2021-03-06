#Imports for tkinter gui library
import tkinter
from tkinter import *
from tkinter.scrolledtext import *
import tkinter.filedialog
import tkinter.messagebox

# Create a basic window with text-editing capabilities
root = tkinter.Tk(className="note")
editor = tkinter.scrolledtext.ScrolledText(root, width=100, height=80)

# defining menu commands
def open_command():
    file = tkinter.filedialog.askopenfile(parent=root,mode='rb',title="Select a file")
    if file != None:
        contents = file.read()
        editor.insert('1.0',contents)
        file.close()

def save_command():
    file = tkinter.filedialog.asksaveasfile(mode="w")
    if file != None:
        usertext = str(editor.get(1.0, END))
        file.write(usertext)
        file.close()

def exit_command():
    if tkinter.messagebox.askokcancel("Quit", "Press ok to leave note"):
        root.destroy()

def about_command():
    label = tkinter.messagebox.showinfo("About", "A simple note-taking app written with Python and tkinter")

# creates the basic menu
menu = tkinter.Menu(root)
root.config(menu=menu)

filemenu = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)

helpmenu = tkinter.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)
# end of the menu

editor.pack()
root.mainloop()
