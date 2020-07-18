import pandas as pd
import os 
import sys
from os import listdir


def rename_xls (filepaths):
    for f in filepaths:
        if f.endswith('.xls'):
            os.rename(os.path.join(os.getcwd(),'Contacts',filepath),f.split('.')[0] + '.csv')


filepaths = listdir("./Contacts")


Data = pd.DataFrame()
 for filepath in filepaths:
     pdaux = pd.read_excel(os.path.join("./Contacts",filepath)
     Data.append()
def main():
    data = []
    
    filepath = [f for f in  if f.startswith('N')]
    for filename in files
    with open (os.path.join(os.path.dirname(sys.argv[0]),))

for f