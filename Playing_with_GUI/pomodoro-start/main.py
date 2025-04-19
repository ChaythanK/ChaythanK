from ctypes import DEFAULT_MODE
from gettext import textdomain
from idlelib.colorizer import color_config
from tkinter import *
import time
from unittest.mock import DEFAULT
# from Playing_with_GUI.Other_Tkinter_Widgets import button
pomodoros = 1
# ---------------------------- CONSTANTS ------------------------------- #
ct=1
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

DARK_MODE = [
    "#1A3636",
    "#677D6A",
    "#40534C",
    "#D6BD98",
]

LEMONADE_VIBES = [
    "#006769",
    "#40A578",
    "#9DDE8B",
    "#E6FF94",
]

COLOR_STYLE = DARK_MODE
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer(total_seconds):
    if total_seconds >= 0:
        mins = total_seconds // 60
        secs = total_seconds % 60
        current_time = f"{mins}:{secs:02d}"  # Ensures two-digit seconds format
        canvas.itemconfig(time_display, text=current_time)  # Update display

        # Schedule the next update after 1000ms (1 second)
        window.after(1000, timer, total_seconds-1)
    else:
        global pomodoros
        pomodoros += 1  # Increment pomodoro count after timer finishes

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# ---------------------------- UI SETUP ------------------------------- #

moods = ["Locked IN", "Time for a break", "Chilling...", "STOP CHILLING!"]
setting = ["color", "text", "time"]

for i in range(ct):
    if i == 0:
        setting[0] = 0
        setting[1] = moods[0]
        setting[2] = 25
    elif i == 1:
        setting[0] = 0
        setting[1] = moods[1]
        setting[2] = 0
    elif i == 2:
        setting[0] = 2
        setting[1] = moods[2]
        setting[2] = 5
    elif i == 3:
        setting[0] = 2
        setting[1] = moods[3]
        setting[2] = 0


window = Tk()
window.title("pomodoro")
window.configure(padx=100,pady=50, bg=COLOR_STYLE[setting[0]])
canvas = Canvas(width=200, height=224,bg=COLOR_STYLE[setting[0]], highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato)
time_display = canvas.create_text(95,124, text="00:00",fill=COLOR_STYLE[-1], font=(FONT_NAME,22,"bold"),)
canvas.grid(column=2, row=2)
canvas.config()


for i in range(pomodoros):
    label = Label(text="✔",font=(FONT_NAME,15,"bold"),foreground=COLOR_STYLE[1])
    label.config(bg=COLOR_STYLE[setting[0]],)
    label.grid(column=2, row=3+i)

#Labels
label = Label(text=setting[1],font=(FONT_NAME,22,"bold"),foreground=COLOR_STYLE[1])
label.config(bg=COLOR_STYLE[setting[0]],)
label.grid(column=2, row=1)

#functions to be called by the start and reset buttons-
def reset():
    global ct
    print("Do something")
    ct+=1
    for i in range(ct):
        if ct>3:
            ct-=3
        else:
            pass
        if i == 0:
            setting[0] = 0
            setting[1] = moods[0]
            setting[2] = 25
        elif i == 1:
            setting[0] = 0
            setting[1] = moods[1]
            setting[2] = 0
        elif i == 2:
            setting[0] = 2
            setting[1] = moods[2]
            setting[2] = 5
        elif i == 3:
            setting[0] = 2
            setting[1] = moods[3]
            setting[2] = 0

    window.configure(bg=COLOR_STYLE[setting[0]])
    canvas.config(bg=COLOR_STYLE[setting[0]])

    label = Label(text=setting[1], font=(FONT_NAME, 22, "bold"), foreground=COLOR_STYLE[1])
    label.config(bg=COLOR_STYLE[setting[0]], )
    label.grid(column=2, row=1)
    for i in range(pomodoros):
        label = Label(text="✔", font=(FONT_NAME, 15, "bold"), foreground=COLOR_STYLE[1])
        label.config(bg=COLOR_STYLE[setting[0]], )
        label.grid(column=2, row=3 + i)
    timer(setting[2]*60)
    print(ct)



def start():
    global ct
    print("Do something")

#start and reset buttons
start_button = Button(text="Start", font=(FONT_NAME,10,"bold"), foreground="black", highlightthickness=0, command=start)
start_button.grid(column=1,row=3)
reset_button = Button(text="Reset", font=(FONT_NAME,10,"bold"), foreground="black", highlightthickness=0, command=reset)
reset_button.grid(column=3,row=3)

if ct==1:
    timer(25*60)
    print(ct)

window.mainloop()
#imp!!