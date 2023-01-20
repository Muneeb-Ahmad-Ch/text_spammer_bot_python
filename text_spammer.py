### About Me ########################################
#   Coded By : Muneeb Ahmad                         #
#   Github Link: https://github.com/Muneeb-Ahmad-Ch #
#####################################################

from tkinter import *
import tkinter
from pynput.keyboard import Key, Controller
import time

window = tkinter.Tk()
global text
global count
global start_delay
global delay

window.title("Text Spammer Bot")
window.resizable(0, 0)
window.geometry("500x520+400+120")
window.iconbitmap('assets/bot_logo.ico')

# chat bot logo
logo = PhotoImage(file="assets/bot_logo.png")
logo_label = Label(window, image=logo).pack()

version_label = Label(
    window, text="Version: 1.0", font=("Times", "10"), )
version_label.place(x=214, y=118)
version_label.configure(foreground="dark red")


info_label = Label(window, text=" Created by Muneeb.", font=("Times", "11"))
info_label.place(x=30, y=480)

# text input label
text_label = Label(window, text="Enter Text :", font=("Times", "15"))
text_label.place(x=25, y=130)

# counter text label
counter_label = Label(
    window, text="Counter Number :", font=("Times", "15"))
counter_label.place(x=25, y=300)

# start_delay text label
delay_label = Label(
    window, text="Start Delay Time (sec) :", font=("Times", "15"))
delay_label.place(x=25, y=350)
# delay text label
start_delay_label = Label(
    window, text="Delay Between Messages (sec) :", font=("Times", "15"))
start_delay_label.place(x=25, y=400)

# text input box
text_box = Text(width=49, height=6,   borderwidth=2, font=("Times", "14"))
text_box.place(x=26, y=155)

# counter input box
counter_box = Entry(window, width=26, borderwidth=2, font=("Times", "14"))
counter_box.place(x=230, y=303)

# start_delay input box
start_delay_box = Entry(window, width=21, borderwidth=2, font=("Times", "14"))
start_delay_box.place(x=273, y=353)

# delay input box
delay_box = Entry(window, width=15, borderwidth=2, font=("Times", "14"))
delay_box.place(x=326, y=403)

# main  function


def run():
    text = text_box.get("1.0", END)
    print(text)
    count = int(counter_box.get())
    print(count)
    start_delay = int(start_delay_box.get())
    delay = int(delay_box.get())
    print(start_delay)
    Keyboard = Controller()
    time.sleep(int(delay_box.get()))
    for i in range(count):
        for letter in text:
            Keyboard.press(letter)
            Keyboard.release(letter)
        Keyboard.press(Key.enter)
        time.sleep(delay)


# button
btn = Button(window, text='RUN', bd=1, padx=20, pady=0,
             borderwidth=2, height=0, font=("Times", "20"), command=run)
btn.pack()
btn.place(x=350, y=450)

window.mainloop()
