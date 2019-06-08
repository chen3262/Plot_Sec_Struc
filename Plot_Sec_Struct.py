########################## change the following parameters ##########################################
file = '/hdd/si_han/Project/Abeta/AbetaTraj/timeline.tml' # path of the output from VMD Timeline
DIR = '/home/si_han/Desktop/' # path of the folder to store the pidctures
num_res = 42 # Number of residues of your protein
dim_fig1 = [30, 4] # wiidth and height of the horizontal heatmap
dim_fig2 = [10, 25] # wiidth and height of the vertical heatmap
#####################################################################################################


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as colors

df = pd.read_csv(file, delimiter=r"\s+", header=None)
df = df[df[0]!='#']
df[0] = pd.to_numeric(df[0])
df = df.reset_index(drop=True)
sec_label = list(set(df[4]))
num_frame = int(len(df)/num_res)

sec_name = sec_label.copy()
for i in range(len(sec_name)):
    if sec_name[i] == 'E':
        sec_name[i] = 'Extended Configuration'
    elif sec_name[i] == 'T':
        sec_name[i] = 'Turn'
    elif sec_name[i] == 'B':
        sec_name[i] = 'Isolated Bridge'
    elif sec_name[i] == 'H':
        sec_name[i] = 'Aplha Helix'
    elif sec_name[i] == 'G':
        sec_name[i] = '3-10 Helix'
    elif sec_name[i] =='I':
        sec_name[i] = 'Pi-helix'
    elif sec_name[i] == 'C':
        sec_name[i] = 'Coil'

cal_res = []
for i in range(1,num_res+1):
    tmp = [i]
    sel = df[df[0]==i]
    for _, lb in enumerate(sec_label):
        tmp.append(len(sel[sel[4]==lb]))
    cal_res.append(tmp)

count = pd.DataFrame(cal_res, columns=['resid']+sec_label)
count.index = np.arange(1, len(count) + 1)
frame_num = count[sec_label].sum(axis=1).loc[1]
percentage = count[sec_label]/frame_num*100
percentage.columns = sec_name

plt.figure(figsize=dim_fig1)
ax = sns.heatmap(percentage.T, cmap='binary'
                 ,annot=False
                 ,cbar_kws={'label': 'percentage (%)'}
                ,norm=colors.PowerNorm(gamma=1./4.))
ax.figure.axes[-1].yaxis.label.set_size(16)
ax.tick_params(labelsize=16)
cax = plt.gcf().axes[-1]
cax.tick_params(labelsize=20)
for _, spine in ax.spines.items():
    spine.set_visible(True)
plt.savefig(DIR+'sec_struct_horizontal.pdf')

plt.figure(figsize=dim_fig2)
ax = sns.heatmap(percentage, cmap='binary',annot=True, cbar=False,norm=colors.PowerNorm(gamma=1./4.))
ax.figure.axes[-1].yaxis.label.set_size(16)
ax.tick_params(labelsize=16)
ax.xaxis.tick_top()
ax.set_yticklabels(ax.get_yticklabels(), rotation = 0)
ax.set_xticklabels(ax.get_xticklabels(), rotation = 70)
for _, spine in ax.spines.items():
    spine.set_visible(True)
plt.savefig(DIR+'sec_struct_vertical.pdf')
