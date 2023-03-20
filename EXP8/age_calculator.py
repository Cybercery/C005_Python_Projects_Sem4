import tkinter as tk

win = tk.Tk()
win.geometry("500x800")
win.title("Age Calculator")
win.configure(bg="#56d4cc")
label1 = tk.Label(win, text="Date of Birth", bg="red", height=2, width=10)
label1.place(x=80, y=1)

label3 = tk.Label(win, text="Day", bg="#56d4cc")
label3.place(x=10, y=50)
ent1 = tk.Entry(win)
ent1.place(x=50, y=50)

label4 = tk.Label(win, text="Month", bg="#56d4cc")
label4.place(x=5, y=75)
ent2 = tk.Entry(win)
ent2.place(x=50, y=75)

label5 = tk.Label(win, text="Year", bg="#56d4cc")
label5.place(x=5, y=100)
ent3 = tk.Entry(win)
ent3.place(x=50, y=100)

label2 = tk.Label(win, text="Given Date", bg="red", height=2, width=10)
label2.place(x=350, y=1)

label6 = tk.Label(win, text=" Given Day", bg="#56d4cc")
label6.place(x=250, y=50)
ent4 = tk.Entry(win)
ent4.place(x=330, y=50)

label7 = tk.Label(win, text="Given Month", bg="#56d4cc")
label7.place(x=245, y=75)

ent5 = tk.Entry(win)
ent5.place(x=330, y=75)
label8 = tk.Label(win, text="Given Year", bg="#56d4cc")
label8.place(x=250, y=100)
ent6 = tk.Entry(win)
ent6.place(x=330, y=100)

win.mainloop()


def checkError():
    if (ent1.get() == "" or ent2.get() == ""
            or ent3.get() == "" or ent4.get() == ""
            or ent5.get() == "" or ent6.get() == ""):
        tk.messagebox.showerror("Input Error")

        clearAll()

        return -1


