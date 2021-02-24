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
     'size':15}
date = xlrd.open_workbook('./unstable_curve.xlsx')
table=date.sheets()[0]
#  displacement data
time = np.linspace(1, 25, num = 25)
rainfall_dept = [i for i in table.col_values(1) if isinstance(i, (int, float))]
Percen_Unstable = [i for i in table.col_values(2) if isinstance(i, (int, float))]
Percen_PF5 = [i for i in table.col_values(3) if isinstance(i, (int, float))]
Percen_PF10 = [i for i in table.col_values(4) if isinstance(i, (int, float))]
Percen_PF20 = [i for i in table.col_values(5) if isinstance(i, (int, float))]
Percen_PF30 = [i for i in table.col_values(6) if isinstance(i, (int, float))]
Percen_PF60 = [i for i in table.col_values(7) if isinstance(i, (int, float))]




fig = plt.figure(num=1,figsize=(10, 4))
ax1 = fig.add_subplot(111)
# plt.scatter(a[::scatter_intensity], b[::scatter_intensity], marker="o", edgecolor="black",linewidths=1,
#             color="none", label="experiment")
ax1.plot(time, Percen_Unstable, color="black", linewidth=1.8, linestyle='-', label="1")
ax1.plot(time, Percen_PF5, color="red", linewidth=1.8, linestyle='-',label="2")
ax1.plot(time, Percen_PF10, color="red", linewidth=1.8, linestyle='-',label="3")
ax1.plot(time, Percen_PF20, color="red", linewidth=1.8, linestyle='-',label="4")
ax1.plot(time, Percen_PF30, color="red", linewidth=1.8, linestyle='-',label="5")
ax1.plot(time, Percen_PF60, color="red", linewidth=1.8, linestyle='-',label="6")




# plt.scatter(analytical_t[::scatter_intensity], analytical_y[::scatter_intensity], marker="o", edgecolor="black",linewidths=1, s=60,
#                            color="none", label="Analytical solution")
plt.xlim((1, 25))
plt.ylim((0, 0.15))
x_ticks=np.linspace(1, 25 ,5)
y_ticks=np.linspace(0, 0.15, 4)
plt.xticks(x_ticks, fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, fontproperties = 'Arial', size = 20)

plt.legend(loc = 2, prop=font_legend, edgecolor="k")


# ax.tick_params(direction='out', length=6, width=2, colors='r',
#                grid_color='r', grid_alpha=0.5)
#plt.xlabel('Time Series of Rainfall, 1hr',font1)
ax1.set_ylabel("pencentage", font1)
ax1.set_xlabel("Time Series of Rainfall (1hr)", font1)

plt.xticks([4, 11, 17],['7-03 23:00', '7-04 06:00', '7-04 12:00'],fontproperties = 'Arial', size = 20)
plt.grid(linestyle='-')
#plt.savefig('aaa.png', bbox_inches='tight')
## plot 2
ax2 = ax1.twinx()
plt.ylim(0, 30)
ax2.set_ylabel('Rainfall ($mm~h^{-1}$)', font1)
y2_ticksc = np.linspace(0, 30, 4)
plt.yticks(y2_ticksc, fontproperties = 'Arial', size = 20)
#ax2.hist(rainfall_dept, bins = 100, color='blue',alpha=0.5, label="obs")
ax2.bar(time, rainfall_dept, width = 1, color = 'C0', alpha = 0.8, zorder=1)

#ax2.plot(time, rainfall_dept)
#plt.legend(loc = 0, prop=font_legend, edgecolor="k")


plt.tight_layout()
plt.show()
print("plot success!")
