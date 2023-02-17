from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator

root = Tk()
root.geometry("1080x720")
root.title("Google Translator")
root.resizable(False, False)


def translate():
    text_ = text1.get(1.0, END)
    t1 = Translator()
    trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
    trans_text = trans_text.text
    text11.delete(1.0, END)
    text11.insert(END, trans_text)


def label_changes():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_changes)


image = PhotoImage(file="arrow.png")
ilabale = Label(root, image=image, width=150)
ilabale.place(x=460, y=70)

language = googletrans.LANGUAGES
languagev = list(language.values())
lan1 = language.keys()


#COMBO1
combo1 = ttk.Combobox(root, values=languagev, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("English")
label1 = Label(root, text="English", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)


#COMBO2
combo2 = ttk.Combobox(root, values=languagev, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("Select Language")
label2 = Label(root, text="English", font="Segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)


#FRAME1
f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=430, height=210)

text1 = Text(f, font="Robote 20", bg="#F0F0F8", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scroll1 = Scrollbar(f)
scroll1.pack(side="right", fill='y')
scroll1.configure(command=text1.yview)
text1.configure(yscrollcommand=scroll1.set)



#FRAME2
f1 = Frame(root, bg="black", bd=5)
f1.place(x=620, y=118, width=430, height=210)

text11 = Text(f1, font="Robote 20", bg="#F0F0F8", relief=GROOVE, wrap=WORD)
text11.place(x=0, y=0, width=430, height=200)

scroll11 = Scrollbar(f1)
scroll11.pack(side="right", fill='y')
scroll11.configure(command=text11.yview)
text11.configure(yscrollcommand=scroll11.set)

#BUTTON

b1 = Button(root, text="Translate", font=("Roboto", 15), activebackground="#CDCDAA", cursor="hand2",
            bd=1, width=10, height=2, bg="black", fg="white", command=translate)

b1.place(x=476, y=250)

label_changes()
root.mainloop()
