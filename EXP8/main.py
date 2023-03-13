import tkinter as tk

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
dropdown = tk.OptionMenu(win, menu, "United States", "Canada", "Afghanistan", "Albania", "Algeria", "American Samoa",
                         "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and/or Barbuda", "Argentina",
                         "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh",
                         "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia",
                         "Bosnia and Herzegovina", "Botswana", "Bouvet Island", "Brazil",
                         "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi",
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
                         "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Israel", "Italy", "Ivory Coast",
                         "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati",
                         "Korea, Democratic People's Republic of", "Korea, Republic of", "Kosovo", "Kuwait",
                         "Kyrgyzstan", "Lao People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia",
                         "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia",
                         "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
                         "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico",
                         "Micronesia, Federated States of", "Moldova, Republic of", "Monaco", "Mongolia", "Montserrat",
                         "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
                         "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria",
                         "Niue", "Norfork Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau",
                         "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland",
                         "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda",
                         "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa",
                         "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone",
                         "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa",
                         "South Georgia South Sandwich Islands", "South Sudan", "Spain", "Sri Lanka", "St. Helena",
                         "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbarn and Jan Mayen Islands", "Swaziland",
                         "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan", "Tajikistan",
                         "Tanzania, United Republic of", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago",
                         "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine",
                         "United Arab Emirates", "United Kingdom", "United States minor outlying islands", "Uruguay",
                         "Uzbekistan", "Vanuatu", "Vatican City State", "Venezuela", "Vietnam",
                         "Virigan Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands",
                         "Western Sahara", "Yemen", "Yugoslavia", "Zaire", "Zambia", "Zimbabwe")
dropdown.place(x=330, y=255)


def close():
    # win.destroy()
    win.quit()


# Create a Button to call close()
btn = tk.Button(win, text="Submit", font=("Calibri", 14, "bold"), command=close)
btn.place(x=280,y=380)
win.mainloop()


