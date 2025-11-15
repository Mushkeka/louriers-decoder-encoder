import tkinter as tk
import base64
from tkinter import Button as btn, Label as lbl, Text as txt, messagebox as mb


root = tk.Tk()
root.title('encoder/decoder')

def decode():
    s = text.get(1.0, 'end-1c')
    try:
        decode = base64.b64decode(s.encode()).decode()
        text.delete(1.0, 'end')
        text.insert('end', decode)
    except Exception as a:
        mb.showerror('Error', "Can't decode.")


def encode():
    s = text.get(1.0, 'end-1c')
    encode = base64.b64encode(s.encode()).decode()
    text.delete(1.0, 'end')
    text.insert('end', encode)

def copyText():
    s = text.get(1.0, 'end-1c')
    root.clipboard_clear()          
    root.clipboard_append(s)
    mb.showinfo('info', "text copied to clipboard.")

def textdelete(event):
    text.delete(1.0, 'end')

text = txt(width=54, height=9, wrap="word", background='light gray', font=('Arial', 12))
text.grid(row=0, column=0, columnspan=3)
text.insert(1.0, 'Type or paste text here.')

btn_1 = btn(text="Encode.", command=encode, background='light gray')
btn_1.grid(row=5, column=0, pady=5)

btn_2 = btn(text="Decode.", command=decode, background='light gray')
btn_2.grid(row=5,column=1,pady=5)

btn_copy = btn(text='Copy.', command=copyText, background='light gray')
btn_copy.grid(row=5, column=2,pady=5)

text.bind('<Button-1>', textdelete)

root.mainloop()
