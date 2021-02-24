# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:38:14 2020
this code is applied to plot ROC and AUC value
@author: cgdwo
"""

import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import xlrd


# set the family font 
font1={'family':'Arial',
     'style':'normal',
    'weight':'normal',
     'size':15}
font_xylable={'family':'Arial',
     'style':'normal',
    'weight':'normal',
     'size':20}
font_legend={'family':'Arial',
     'style':'normal',
    'weight':'normal',
     'size':12}
date = xlrd.open_workbook('./ROC_result.xlsx')
table=date.sheets()[0]
#  displacement data
rFP_3D = table.col_values(0)[1:]
rTP_3D = table.col_values(1)[1:]
rFP_inf = table.col_values(2)[1:]
rTP_inf = table.col_values(3)[1:]

#---------plot corner line-------
x_diagonal = np.linspace(0, 5, num = 2)
y_diagonal = x_diagonal
# fit parameters

#---------plot corner line-------


#-------------fit plot---------

plt.figure(num=1,figsize=(6, 5))
#plt.scatter(FS_3d, FS_inf, marker=".", edgecolor="black",linewidths=1,
#             color="k", cmap = 'best')

# line plot 

#plt.plot(density, FSR_area, 'o', ms = 3,  color="C0", linewidth = 1.5, linestyle='-')
plt.plot(rFP_3D, rTP_3D, color="C0", linewidth = 2, linestyle='-', label = r"$ CRESTABLE3D $")
plt.plot(rFP_inf, rTP_inf, color="C1", linewidth = 2, linestyle='-', label = "$ CRESLIDE $")
plt.plot(x_diagonal, y_diagonal, color="black", linewidth = 1.5, linestyle='--')
#plt.plot(x_fit_2, y_fit_2, color="red", linewidth = 1.5, linestyle='-')
# plt.fill_between(rFP_3D, rTP_3D,  color='C0',   alpha=0.1)
# plt.fill_between(rFP_inf, rTP_inf, color='C1',   alpha=0.2)
plt.xlim((0, 1)) 
plt.ylim((0, 1))
x_ticks=np.linspace(0, 1 ,6)
y_ticks=np.linspace(0, 1, 6)
plt.xticks(x_ticks, fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, fontproperties = 'Arial', size = 20)
# ax.tick_params(direction='out', length=6, width=2, colors='r',
#                grid_color='r', grid_alpha=0.5)
plt.xlabel("False positive rate", font_xylable)
plt.ylabel("True positive rate",font_xylable)


plt.text(0.45, 0.15, "$ AUC_{CRESTABLE3D} = 0.77 $", fontdict = font1)
plt.text(0.45, 0.05, "$ AUC_{CRESLIDE} = 0.72 $", fontdict = font1)
plt.text(0.2, 0.15, "$AUC_{ROC}=0.5$ (random prediction)", size=15, rotation=40)


plt.scatter([0.2],[0.67],s = 50, color='C0')
plt.scatter([0.32],[0.65],s = 50, color='C1')
plt.annotate('(0.20,0.67)', xy=(0, 0.72), textcoords = 'offset points',fontsize = 15)
plt.annotate('(0.32,0.65)', xy=(0.35, 0.63), textcoords = 'offset points',fontsize = 15)
         # ha="center", va="center",
         # bbox=dict(boxstyle="round",
         #           ec=(1., 0.5, 0.5),
         #           fc=(1., 0.8, 0.8),
         #           )
         # )
#plt.ylabel("Changed area ($\mathrm{m^2}$)",font1)
#plt.ylabel(" $ \times $ ",font1)
# plt.xticks([0, 1,  2.5,  5],[0, 'bad', 2.5,  5],fontproperties = 'Arial', size = 20)
# plt.yticks([0, 1,  2.5,  5],[0, 'bad', 2.5,  5],fontproperties = 'Arial', size = 20)
plt.legend(loc = 0, prop=font_legend, edgecolor="k")
#plt.grid(linestyle='-')
#plt.savefig('aaa.png', bbox_inches='tight')
plt.tight_layout()
plt.show()
print("plot success!")
