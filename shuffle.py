import pandas as pd
import re

# Read in the excel file
pre_shuffle = pd.read_excel("Shuffle.xlsx")

# Check how many of each class group there are. A, B, C, D, ...
def get_years_count(df):
    # List to store the matches
    matches = []
    year_groups = []
    
    # Extract column B where the year groups are
    column_b = pd.read_excel("Shuffle.xlsx", usecols='B')
    
    # Define the regex pattern
    pattern = r"\b\w+(?: \w+)? [A-Z]\b"
    
    # Iterate over each value in the column
    for value in column_b.values:
        # Apply the regex pattern to the value
        match = re.search(pattern, str(value))
        if match:
            matches.append(match.group())
    for year in matches:
        year_group = year.split()
        year_groups.append(year_group[0])
    count_dict = {}

    for item in year_groups:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    return count_dict

def sort(df):
    

print(pre_shuffle)
