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
     'size':18}
date = xlrd.open_workbook('./50_50/density_50.xlsx')
table=date.sheets()[0]
#  displacement data
density = table.col_values(0)[2:1000] 
FSR_area = table.col_values(1)[2:1000]
area_change = table.col_values(2)[2:1000]
# fit parameters

#---------plot corner line-------


#-------------fit plot---------

plt.figure(num=1,figsize=(10, 3))
#plt.scatter(FS_3d, FS_inf, marker=".", edgecolor="black",linewidths=1,
#             color="k", cmap = 'best')

# line plot 

#plt.plot(density, FSR_area, 'o', ms = 3,  color="C0", linewidth = 1.5, linestyle='-')
plt.plot(density, FSR_area, color="C0", linewidth = 2, linestyle='-', label = r"$ \Delta FSR \times area $")
plt.plot(density, area_change, color="C1", linewidth = 2, linestyle='-', label = "$ \sum Changed~pixels~area$")
#plt.plot(x_fit_2, y_fit_2, color="red", linewidth = 1.5, linestyle='-')
# plt.fill_between(x_fit, y_fit, y_fit_2, color='C1',   alpha=0.3)
# plt.fill_between(x_fit, y_fit, y_fit_3, color='C1',   alpha=0.3)
plt.xlim((0, 1000)) 
plt.ylim((0, 150000))
x_ticks=np.linspace(0, 1000 ,5)
y_ticks=np.linspace(0, 150000, 5)
plt.xticks(x_ticks, fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, fontproperties = 'Arial', size = 20)
# ax.tick_params(direction='out', length=6, width=2, colors='r',
#                grid_color='r', grid_alpha=0.5)
plt.xlabel("Ellipsoid density", font1)


plt.ylabel(r"$ Area~(\mathrm{m^2}) $",font1)
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
