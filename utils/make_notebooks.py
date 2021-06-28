import pandas as pd
import os


df = pd.read_csv('new_old_alignment.csv')

df['New'] = df.drop(columns=['Time','New', 'Old'])\
            .apply(lambda x : str(x.name)  + '_' + '_'.join(x.to_list()), axis = 1)\
            .str.replace('[^\w]','_').apply(lambda p : p +'.ipynb')

def notebook_writer(path, rel_path = 'notebooks2021'):
    if not os.path.isfile(p):
        with open(p, 'w') as f:
            f.write('\{\}')
        
df.New.apply(notebook_writer, rel_path = 'notebooks2021')



df.to_csv('new_old_alignment.csv')