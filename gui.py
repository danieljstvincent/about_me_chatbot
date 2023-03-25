import tkinter
from tkinter import *


def send():
    msg = TextEntryBox.get("1.0", 'end-1c').strip()
    TextEntryBox.delete('1.0', 'end')

    # if msg
base = Tk()
base.title("About me (Daniel St. Vincent)")
base.geometry("400x500")
base.resizable(width=False, height=False)


ChatHistory = Text(base, bd=0, bg='white', font='Arial')
ChatHistory.config(state=DISABLED)

SendButton = Button(base, font=('Arial', 12, 'bold'), text="Send", bg="#dfdfdf", activebackground="#3e3e3e", fg='#ffffff', command=send)

TextEntryBox = Text(base, bd=0, bg='white', font='Arial')

ChatHistory.place(x=376, y=6, height=386, width=376)
TextEntryBox.place(x=128, y=400, height=80, width=265)
SendButton.place(x=6, y=400, height=80, width=125)

base.mainloop()

