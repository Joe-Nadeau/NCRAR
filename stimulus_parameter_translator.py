# Code author: Joseph K. Nadeau

from numpy.lib.shape_base import column_stack
import pandas as pd
import numpy as np

# Read excel docs into program as Pandas dataframes

# rot_data_sheet_02hz = pd.read_excel('TBW_Rotation_Data_sheet_02Hz_20170131.xls', header=None)
# rot_data_sheet_05hz = pd.read_excel('TBW_Rotation_Data_sheet_05Hz_20170131.xls', header=None)
rot_data_sheet_1hz = pd.read_excel('TBW_Rotation_Data_sheet_1Hz_RL10_23-Dec-2021.xls', header=None)
# rot_data_sheet_10hz = pd.read_excel('TBW_Rotation_Data_sheet_10Hz_20170131.xls', header=None)
# rot_data_sheet_20hz = pd.read_excel('TBW_Rotation_Data_sheet_20Hz_20170131.xls', header=None)
# rot_data_sheet_50hz = pd.read_excel('TBW_Rotation_Data_sheet_50Hz_20170131.xls', header=None)


# vis_vest_02hz = pd.read_excel('TBW_VisVest_0.2Hz.xlsx')
# vis_vest_05hz = pd.read_excel('TBW_VisVest_0.5Hz_BLANK.xlsx')
vis_vest_1hz = pd.read_excel(r'Z:\Hullar_Vestibular Psychophysic\Source_Data\Temporal Binding Window Data\TBW_VisVest_Blanks\TBW_VisVest_1Hz.xlsx')
# vis_vest_10hz = pd.read_excel('TBW_VisVest_1Hz.xlsx')
# vis_vest_20hz = pd.read_excel('TBW_VisVest_2Hz.xlsx')
# vis_vest_50hz = pd.read_excel('TBW_VisVest_5Hz.xlsx')

# Format rot_data_sheet dataframes and merge them with vis_vest dataframes

def translate(df1, df2, hz):

    # Split strings in all rows of argument 1 at '_' and put each item at split in its own column
    df1 = df1.iloc[: , 0].str.split('_', expand=True)
    # Strip strings in all rows of all alphabetical characters
    df1 = df1.replace(to_replace=r'[A-Za-z]', value='', regex=True)
    # Convert remaining strings(digits as type 'string') to integers so that operations can be performed
    df1 = df1.astype(int)
    # Divide every item in column 1 of df1 by 10
    df1.iloc[:, 1] = df1.iloc[:, 1].div(10)
    # Divide every item in column 3 of df1 by 10
    df1.iloc[:, 3] = df1.iloc[:, 3].div(10)
    # Subtract 200 from every item in column 2
    # df1.iloc[:, 2] = df1.iloc[:, 2].sub(200)
    # Rename columns in df1 based on the following dictionary
    df1 = df1.rename(columns = {0: hz, 1: 'Chair Delay (s)', 2: 'Flash Delay (ms)', 3: 'Frequency', 4: 'Chair Amp'})
    # Merge df1 and df2
    trans_df = pd.merge(df1, df2, how='outer')
    # If flash delay is negative, then first stim is flash
    trans_df["First Stim"] = ["Flash" if ele < 0 else "chair" for ele in trans_df["Flash Delay (ms)"]]
    # Return new dataframe
    return trans_df

# Apply 'translate' function to all dataframes

# test_02hz = translate(rot_data_sheet_02hz, vis_vest_02hz, '0.2 Hz Test #')
# test_05hz = translate(rot_data_sheet_05hz, vis_vest_05hz, '0.5 Hz Test #')
# test_1hz = translate(rot_data_sheet_10hz, vis_vest_10hz, '1 Hz Test #')
# test_2hz = translate(rot_data_sheet_20hz, vis_vest_20hz, '2 Hz Test #')
# test_5hz = translate(rot_data_sheet_50hz, vis_vest_50hz, '5 Hz Test #')
new_1hz = translate(rot_data_sheet_1hz, vis_vest_1hz, '1 Hz Test #')

# Export files to excel documents (these need to be renamed)

# test_02hz.to_excel("TBW_VisVest_0.2Hz_v1.xlsx")
# test_05hz.to_excel("TBW_VisVest_0.5Hz_v1.xlsx")
# test_1hz.to_excel("TBW_VisVest_1Hz_v1.xlsx")
# test_2hz.to_excel("TBW_VisVest_2Hz_v1.xlsx")
# test_5hz.to_excel("TBW_VisVest_5Hz_v1.xlsx")
new_1hz.to_csv("TBW_VisVest_1Hz_v3.csv")
