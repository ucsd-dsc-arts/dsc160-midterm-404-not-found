import pandas as pd
import numpy as np
import os

pp = pd.read_csv(os.path.join(os.pardir, 'data/picasso.csv'))
hm = pd.read_csv(os.path.join(os.pardir, 'data/henri_dic.csv'))

pp = pp.rename(columns={'Unnamed: 0': 'Picturesource', '0': 'Painting'})
pp = pp.assign(Year=pp['Painting'])
pp['Year'] = pp.apply(lambda row: row.Painting[-5:-1], axis = 1)
pp['Painting'] = pp.apply(lambda row: row.Painting.lower(), axis = 1)
maternity_keywords = ['maternity','olga','mother','motherhood','maya','graces','child']
mistress_keywords = ['ladies','woman','lover','bather','fernande','marie','dora','dream','muse','female','flower']


# 0 for maternity and 1 for mistress
def pp_mat_or_mis(row):
    for i in maternity_keywords:
        if i in row['Painting']:
            return 0
    for j in mistress_keywords:
        if j in row['Painting']:
            return 1
pp['Portrait'] = pp.apply(pp_mat_or_mis, axis=1)
pp_women = pp.loc[pp['Portrait'].notnull()]
pp_women.to_csv(os.path.join(os.pardir,'data/picasso_women.csv'), index = False, header=True)
print('Finish classifying Picasso women type...')




hm = hm.rename(columns={'Unnamed: 0': 'Picturesource', '0': 'Painting'})
hm = hm.assign(Year=hm['Painting'])
hm['Year'] = hm.apply(lambda row: row.Painting[-5:-1], axis = 1)
hm['Painting'] = hm.apply(lambda row: row.Painting.lower(), axis = 1)
mat_keywords = ['blue nude','madame','matisse','marguerite','conversation']
mis_keywords = ['odalisque','girl','nude','lorette','carmelina','dark hair','woman','sisters','laurette','figure','interior','helen','model']


def hm_mat_or_mis(row):
    for i in mat_keywords:
        if i in row['Painting']:
            return 0
    for j in mis_keywords:
        if j in row['Painting']:
            return 1
hm['Portrait'] = hm.apply(hm_mat_or_mis, axis=1)
hm_women = hm.loc[hm['Portrait'].notnull()]
hm_women.to_csv (os.path.join(os.pardir,'data/matisse_women.csv'), index = False, header=True)
print('Finish classifying Henri women type...')