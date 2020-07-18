import pandas as pd
import os 

from os import listdir


def rename_xls (filepaths):
    for f in filepaths:
        if f.endswith('.xls'):
            os.rename(os.path.join(os.getcwd(),'Contacts',f),f.split('.')[0] + '.csv')



def load_pandascsv (filepaths):
    li = []
    for filepath in filepaths:
        url = 'https://raw.githubusercontent.com/Urobhi/BairesDev/master/DstCH/Contacts/'+ filepath
        if filepath.endswith(".csv"):
            
            aux=pd.read_csv(url,index_col = None)
            
            aux['Response'] = filepath[0]
            li.append(aux)
        else:
            aux=pd.read_excel(url, index_col = None)
            aux['Response'] = filepath[0]
            li.append(aux)
    df = pd.concat(li,axis=0,ignore_index=True)
    return(df)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

filepaths = listdir(os.path.join(os.getcwd(),"Contacts"))

rename_xls(filepaths)

filepaths =listdir(os.path.join(os.getcwd(),"./Contacts"))

Data = load_pandascsv(filepaths)
