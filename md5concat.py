import pandas as pd
import os
import os, glob
md5=pd.DataFrame()
for filename in glob.glob('*.txt'):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        content = pd.read_csv(f,sep='\t')
        ls= list(content)
        md5=md5.append(ls,ignore_index=True)
md5=md5[0].str.split(expand=True)  
md5.to_csv('md5file.csv')