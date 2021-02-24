import numpy as np

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

import xlrd


# set the family font 
font1={'family':'Arial',
     'style':'normal',
    'weight':'normal',
     'size':20}
font_legend={'family':'Arial',
     'style':'normal',
    'weight':'normal',
     'size':20}
date = xlrd.open_workbook('./discharge_plot.xlsx')
table=date.sheets()[0]
#  displacement data
time = np.linspace(1, 169, num = 169)
rainfall_dept = table.col_values(1)[1:170]
R_simulate = table.col_values(2)[1:170]
R_obs = table.col_values(3)[1:170]



fig = plt.figure(num=1,figsize=(10, 5))
ax1 = fig.add_subplot(111)
# plt.scatter(a[::scatter_intensity], b[::scatter_intensity], marker="o", edgecolor="black",linewidths=1,
#             color="none", label="experiment")
ax1.plot(time, R_obs, color="black", linewidth=1.8, linestyle='-', label="Q_obs")
ax1.plot(time, R_simulate, color="red", linewidth=1.8, linestyle='-',label="Q_simulation")

# plt.scatter(analytical_t[::scatter_intensity], analytical_y[::scatter_intensity], marker="o", edgecolor="black",linewidths=1, s=60,
#                            color="none", label="Analytical solution")
plt.xlim((1, 169))
plt.ylim((0, 1000))
x_ticks=np.linspace(1, 169 ,5)
y_ticks=np.linspace(0, 1500, 5)
#plt.xticks(x_ticks, fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, fontproperties = 'Arial', size = 20)

plt.legend(loc = 7, prop=font_legend, edgecolor="k")


# ax.tick_params(direction='out', length=6, width=2, colors='r',
#                grid_color='r', grid_alpha=0.5)
#plt.xlabel('Time Series of Rainfall, 1hr',font1)
ax1.set_ylabel("Discharge ($m^{3}s^{-1}$)", font1)
ax1.set_xlabel("Time Series of Rainfall (1hr)", font1)
plt.text(5, 300, r'NSEC = 0.77', fontdict = font1)
plt.text(5, 200, r'CC = 0.93', fontdict = font1)
plt.text(5, 100, r'Bias = 37.9%', fontdict = font1)
plt.xticks([1, 43, 85,  127, 169],['', '7-04  2:00', '7-05  20:00',  '7-07  14:00',''],fontproperties = 'Arial', size = 20)
plt.grid(linestyle='-')
#plt.savefig('aaa.png', bbox_inches='tight')
## plot 2
ax2 = ax1.twinx()
plt.ylim(50,0)
ax2.set_ylabel('Rainfall ($mm~h^{-1}$)', font1)
y2_ticksc = np.linspace(100, 0, 5)
plt.yticks(y2_ticksc, fontproperties = 'Arial', size = 20)
#ax2.hist(rainfall_dept, bins = 100, color='blue',alpha=0.5, label="obs")
ax2.bar(time, rainfall_dept, width = 1, color = 'C0', alpha = 0.8)

#ax2.plot(time, rainfall_dept)
#plt.legend(loc = 0, prop=font_legend, edgecolor="k")


plt.tight_layout()
plt.show()
print("plot success!")
