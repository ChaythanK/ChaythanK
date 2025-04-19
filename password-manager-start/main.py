from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# setting up window & canvas
window = Tk()
canvas = Canvas(width=200, height=200,)

# placing elements of screen below
window.config(padx = 20, pady = 20)
window.title("password manager")
logo = PhotoImage(file="logo.png")
img = canvas.create_image(100,100, image=logo)
canvas.grid(column = 2, row = 1)
#img setup done above

#-------------------------WEBSITE ENTRY BLOCK---------------------#
website_label = Label(width = 15, text="Website")
website_label.grid(column = 1, row = 2)

#Entry
website_entry = Entry(width=35)
#Add some text to begin with
website_entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(website_entry.get())
website_entry.grid(column = 2, row = 2, columnspan = 2, sticky='w')#sticky "w" tells it to have a left align

#----------------------USERNAME ENTRY BLOCK -------------------------#
username_label = Label(text = "Password")
username_label.grid(column = 1, row = 4)

#Entry
username_entry = Entry(width=35)
#Add some text to begin with
username_entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(username_entry.get())
username_entry.grid(column=2, row=3, sticky='w')#sticky "w" tells it to have a left align
window.columnconfigure(2, minsize=21)

#----------------------PASSWORD ENTRY BLOCK-------------------------- #
password_label = Label(text="Email/Username")
password_label.grid(column = 1, row = 3)

#Entry
password_entry = Entry(width=21)
#Add some text to begin with
password_entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(password_entry.get())
password_entry.grid(column = 2, row = 4, sticky='w')#sticky "w" tells it to have a left align

def if_pressed():
    print(website_entry.get())
    print(username_entry.get())
    print(password_entry.get())

password_button = Button(text="Generate Password", command=if_pressed)#button
password_button.grid(column = 3, row = 4,)
window.columnconfigure(3, minsize = 15)
window.columnconfigure(2, minsize = 21)

window.mainloop()
