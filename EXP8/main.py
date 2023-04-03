import tkinter as tk
from PIL import ImageTk, Image
import calendar
from datetime import date


def registration_form():
    win = tk.Tk()
    win.title('Registration Form')
    win.geometry('640x480')

    label_title = tk.Label(win, text="Registration Form")
    label_title.config(font=('Helvetica bold', 40))

    label2_fullname = tk.Label(win, text="Full Name")
    label3_email = tk.Label(win, text="Email")
    label4_gender = tk.Label(win, text="Gender")
    label5_country = tk.Label(win, text="Country")
    label6_programming = tk.Label(win, text="Programming")

    label_title.place(x=100, y=25)
    label2_fullname.place(x=160, y=140)
    label3_email.place(x=160, y=180)
    label4_gender.place(x=160, y=220)
    label5_country.place(x=160, y=260)
    label6_programming.place(x=160, y=300)

    fullname = tk.Entry(win, width=25)
    fullname.place(x=330, y=140)

    email = tk.Entry(win, width=25)
    email.place(x=330, y=180)
    i = tk.IntVar()
    male = tk.Radiobutton(win, text="Male", value=1, variable=i)
    female = tk.Radiobutton(win, text="Female", value=2, variable=i)
    other = tk.Radiobutton(win, text="Other", value=3, variable=i)
    male.place(x=330, y=220)
    female.place(x=405, y=220)
    other.place(x=480, y=220)

    j = tk.IntVar()
    k = tk.IntVar()
    java_check = tk.Checkbutton(win, text="Java", variable=j)
    java_check.place(x=330, y=300)
    python_check = tk.Checkbutton(win, text="Python", variable=k)
    python_check.place(x=410, y=300)

    menu = tk.StringVar()
    menu.set("Select Your Country")
    dropdown = tk.OptionMenu(win, menu, "United States", "Canada", "Afghanistan", "Albania", "Algeria",
                             "American Samoa",
                             "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and/or Barbuda", "Argentina",
                             "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
                             "Bangladesh",
                             "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia",
                             "Bosnia and Herzegovina", "Botswana", "Bouvet Island", "Brazil",
                             "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso",
                             "Burundi",
                             "Cambodia", "Cameroon", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad",
                             "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros",
                             "Congo", "Cook Islands", "Costa Rica", "Croatia (Hrvatska)", "Cuba", "Cyprus",
                             "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor",
                             "Ecudaor", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia",
                             "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji", "Finland", "France",
                             "France, Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories",
                             "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland",
                             "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti",
                             "Heard and Mc Donald Islands", "Honduras", "Hong Kong", "Hungary", "Iceland", "India",
                             "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Israel", "Italy",
                             "Ivory Coast",
                             "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati",
                             "Korea, Democratic People's Republic of", "Korea, Republic of", "Kosovo", "Kuwait",
                             "Kyrgyzstan", "Lao People's Democratic Republic", "Latvia", "Lebanon", "Lesotho",
                             "Liberia",
                             "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia",
                             "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
                             "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico",
                             "Micronesia, Federated States of", "Moldova, Republic of", "Monaco", "Mongolia",
                             "Montserrat",
                             "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
                             "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria",
                             "Niue", "Norfork Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan",
                             "Palau",
                             "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland",
                             "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda",
                             "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa",
                             "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles",
                             "Sierra Leone",
                             "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa",
                             "South Georgia South Sandwich Islands", "South Sudan", "Spain", "Sri Lanka", "St. Helena",
                             "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbarn and Jan Mayen Islands",
                             "Swaziland",
                             "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan", "Tajikistan",
                             "Tanzania, United Republic of", "Thailand", "Togo", "Tokelau", "Tonga",
                             "Trinidad and Tobago",
                             "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda",
                             "Ukraine",
                             "United Arab Emirates", "United Kingdom", "United States minor outlying islands",
                             "Uruguay",
                             "Uzbekistan", "Vanuatu", "Vatican City State", "Venezuela", "Vietnam",
                             "Virigan Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands",
                             "Western Sahara", "Yemen", "Yugoslavia", "Zaire", "Zambia", "Zimbabwe")
    dropdown.place(x=330, y=255)

    def close():
        # win.destroy()
        win.quit()

    # Create a Button to call close()
    btn = tk.Button(win, text="Submit", font=("Calibri", 14, "bold"), command=close)
    btn.place(x=280, y=380)
    win.mainloop()


def add_number_mini_task():
    win = tk.Tk()
    win.title("Number Addition")
    win.geometry('500x400')

    # labelframe
    frame = tk.LabelFrame(win, text="Number Addition", width=450, height=250, fg="Black").pack()

    # label creation
    label1 = tk.Label(win, text="First Number:")
    label2 = tk.Label(win, text="Second Number:")
    label3 = tk.Label(win, text="Result:")

    # placing the labels
    label1.place(x=50, y=50)
    label2.place(x=50, y=80)
    label3.place(x=50, y=110)

    # creation of the entry
    entry1 = tk.Entry(win)
    entry2 = tk.Entry(win)
    entry3 = tk.Entry(win)

    # entry placing
    entry1.place(x=160, y=50)
    entry2.place(x=160, y=80)
    entry3.place(x=160, y=110)

    # add function
    def add():
        a = int(entry1.get())
        b = int(entry2.get())
        c = a + b
        entry3.insert(0, c)

    # clear
    def clear():
        entry1.delete(0, "end")  # 0 to end means from start to end(all digits get cleared)
        entry2.delete(0, "end")
        entry3.delete(0, "end")

    def exit():
        quit()

    # button creation
    add_button = tk.Button(win, text="Add", width=5, height=2, command=add)
    clear_button = tk.Button(win, text="Clear", width=5, height=2, command=clear)
    exit_button = tk.Button(win, text="Exit", width=5, height=2, command=exit)

    # placing the buttons
    add_button.place(x=160, y=160)
    clear_button.place(x=260, y=160)
    exit_button.place(x=350, y=270)

    win.mainloop()


def circle():
    win = tk.Tk()
    win.title('Welcome')
    win.geometry('500x500')
    can = tk.Canvas(win)
    oval = can.create_oval(70, 70, 210, 210, fill='Blue')
    can.pack()
    oval = can.create_oval(105, 100, 125, 120, fill='Black')
    can.pack()
    oval = can.create_oval(155, 100, 175, 120, fill='Black')
    can.pack()
    oval = can.create_oval(100, 160, 180, 190, fill='Red')
    can.pack()
    win.mainloop()

circle()