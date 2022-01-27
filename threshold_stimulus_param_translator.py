# Code author: Joseph K. Nadeau

from numpy.lib.shape_base import column_stack
import pandas as pd
import numpy as np

# Read excel docs into program as Pandas dataframes

rot_data_sheet_1hz_narrow = pd.read_excel(r'Z:\Hullar_Vestibular Psychophysic\Source_Data\Threshold Data\Data Sheets\MethodConstant_Rotation_Data_sheet_Narrow1Hz_RLequal_19intervals_20-Jan-2022.xls', header=None)
rot_data_sheet_1hz_medium = pd.read_excel(r'Z:\Hullar_Vestibular Psychophysic\Source_Data\Threshold Data\Data Sheets\MethodConstant_Rotation_Data_sheet_Medium_1Hz_RLequal_19intervals_24-Jan-2022.xls', header=None)
rot_data_sheet_1hz_wide = pd.read_excel(r'Z:\Hullar_Vestibular Psychophysic\Source_Data\Threshold Data\Data Sheets\MethodConstant_Rotation_Data_sheet_Wide_1Hz_RLequal_19intervals_24-Jan-2022.xls', header=None)
    
print(rot_data_sheet_1hz_narrow.head())
print(rot_data_sheet_1hz_medium.head())
print(rot_data_sheet_1hz_wide.head())

def translate(df1):

    # Split strings in all rows of argument 1 at '_' and put each item at split in its own column
    df1 = df1.iloc[: , 0].str.split('_', expand=True)
    # Strip strings in all rows of all alphabetical characters
    df1 = df1.replace(to_replace=r'[A-Za-z]', value='', regex=True)
    # Convert remaining strings(digits as type 'string') to integers so that operations can be performed
    df1 = df1.astype(int)
    # Divide every item in column 1 of df1 by 10
    df1.iloc[:, 1] = df1.iloc[:, 1].div(10)
    # Divide every item in column 2 of df1 by 10
    # df1.iloc[:, 2] = df1.iloc[:, 2].div(10)
    # Rename columns
    df1 = df1.rename(columns={df1.columns[0]: '1Hz Test #', df1.columns[1]: 'Chair Delay', df1.columns[2]: 'Frequency', df1.columns[3]: 'Chair Amp'})
    # Add columns
    df1["Subject Answer"] = ""
    df1["Correct"] = ""

    return df1

newThresholdParams_narrow= translate(rot_data_sheet_1hz_narrow)
newThresholdParams_medium= translate(rot_data_sheet_1hz_medium)
newThresholdParams_wide= translate(rot_data_sheet_1hz_wide)

print(newThresholdParams_narrow.head())
print(newThresholdParams_medium.head())
print(newThresholdParams_wide.head())

newThresholdParams_narrow.to_csv("MethodConstant_Rotation_Score_sheet_narrow_19intervals_25-Jan-2022.csv", index=False)
newThresholdParams_medium.to_csv("MethodConstant_Rotation_Score_sheet_medium_19intervals_25-Jan-2022.csv", index=False)
newThresholdParams_wide.to_csv("MethodConstant_Rotation_Score_sheet_wide_19intervals_25-Jan-2022.csv", index=False)
