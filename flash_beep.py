from tkinter import *
import pandas as pd
import winsound, random, time


root = Tk()
root.title("Flash_Beep")

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 600  # Set Duration To 1000 ms == 1 second

instructions = Label(root, text = "This program will present a 'flash' and a 'beep' when the 'Start' button is clicked. Your task is to determine whether the 'flash' and 'beep' occured at the same time or independently of one another. When you are ready to begin please click the 'Start' button.", wraplength = 200)
instructions.pack()

canvas_1 = Canvas(root, width=500, height=500, )
canvas_1.pack()
canvas_1.create_rectangle(0, 0, 500, 500, fill='black', tag='rect')

def flash_beep(event):
    stimulus_delay = [.1, .2, .3, .4, .5, .6, .7, .8, .9, 1]
    sd_random = random.choice(stimulus_delay)
    temporal_delay = [0, .01, .02, .03, .04, .05, .06, .07 , .08, .09]
    td_random = random.choice(temporal_delay)
    func_list = [beep, flash]
    random_func = random.choice(func_list)

    if random_func == beep:
        time.sleep(sd_random)
        random_func()
        time.sleep(td_random)
        flash(1)
        answer()
    elif random_func == flash:
        time.sleep(sd_random)
        random_func(1)
        time.sleep(td_random)
        beep()
        answer()
    


def beep():
    frequency = 2000  # Set Frequency To 2500 Hertz
    duration = 400  # Set Duration To 1000 ms == .6 second
    winsound.Beep(frequency, duration)


def flash(n):
    color = ['white', 'black'][n%2]
    canvas_1.itemconfig('rect', fill=color)
    if n >= 0:
        root.after(50, flash, n-1)
    else:
        canvas_1.itemconfig('rect', fill='black')

def answer():
        label_question = Label(root, text = "Which occured first: the 'flash' or the 'beep'? Or did they occur at the same time?")
        label_question.pack()
        button_flash = Button(root, text = "The flash")
        button_flash.pack()
        button_beep = Button(root, text = "The beep")
        button_beep.pack()
        button_same_time = Button(root, text = "Same time")
        button_same_time.pack()

def log_and_destroy(bs):
    # log sd_random, td_random, random_func into pandas dataframe
    # log the name of the button that was clicked into the pandas dataframe
    # destroy answer buttons

    bs.destroy()



button_start = Button(root, text = "Start")
button_start.pack()
button_start.bind('<Button-1>', flash_beep)

button_quit = Button(root, text = "Exit Program", command = root.quit)
button_quit.pack()

root.mainloop()


