from tkinter import *
from PIL import ImageTk, Image
import calendar
from datetime import date


def displayCalendar():
    month = int(month_box.get())
    year = int(year_box.get())
    output_calendar = calendar.month(year, month)
    calendar_field.delete(1.0, 'end')

    calendar_field.insert('end', output_calendar)


def reset():
    calendar_field.delete(1.0, 'end')

    month_var.set(current_month)
    year_var.set(current_year)

    month_box.config(textvariable=month_var)
    year_box.config(textvariable=year_var)


def close():
    top.destroy()


top = Tk()
top.title("Calendar")

top.geometry('500x550+650+250')
top.resizable(0, 0)

header_frame = Frame(top)
entry_frame = Frame(top)
result_frame = Frame(top)
button_frame = Frame(top)
header_frame.pack(expand=True, fill="both")
entry_frame.pack(expand=True, fill="both")
result_frame.pack(expand=True, fill="both")
button_frame.pack(expand=True, fill="both")

header_label = Label(
    header_frame,
    text="CALENDAR",
)

header_label.pack(expand=True, fill="both")

calendar_image = ImageTk.PhotoImage(Image.open(r"C:\Users\soham\PycharmProjects\C005_Python_Projects_Sem4\EXP8\calender.jpg").resize((50, 50), Image.ANTIALIAS))
image_label = Label(
    header_frame,
    image=calendar_image,
)

image_label.pack(expand=True, fill="both")

month_label = Label(
    entry_frame,
    text="Month:",
    font=("consolas", "10", "bold"),
)
year_label = Label(
    entry_frame,
    text="Year:",
    font=("consolas", "10", "bold"),
)

month_label.place(x=120, y=0)
year_label.place(x=268, y=0)
month_var = IntVar(entry_frame)
year_var = IntVar(entry_frame)
current_month = date.today().month
current_year = date.today().year
month_var.set(current_month)
year_var.set(current_year)
month_box = Spinbox(entry_frame, from_=1, to=12, width="5", textvariable=month_var)
year_box = Spinbox(entry_frame, from_=0000, to=3000, width="5", textvariable=year_var)
month_box.place(x=180, y=0)
year_box.place(x=320, y=0)
calendar_field = Text(
    result_frame,
    width=20,
    height=8,
    font=("consolas", "14"),
    relief=RIDGE,
    borderwidth=2
)
calendar_field.pack(expand=False, fill=None)

display_button = Button(
    button_frame,
    text="Show",
    command=displayCalendar
)

reset_button = Button(
    button_frame,
    text="Clear",
    command=reset
)
close_button = Button(
    button_frame,
    text="Exit",
    command=close
)
display_button.place(x=140, y=0)
reset_button.place(x=230, y=0)
close_button.place(x=305, y=0)
top.mainloop()
