"""Audiobook maker

This app lets you take any file and it will read it out for you.
You can also select what page you want to be read.
"""

import pyttsx3
import PyPDF2
from tkinter import filedialog
import os
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
apps = []


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File")
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


def readPdf():
    ROOT = tk.Tk()
    ROOT.withdraw()
    # the input dialog
    FILE_INP = str(simpledialog.askstring(title="Select File",
                                          prompt="Input File Name:"))
    USER_INP = int(simpledialog.askstring(title="Select Page",
                                          prompt="Input the page number:"))
    page_number = USER_INP
    book = open(FILE_INP, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    # pages = pdfReader.numPages
    speaker = pyttsx3.init()
    page = pdfReader.getPage(USER_INP)
    text = page.extractText()
    speaker.say(text)

    while USER_INP == page_number:
        if USER_INP == page_number:
            for x in range(1):
                speaker.runAndWait()
        else:
            speaker.stop()
        break


def stopVoice():
    root.destroy()


canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()

stopVoice = tk.Button(root, text="Exit", padx=10, pady=5, fg="white", bg="#263D42",
                      command=stopVoice)
stopVoice.pack()

readPdf = tk.Button(root, text="Select File&Page", padx=10, pady=5, fg="white", bg="#263D42", command=readPdf)
readPdf.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
