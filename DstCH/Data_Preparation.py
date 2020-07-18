import pandas as pd
import os 

from os import listdir


def rename_xls (filepaths,basepath):
    for f in filepaths:
        if f.endswith('.xls'):
            os.rename(os.path.join(os.getcwd(),'Contacts',f),os.path.f.split('.')[0] + '.csv')



def load_pandascsv (filepaths,basepath):
    li = []
    for filepath in filepaths:
        url = 'https://raw.githubusercontent.com/Urobhi/BairesDev/master/DstCH/' + basepath + filepath
        print(url)
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
rename_xls(filepaths,"./Contacts/")
filepaths =listdir(os.path.join(os.getcwd(),"./Contacts"))
Train_Data = load_pandascsv(filepaths,"Contacts/")




filepaths = listdir(os.path.join(os.getcwd(),"Data"))
rename_xls(filepaths,"./Data/")
filepaths =listdir(os.path.join(os.getcwd(),"./Data"))
Test_Data = load_pandascsv(filepaths,"Data/")

