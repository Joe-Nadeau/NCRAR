from os import error
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pandas as pd
import datetime
import sys

root = Tk()
root.title("Flash/Rotation TBW Scoring Application")

small_font = ("Kalinga", 12)
medium_font = ("Kalinga", 16)
large_font = ("Kalinga", 20)
    
# Define globals
global container
global subject_id

# Variables
counter = IntVar(root, 1)

container = Frame(root, width=1000, height=800, bg='lightgreen')
container.pack(side="top", fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

def create_buttons():
    subject_id = subject_id_entry.get()
    subject_id_label.destroy()
    subject_id_entry.destroy()
    start_button.destroy()
    
    trial_count_label = Label(container, text="Trial #:", font=large_font, bg="palegreen2")
    trial_count = Label(container, textvariable=counter, font=large_font, bg="palegreen2")
    button_flash = Button(container, text="Flash First", command=flashClick, height=10, width=20, font=large_font, bg="papaya whip")
    button_turn = Button(container, text="Turn First", command=turnClick, height=10, width=20, font=large_font, bg="LavenderBlush2")
    button_undo = Button(container, text="Undo Last Answer", command=undoLast, height=2, width=40, font=large_font, bg="red")
    button_export_data = Button(container, text="Export Subject Data", command=lambda : df.to_csv('Z:\Hullar_Vestibular Psychophysic\Source_Data\Temporal Binding Window Data\Subject Data\%s.csv' % subject_id), height=2, width=40, font=large_font, bg="forest green")
    
    trial_count_label.grid(row=0, column=0, columnspan=2, padx=5, pady=(5, 0))
    trial_count.grid(row=0, column=1, padx=5, pady=1)
    button_flash.grid(row=1, column=0, padx=10, pady=10)
    button_turn.grid(row=1, column=1, padx=10, pady=10)
    button_undo.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    button_export_data.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
def flashClick(event=None):
    
    trial_number = counter.get() - 1
    subject_answer = 0 
    df.at[trial_number, 'Subject Answer'] = subject_answer
    print('Subject Answer: Flash', df.at[trial_number, 'Subject Answer'])
    
    print('counter/trial #:', trial_number,'\nFirst Stim:', df.at[trial_number, 'First Stim'])
    if df.at[trial_number, 'First Stim'] == 'Flash' and df.at[trial_number, 'Subject Answer'] == 0.0:
        df.at[trial_number, 'Correct'] = 'Y'
    
    elif df.at[trial_number, 'First Stim'] != 'Flash' and df.at[trial_number, 'Subject Answer'] == 0.0:
        df.at[trial_number, 'Correct'] = 'N'
        
    else:
        print('Error at flashClick function execution')
    
    counter.set(counter.get() + 1)
    print('counter:', counter.get())
    print(df)
    
    # iterate through 'Subject Answer' and 'Correct' columns in dataframe and add data based on button click. You'll probably need to use a for loop here.
    
def turnClick(event=None):
    
    trial_number = counter.get() - 1
    subject_answer = 1
    df.at[trial_number, 'Subject Answer'] = subject_answer
    print('Subject answer: Turn', df.at[trial_number, 'Subject Answer'])
    
    print('counter/trial #:', trial_number,'\nFirst Stim:', df.at[trial_number, 'First Stim'])
    if df.at[trial_number, 'First Stim'] == 'chair' and df.at[trial_number, 'Subject Answer'] == 1.0:
        df.at[trial_number, 'Correct'] = 'Y'

    elif df.at[trial_number, 'First Stim'] != 'chair' and df.at[trial_number, 'Subject Answer'] == 1.0:
        df.at[trial_number, 'Correct'] = 'N'
        
    else:
        print('Error at turnClick function execution')
    
    counter.set(counter.get() + 1)
    print('counter', counter.get())
    print(df)
    
def undoLast(event=None):
    counter.set(counter.get() - 1)
    
    # get last entry in 'Subject Answer' and 'Correct' columns and delete them from the dataframe.
    
# def exportData(subject_id):
#     final_score_sheet = df.to_csv('Z:\Hullar_Vestibular Psychophysic\Source_Data\Temporal Binding Window Data\Subject Data\%s.csv' % subject_id)
    
    
score_sheet = r'Z:\Hullar_Vestibular Psychophysic\Source_Data\Temporal Binding Window Data\TBW_VisVest_1Hz_v3.csv'
subject_id_label = Label(container, text="Subject ID:", bg='palegreen2')
subject_id_entry = Entry(container)
start_button = Button(container, text="Start", command=create_buttons)

subject_id_label.grid(row=0, column=1, padx=10, pady=5)
subject_id_entry.grid(row=0, column=2, padx=10, pady=10)
start_button.grid(row=1, column=0, columnspan=3)

# Create dataframe
df = pd.read_csv(score_sheet)
df['Correct'] = df['Correct'].astype(str)


root.mainloop()