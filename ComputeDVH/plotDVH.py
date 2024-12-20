#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import matplotlib.colors as colors
import itertools
import argparse
parser = argparse.ArgumentParser(description='Presents label of the TXT files')
parser.add_argument("-label1", help="label of TXTs files 1", type=str, default="")
parser.add_argument("-dir1", help="folder of TXTs files 2", type=str, default="")
parser.add_argument("-Dgoal", help="reference planned dose [cGy]",type=float,default=100)
parser.add_argument("-roi", help="list of ROIs name", type=str, nargs='+')
ROIs = []
args= parser.parse_args()
global fileLabel_1
global fileDir_1

fileLabel_1 = args.label1
fileDir_1 = args.dir1

my_Color = ['r','g','b','k','y','c','m','tab:orange','tab:purple','tab:pink','tab:brown','yellowgreen','slategray','hotpink', 'tan','lightcoral', 'tomato']

plt.rcParams.update({'font.size': 11})
fig = plt.figure(figsize=(6,6))
ax1=plt.subplot(111)


plt.xlabel('Dose [cGy]',fontsize='11')
plt.ylabel('Volume [%]',fontsize='11')
c = 0
for ROIname in args.roi:
    x1,y1=np.loadtxt(fileDir_1 + '/' +ROIname+ fileLabel_1 + '.txt', comments=['#','idx'], usecols=(0,1), unpack=True)
    plt.plot(x1, y1,color=my_Color[c],label=ROIname, linewidth=1.8)
    c+=1

box=ax1.get_position()
ax1.set_position([box.x0, box.y0 + box.height * 0.1,
    box.width, box.height * 0.9])


box2=ax1.get_position()
ax1.set_position([box2.x0, box2.y0 + box2.height * 0.1,
    box2.width, box2.height * 0.9])

plt.plot([args.Dgoal*0.95],[95],'r*',lw=5,markerfacecolor='r', markeredgewidth=1, markeredgecolor='yellow',markersize=17)
star = Line2D([], [],marker='*',linewidth='0',markerfacecolor='r',markeredgewidth=1,markeredgecolor='yellow' ,markersize=17, label='V95% 95%')

legend1=plt.legend(loc = 'upper center',bbox_to_anchor=(0.5,-0.2),fancybox=True,shadow=True,ncol=3)
#legend3=plt.legend(handles=[star],loc=1)

line1 = Line2D([0],[0], label = fileLabel_1, color = 'k', linestyle = 'solid')

legend2 = plt.legend(handles=[star], bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left",mode="expand", borderaxespad=0, ncol=1)

#legend4 = plt.legend(handles=[star], bbox_to_anchor=(0.5,0.5), loc="lower left",mode="expand", borderaxespad=0, ncol=4)
plt.gca().add_artist(legend1)
plt.gca().add_artist(legend2)
#plt.gca().add_artist(legend4)
#plt.gca().add_artist(legend3)
plt.grid()
plt.show()




