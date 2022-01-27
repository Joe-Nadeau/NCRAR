from cgitb import text
from distutils import command
from itertools import count
from os import error
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pandas as pd
from datetime import date
import sys
import os.path
import re

root = Tk()
root.title("Vestibular Threshold Scoring Application")

small_font = ("Kalinga", 12)
medium_font = ("Kalinga", 16)
large_font = ("Kalinga", 20)
giant_font = ("Kalinga", 40)
today = date.today()
today = today.strftime("%d-%b-%Y")
    
# Define globals
global container
global previous_counter
global subject_id

# Variables
counter = IntVar(root, 1)
previous_counter = IntVar(root, 0)

container = Frame(root, width=1000, height=800, bg='lightgreen')
container.pack(side="top", fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

def create_buttons():
    subject_id = subject_id_entry.get()
    subject_id_label.destroy()
    subject_id_entry.destroy()
    start_button.destroy()
    
    label_SID = Label(container, text=f"Subject id: {subject_id}", font=large_font, fg="firebrick2", bg="palegreen2")
    previous_trial_label = Label(container, text="Last completed trial:", font=large_font, bg="palegreen2")
    current_trial_count_label = Label(container, text="Current trial:", font=large_font, bg="palegreen2")
    previous_trial_count = Label(container, textvariable=previous_counter, font=large_font, bg="palegreen2")
    current_trial_count = Label(container, textvariable=counter, font=large_font, bg="palegreen2")
    button_left = Button(container, text="Left", command=leftClick, height=10, width=20, font=large_font, bg="papaya whip")
    button_right = Button(container, text="Right", command=rightClick, height=10, width=20, font=large_font, bg="LavenderBlush2")
    button_undo = Button(container, text="Undo Last Answer", command=undoLast, height=2, width=40, font=large_font, bg="red")
    button_export_data = Button(container, text="Export Subject Data", command= lambda: exportData(subject_id), height=2, width=40, font=large_font, bg="forest green", activebackground="blue")

    label_SID.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
    previous_trial_label.grid(row=1, column=0, padx=5, pady=2)
    current_trial_count_label.grid(row=1, column=2, padx=5, pady=2)
    previous_trial_count.grid(row=1, column=1, padx=5, pady=1)
    current_trial_count.grid(row=1, column=3, padx=5, pady=1)
    button_left.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    button_right.grid(row=2, column=2, columnspan=2, padx=10, pady=10)
    button_undo.grid(row=3, column=0, columnspan=4, padx=10, pady=10)
    button_export_data.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

    
def leftClick(event=None):
    
    # Subject answer of 0 = Left
    # Subject answer of 1 = Right
    # Chair Amplitude > 0 = Right turn
    # Chair Amplitude < 0 = Left turn
    
    trial_number = counter.get() - 1
    subject_answer = 0 
    df.at[trial_number, 'Subject Answer'] = subject_answer
    print('Subject Answer: Left', df.at[trial_number, 'Subject Answer'])
    
    print('counter/trial #:', trial_number,'\nChair Amp:', df.at[trial_number, 'Chair Amp'])
    if df.at[trial_number, 'Chair Amp'] < 0 and df.at[trial_number, 'Subject Answer'] == 0.0:
        df.at[trial_number, 'Correct'] = 'Y'
    
    elif df.at[trial_number, 'Chair Amp'] > 0 and df.at[trial_number, 'Subject Answer'] == 0.0:
        df.at[trial_number, 'Correct'] = 'N'
        
    elif df.at[trial_number, 'Chair Amp'] == 0 and df.at[trial_number, 'Subject Answer'] == 0.0:
        df.at[trial_number, 'Correct'] = None
        
    else:
        print('Error at leftClick function execution')
    
    previous_counter.set(previous_counter.get() + 1)
    counter.set(counter.get() + 1)
    print('counter:', counter.get())
    print('previous counter:', previous_counter.get())
    print(df)
    
    # iterate through 'Subject Answer' and 'Correct' columns in dataframe and add data based on button click. You'll probably need to use a for loop here.
    
def rightClick(event=None):
    
    # Subject answer of 0 = Left
    # Subject answer of 1 = Right
    # Chair Amplitude > 0 = Right turn
    # Chair Amplitude < 0 = Left turn
    
    trial_number = counter.get() - 1
    subject_answer = 1
    df.at[trial_number, 'Subject Answer'] = subject_answer
    print('Subject answer: Right', df.at[trial_number, 'Subject Answer'])
    
    print('counter/trial #:', trial_number,'\nChair Amp:', df.at[trial_number, 'Chair Amp'])
    if df.at[trial_number, 'Chair Amp'] > 0 and df.at[trial_number, 'Subject Answer'] == 1.0:
        df.at[trial_number, 'Correct'] = 'Y'

    elif df.at[trial_number, 'Chair Amp'] < 0 and df.at[trial_number, 'Subject Answer'] == 1.0:
        df.at[trial_number, 'Correct'] = 'N'
        
    elif df.at[trial_number, 'Chair Amp'] == 0 and df.at[trial_number, 'Subject Answer'] == 1.0:
        df.at[trial_number, 'Correct'] = None
        
    else:
        print('Error at rightClick function execution')
    
    previous_counter.set(previous_counter.get() + 1)
    counter.set(counter.get() + 1)
    print('counter:', counter.get())
    print('previous counter:', previous_counter.get())
    print(df)
    
def undoLast(event=None):
    counter.set(counter.get() - 1)
    previous_counter.set(previous_counter.get() - 1)
    
def exportData(subject_id):
    
    # create new filename
    fileToBeSaved = '%s_VT_%s.csv' % (subject_id, today)
    
    # find all files at x-locaton that match z-pattern and save to a-list.
    regex_1 = re.compile('\D+\d+_VT_\d\d-\D\D\D-\d\d\d\d|(\(\d\))|.csv')
    ncrar_share_path = 'Z:\Hullar_Vestibular Psychophysic\Source_Data\Threshold Data'
    # ohsu_laptop_path = 'C:\TimHullar_Lab\Source Data\Threshold Data'
    file_list = []
    repeat_count = 0
    
    for filename in os.listdir(ncrar_share_path):
        if regex_1.match(filename):
            file_list.append(filename)
    
    # check a-list to see if new filename matches any files in list.
    # if new filename matches a file in a-list update name of new file.
    while fileToBeSaved in file_list:
        print(f'{fileToBeSaved} already exists. I will try a new filename.')
        repeat_count += 1
        fileToBeSaved = '%s_VT_%s(%s).csv' % (subject_id, today, repeat_count)
    try:
        df.to_csv(f'Z:\Hullar_Vestibular Psychophysic\Source_Data\Threshold Data\{fileToBeSaved}', index=None)
        pop_up = Toplevel()
        export_complete_message = Label(pop_up, text="Data Export has been completed.\nYou may now close the program.", bg="#34a82c", font=large_font)
        export_complete_message.pack()
    except:
        error_message_window = Toplevel()
        export_error_message = Label(error_message_window, text="There was an error exporting subject data. Please contact Joey for troubleshooting.", bg="DarkOrange1", font=large_font)
        export_error_message.pack()

        
# score_sheet = r'C:\TimHullar_Lab\Testing_Sheets\MethodConstant_Rotation_Score_sheet.csv'
# score_sheet = r'C:\TimHullar_Lab\Testing_Sheets\MethodConstant_Rotation_Score_sheet_19intervals_13-Jan-2022.csv'
# score_sheet = r'Z:\Hullar_Vestibular Psychophysic\Source_Data\Threshold Data\MethodConstant_Rotation_Score_sheet_19intervals_13-Jan-2022.csv'
score_sheet = "pass"
subject_id_label = Label(container, text="Subject ID:", bg='palegreen2')
subject_id_entry = Entry(container)
start_button = Button(container, text="Start", command=create_buttons)

subject_id_label.grid(row=0, column=1, padx=10, pady=5)
subject_id_entry.grid(row=0, column=2, padx=10, pady=10)
start_button.grid(row=1, column=0, columnspan=3)

# Create dataframe
df = pd.read_csv(score_sheet, index_col=None)
df['Correct'] = df['Correct'].astype(str)
print(df)


root.mainloop()