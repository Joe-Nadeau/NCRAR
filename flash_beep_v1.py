# Code author: Joseph K. Nadeau

from tkinter import *
import pygame
import pandas as pd
import numpy as np
import winsound, random, time, os
from collections import Counter

def flash_beep(event):
    global stimulus_delay, sd_random, td_random, temporal_delay, func_list, random_func, stim_1, reps, entry_subject_id, button_export
 
    while len(temporal_delay) > 0:     
        stimulus_delay = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        sd_random = random.choice(stimulus_delay)
        td_random = random.choice(temporal_delay)
        func_list = [beep, flash_white]
        random_func = random.choice(func_list)
        
        if random_func == flash_white:
                stim_1 = 'Beep'
        elif random_func == beep:
                stim_1 = 'Flash'
        else:
            stim_1 = 'NOT flash_white OR beep'
            
        if random_func == beep:
            timeA = time.perf_counter()
            root.after(sd_random, beep)
            timeB = time.perf_counter()
            root.after(td_random, flash_white)
            timeC = time.perf_counter()
            print("beep =", timeB - timeA)
            print("flash =", timeC - timeB)
            temporal_delay.remove(td_random)
            answer()
            
        elif random_func == flash_white:
            timeD = time.perf_counter()
            root.after(sd_random, flash_white)
            timeE = time.perf_counter()
            root.after(td_random, beep)
            timeF = time.perf_counter()
            print("flash", timeE - timeD)
            print("beep", timeF - timeE)
            temporal_delay.remove(td_random)
            answer()
            
        return sd_random, td_random, stim_1
    button_start.destroy()
    button_quit.destroy()
    entry1.destroy()
    instructions.destroy()
    canvas_1.destroy()
    test_complete_message = Label(root, text = "\n\nYou have completed the test! Thank you for participating.\n\n", wraplength = 600, font = ("Times", 40), bg = "white", fg = "green")
    test_complete_message.pack()
    stop_label = Label(root, text = "STOP", font = 35, bg = "red", fg = "white", pady = 20)
    stop_label.pack(fill = "x")
    sub_id_label = Label(root, text = "This section to be completed by test administrator: \n\n\nEnter Subject ID", font = ("Times", 16, ), fg = "red", bg = "white", pady = 30)
    sub_id_label.pack()
    entry_subject_id = Entry(root)
    entry_subject_id.pack()
    button_export = Button(root, text = "Export Subject Data")
    button_export.pack()
    button_export.bind("<Button-1>", export_dataframe)
     
def beep():
    pygame.mixer.music.load("beep-3.wav")
    pygame.mixer.music.play(loops=0)
    # frequency = 1000
    # duration = 200
    # winsound.Beep(frequency, duration)

def flash_black():
    canvas_1.itemconfigure(canvas_1.find_withtag('rect'), fill="black")
    flash_end_time = time.time()

def flash_white():
    flash_start_time = time.time()
    canvas_1.itemconfigure(canvas_1.find_withtag('rect'), fill="white")
    root.after(50, flash_black)

def answer():
        l = label_question = Label(root, text = "Which occured first: the 'flash' or the 'beep'? If you can't tell, just give it your best guess.", bg = "white")
        label_question.pack(fill = "x")
        
        bf = button_flash = Button(root, text = "Flash")
        bf.config(command = lambda: log_and_destroy(l, bf, bb, "Flash"))
        button_flash.pack(pady=10)
        
        bb = button_beep = Button(root, text = "Beep")
        bb.config(command = lambda: log_and_destroy(l, bf, bb, "Beep"))
        button_beep.pack()
        
        entry1.pack()
        
def log_and_destroy(x, y, z, text):
    # log the name of the button that was clicked into the pandas dataframe
    # destroy answer buttons
    global data, correct_ans
    subject_answer = entry1.get()
    entry1.insert(0, text)
    subject_answer = entry1.get()
    entry1.delete(0, END)
    
    if subject_answer == stim_1:
        correct_ans = 'Y'
    else:
        correct_ans = 'N'
        
    data = ['0', sd_random, td_random, stim_1, subject_answer, correct_ans]
    df_length = len(df)
    df.loc[df_length] = data
    df['Test #'] = np.arange(len(df))
    print(df)
    
    x.destroy()
    y.destroy()
    z.destroy()

def export_dataframe(event):
    sub_id = entry_subject_id.get()
    df.to_excel(r"Z:\Hullar_Vestibular Psychophysic\Source_Data\Temporal Binding Window Data\%s.xlsx" % sub_id)
    export_complete_label = Label(root, text = "Data export complete. \n You may now exit the program.", font = 30, bg = "green2")
    export_complete_label.pack(pady = 20)






global root, entry1, canvas_1, df, data

root = Tk()
root.title("Flash_Beep")
root.configure(bg="gray60")

pygame.mixer.init()

entry1 = Entry(root)

frequency = 2500  # Set Frequency To 2500 Hertz
duration =  100 # Set Duration, 1000 ms == 1 second
temporal_delay = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                  5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 
                 30, 30, 30, 30, 30, 30, 30, 30, 30, 30] 
                #  40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 
                #  50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 
                #  60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 
                #  70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 
                #  80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 
                #  90, 90, 90, 90, 90, 90, 90, 90, 90, 90]

instructions = Label(root, text = "This program will present a 'flash' and a 'beep' when the 'Start' button is clicked. Your task is to determine whether the 'flash' OR 'beep' occured first. When you are ready to begin please click the 'Start' button."
                    , wraplength = 700, font = ("Times", 16), bg = "bisque2", padx=30, pady=30)
instructions.pack(fill = "x", pady = 30)

# create an empty dataframe for storing subject responses and the stimulus data
data = []
df = pd.DataFrame(columns= ['Test #', 'Stimulus Delay', 'Temporal Delay', 'First Stimulus', 'Subject Answer', 'Correct'])

# Create new canvas
canvas_1 = Canvas(root, width=350, height=350, )
canvas_1.pack()
canvas_1.create_rectangle(0, 0, 350, 350, fill='black', tag='rect')

# Create start button and bind it to the flash_beep function so that the function is executed upon button click
button_start = Button(root, text = "Start", bg="SpringGreen3", font=40,)
button_start.pack(pady=20)
button_start.bind("<Button-1>", flash_beep)

button_quit = Button(root, text = "Exit Program", command = root.destroy, bg="coral2")
button_quit.pack()

root.mainloop()

