import turtle
from tkinter import*
FONT_NAME = "Comic Sans MS"


canvas.config()

def if_pressed():
    print("has been pressed")
    canvas.config(width=1500, height=900)
    canvas.coords(img,750, 450,)
    canvas.delete(text)
    button.destroy()
    canvas.new_image = PhotoImage(file="night_sky.png")
    canvas.itemconfig(img, image=canvas.new_image)
    window.config(bg="black")
    canvas.config(bg="black")
    with open('Shark tank speech text', 'r') as file:
        for line in file:
            if "header" in line:  # Check if "header" exists in the line
                print(line)
                header = ""
                for word in line.split():
                    if word != "header":
                        header +=word
                print(header)

            if "b"==line[0] and "o"==line[1] and "d"==line[2]:
                print(line)

    canvas.create_text(750, 100, text=str(header), fill="white", font=(FONT_NAME, 50,))



button = Button(text="next",fg="white", bg="dark blue", font = ("Comic Sans MS",15, "bold"), command= if_pressed)
button.grid(column = 2, row = 3)

window.mainloop()