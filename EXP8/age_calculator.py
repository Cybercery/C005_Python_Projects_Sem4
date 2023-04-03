import tkinter as tk

win = tk.Tk()
win.geometry("500x500")
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


def checkError():
    if (ent1.get() == "" or ent2.get() == ""
            or ent3.get() == "" or ent4.get() == ""
            or ent5.get() == "" or ent6.get() == ""):
        tk.messagebox.showerror("Input Error")

        return -1


def calculateAge():
    value = checkError()
    if value == -1:
        return
    else:
        birth_day = int(ent1.get())
        birth_month = int(ent2.get())
        birth_year = int(ent3.get())

        given_day = int(ent4.get())
        given_month = int(ent5.get())
        given_year = int(ent6.get())
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if birth_day > given_day:
            given_month = given_month - 1
            given_day = given_day + month[birth_month - 1]

        if birth_month > given_month:
            given_year = given_year - 1
            given_month = given_month + 12

        calculated_day = given_day - birth_day
        calculated_month = given_month - birth_month
        calculated_year = given_year - birth_year

        ent9.insert(10, str(calculated_day))
        ent8.insert(10, str(calculated_month))
        ent7.insert(10, str(calculated_year))


button1 = tk.Button(win, text="Resultant Age", bg="black", fg="white", command=calculateAge)
button1.place(x=175, y=150)

label9 = tk.Label(win, text="Years", bg="#56d4cc")
label9.place(x=200, y=200)

ent7 = tk.Entry(win)
ent7.place(x=150, y=225)

label10 = tk.Label(win, text = "Months", bg="#56d4cc")
label10.place(x=195, y=250)

ent8 = tk.Entry(win)
ent8.place(x=150, y=275)

label11 = tk.Label(win, text="Days", bg="#56d4cc")
label11.place(x=200, y=300)

ent9 = tk.Entry(win)
ent9.place(x=150, y=325)

button3 = tk.Button(win, text="Clear All", bg="black", fg="white")
button3.place(x=190, y=350)

win.mainloop()
