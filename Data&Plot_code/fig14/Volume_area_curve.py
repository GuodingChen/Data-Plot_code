# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 10:05:34 2020

Code for: plot the relationships between the landslide volume and area

    
@author: Guoding Chen
"""
import numpy as np

import matplotlib
# import math
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
# from scipy.stats import gaussian_kde
# from scipy.stats import kde
# import mpl_scatter_density
import xlrd
matplotlib.use('Qt5Agg')
# set the family font 
font1={'family':'Arial',
     'style':'normal',
    'weight':'normal',
     'size':20}
font_legend={'family':'Arial',
     'style':'normal',
    'weight':'normal',
     'size':15}
font_addTEXT={'family':'Arial',
     'style':'normal',
    'weight':'normal',
     'size':13}
font_order={'family':'Arial',
     'style':'normal',
    'weight':'normal',
     'size':20}
# read the data from the excel 

date = xlrd.open_workbook('./volume_area.xlsx')
table=date.sheets()[0]
# PF min
Area_PF_min = [i for i in table.col_values(0) if isinstance(i, (int, float))]
Volume_PF_min = [i for i in table.col_values(1) if isinstance(i, (int, float))]

# PF_max
Area_PF_max = [i for i in table.col_values(2) if isinstance(i, (int, float))]
Volume_PF_max = [i for i in table.col_values(3) if isinstance(i, (int, float))]

# PF_low
Area_PF_low = [i for i in table.col_values(4) if isinstance(i, (int, float))]
Volume_PF_low = [i for i in table.col_values(5) if isinstance(i, (int, float))]

# PF_Moderate
Area_PF_Moderate = [i for i in table.col_values(6) if isinstance(i, (int, float))]
Volume_PF_Moderate = [i for i in table.col_values(7) if isinstance(i, (int, float))]

# PF_High
Area_PF_High = [i for i in table.col_values(8) if isinstance(i, (int, float))]
Volume_PF_High = [i for i in table.col_values(9) if isinstance(i, (int, float))]

# PF_VeryHigh
Area_PF_VeryHigh = [i for i in table.col_values(10) if isinstance(i, (int, float))]
Volume_PF_VeryHigh = [i for i in table.col_values(11) if isinstance(i, (int, float))]

# translate the list to array

Area_PF_min = np.array(Area_PF_min)
Volume_PF_min = np.array(Volume_PF_min)
Area_PF_max = np.array(Area_PF_max)
Volume_PF_max = np.array(Volume_PF_max)
Area_PF_low = np.array(Area_PF_low)
Volume_PF_low = np.array(Volume_PF_low)
Area_PF_Moderate = np.array(Area_PF_Moderate)
Volume_PF_Moderate = np.array(Volume_PF_Moderate)
Area_PF_High = np.array(Area_PF_High)
Volume_PF_High = np.array(Volume_PF_High)
Area_PF_VeryHigh = np.array(Area_PF_VeryHigh)
Volume_PF_VeryHigh = np.array(Volume_PF_VeryHigh)







# set the figure size


fig = plt.figure(num=1,figsize=(11, 6))
plt.style.use('seaborn')
# plt.style.use('fivethirtyeight')
#fig.text(0.5, 0, "Landslide Area, $ A_L~(m^2)$", ha='center', fontdict = font1)
fig.text(0, 0.5, "Landslide Volume, $ V_L~(m^3)$", va='center', rotation='vertical',
          fontdict = font1)

# plot the PF_min------------------------------
plt.subplot(2,3,1)
# Area_fit = np.linspace(0, 90000, num = 500)
Volume_PF_minFit = 285.5 * pow(Area_PF_min, 0.6865) 
Volume_PF_minFitDown = 256.1 * pow(Area_PF_min, 0.6771)
Volume_PF_minFitUp = 314.8 * pow(Area_PF_min, 0.6959)

# expert curves
Volume_expert_min_Guzzetti = 0.074 * pow(Area_PF_min, 1.450) # Guzzetti,2009
Volume_expert_min_Imaizumi = 0.39 * pow(Area_PF_min, 1.31) # Imaizumi and Sidle (2007)
Volume_expert_min_Abele = 0.242 * pow(Area_PF_min, 1.307) # Abele (1974)
# Volume_expert_low_Whitehouse = 0.769 * pow(Area_PF_min, 1.250) # Whitehouse (1983)
Volume_expert_min_Haflidason = 12.273 * pow(Area_PF_min, 1.047) # Haflidason et al. (2005)


plt.fill_between(Area_PF_min, Volume_PF_minFitDown, Volume_PF_minFitUp, 
                 color='C2',   alpha=0.3)

Fit_curve = plt.plot(Area_PF_min, Volume_PF_minFit, color="C2", linewidth = 2, linestyle='-')
Guzzetti_curve = plt.plot(Area_PF_min, Volume_expert_min_Guzzetti, color="C1", linewidth = 2, linestyle='-')
Abele_curve = plt.plot(Area_PF_min, Volume_expert_min_Abele, color="C1", linewidth = 2, linestyle=':')
Haflidason_curve = plt.plot(Area_PF_min, Volume_expert_min_Haflidason, color="C1", linewidth = 2, linestyle='--')
Imaizumi_curve = plt.plot(Area_PF_min, Volume_expert_min_Imaizumi, color="C1", linewidth = 2, linestyle='-.')
# plt.plot(Area_PF_min, Volume_expert_low_Whitehouse, color="C1", linewidth = 2, linestyle='-')



fig.legend([Fit_curve, Guzzetti_curve, Abele_curve, Haflidason_curve, Imaizumi_curve],              # List of the line objects
           labels= ["This work", "Guzzetti et al. (2009)", "Imaizumi and Sidle (2007)",
                    "Abele (1974)", "Haflidason et al. (2005)"],       # The labels for each line
                 # Position of the legend
           bbox_to_anchor=(0.1, 1),
           loc="upper left",  
           borderaxespad=0.1,         # Add little spacing around the legend box
           ncol = 3,   # Title for the legend
           prop = font_legend)      




plt.scatter(Area_PF_min, Volume_PF_min, s = 15, color='k', marker='.')

plt.xlim((0, 90000)) 
plt.ylim((0, 1600000))
x_ticks=np.linspace(0, 100000 ,5)
y_ticks=np.linspace(0, 1600000, 5)


plt.xticks(x_ticks, fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, fontproperties = 'Arial', size = 20)
plt.xticks(x_ticks,
           ['0', '2.5', '5', '7.5', '10'],
           fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, 
           ['0','0.4','0.8','1.2','1.6'],
           fontproperties = 'Arial', size = 20)
plt.text(88000, 0, r'$ \times 10^4 $', fontdict = font_addTEXT)
plt.text(0, 1600000, r'$ \times 10^6 $', fontdict = font_addTEXT)

plt.text(2000, 1400000, '(a)', fontdict = font_order)

# plt.xlabel("Landslide Area, $ A_L~(m^2)$", font1)
# plt.ylabel("Landslide Volume, $ V_L~(m^3)$",font1)


# plot the PF_max------------------------------
plt.subplot(2,3,4)
Volume_PF_maxFit = 146.4 * pow(Area_PF_max, 0.7659)
Volume_PF_maxFitDown = 126.1 * pow(Area_PF_max, 0.7533)
Volume_PF_maxFitUp = 166.6 * pow(Area_PF_max, 0.7785)
 # expert curve

Volume_expert_max_Guzzetti = 0.074 * pow(Area_PF_max, 1.450) # Guzzetti,2009
Volume_expert_max_Imaizumi = 0.39 * pow(Area_PF_max, 1.31) # Imaizumi and Sidle (2007)
Volume_expert_max_Abele = 0.242 * pow(Area_PF_max, 1.307) # Abele (1974)
# Volume_expert_low_Whitehouse = 0.769 * pow(Area_PF_min, 1.250) # Whitehouse (1983)
Volume_expert_max_Haflidason = 12.273 * pow(Area_PF_max, 1.047) # Haflidason et al. (2005)



plt.fill_between(Area_PF_max, Volume_PF_maxFitDown, Volume_PF_maxFitUp, 
                 color='C2',   alpha=0.3)
plt.plot(Area_PF_max, Volume_PF_maxFit, color="C2", linewidth = 2, linestyle='-')
plt.plot(Area_PF_max, Volume_expert_max_Guzzetti, color="C1", linewidth = 2, linestyle='-')
plt.plot(Area_PF_max, Volume_expert_max_Abele, color="C1", linewidth = 2, linestyle=':')
plt.plot(Area_PF_max, Volume_expert_max_Haflidason, color="C1", linewidth = 2, linestyle='--')
plt.plot(Area_PF_max, Volume_expert_max_Imaizumi, color="C1", linewidth = 2, linestyle='-.')


plt.scatter(Area_PF_max, Volume_PF_max, s = 15, color='k', marker='.')
plt.xlim((0, 90000)) 
plt.ylim((0, 1600000))
x_ticks=np.linspace(0, 100000 ,5)
y_ticks=np.linspace(0, 1600000, 5)


plt.xticks(x_ticks, fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, fontproperties = 'Arial', size = 20)
plt.xticks(x_ticks,
           ['0', '2.5', '5', '7.5', '10'],
           fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, 
           ['0','0.4','0.8','1.2','1.6'],
           fontproperties = 'Arial', size = 20)
plt.text(88000, 0, r'$ \times 10^4 $', fontdict = font_addTEXT)
plt.text(0, 1600000, r'$ \times 10^6 $', fontdict = font_addTEXT)
plt.text(2000, 1400000, '(b)', fontdict = font_order)
# plt.xlabel("Landslide Area, $ A_L~(m^2)$", font1)
# plt.ylabel("Landslide Volume, $ V_L~(m^3)$",font1)

# plot the PF_low------------------------------

plt.subplot(2,3,2)

#plt.mpl_scatter_density(Area_PF_max, Volume_PF_max, color = 'red')
# nbins = 100
# Area_PF_low = np.array(Area_PF_low)
# Volume_PF_low = np.array(Volume_PF_low)
# k = kde.gaussian_kde([Area_PF_low, Volume_PF_low])
# xi, yi = np.mgrid[Area_PF_low.min():Area_PF_low.max():nbins*1j, 
#                   Volume_PF_low.min():Volume_PF_low.max():nbins*1j]
# zi = k(np.vstack([xi.flatten(), yi.flatten()]))
# plt.pcolormesh(xi, yi, zi.reshape(xi.shape), 
#                cmap=plt.cm.gist_earth_r, 
#                alpha = 1, edgecolors = 'none')






plt.scatter(Area_PF_low, Volume_PF_low, s = 15, color='k', marker='.')
Volume_PF_lowFit = 6.727 * pow(Area_PF_low, 1.061)
Volume_PF_lowFitDown = 5.926 * pow(Area_PF_low, 1.05)
Volume_PF_lowFitUp = 7.529 * pow(Area_PF_low, 1.072)

# expert curve

Volume_expert_low_Guzzetti = 0.074 * pow(Area_PF_low, 1.450) # Guzzetti,2009
Volume_expert_low_Imaizumi = 0.39 * pow(Area_PF_low, 1.31) # Imaizumi and Sidle (2007)
Volume_expert_low_Abele = 0.242 * pow(Area_PF_low, 1.307) # Abele (1974)
# Volume_expert_low_Whitehouse = 0.769 * pow(Area_PF_min, 1.250) # Whitehouse (1983)
Volume_expert_low_Haflidason = 12.273 * pow(Area_PF_low, 1.047) # Haflidason et al. (2005)




plt.plot(Area_PF_low, Volume_PF_lowFit, color="C2", linewidth = 2, linestyle='-')
plt.plot(Area_PF_low, Volume_expert_low_Guzzetti, color="C1", linewidth = 2, linestyle='-')
plt.plot(Area_PF_low, Volume_expert_low_Abele, color="C1", linewidth = 2, linestyle=':')
plt.plot(Area_PF_low, Volume_expert_low_Haflidason, color="C1", linewidth = 2, linestyle='--')
plt.plot(Area_PF_low, Volume_expert_low_Imaizumi, color="C1", linewidth = 2, linestyle='-.')



plt.fill_between(Area_PF_low, Volume_PF_lowFitDown, Volume_PF_lowFitUp, 
                 color='C2',   alpha=0.3)

plt.xlim((0, 90000)) 
plt.ylim((0, 1600000))
x_ticks=np.linspace(0, 100000 ,5)
y_ticks=np.linspace(0, 1600000, 5)


plt.xticks(x_ticks, fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, fontproperties = 'Arial', size = 20)
plt.xticks(x_ticks,
           ['0', '2.5', '5', '7.5', '10'],
           fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, 
           ['0','0.4','0.8','1.2','1.6'],
           fontproperties = 'Arial', size = 20)
plt.text(88000, 0, r'$ \times 10^4 $', fontdict = font_addTEXT)
plt.text(0, 1600000, r'$ \times 10^6 $', fontdict = font_addTEXT)
plt.text(2000, 1400000, '(c)', fontdict = font_order)

# plot the PF_Moderate------------------------------
plt.subplot(2,3,3)

plt.scatter(Area_PF_Moderate, Volume_PF_Moderate, s = 15, color='k', marker='.')

Volume_PF_ModerateFit = 80.29 * pow(Area_PF_Moderate, 0.8419)
Volume_PF_ModerateFitDown = 62.34 * pow(Area_PF_Moderate, 0.8211)
Volume_PF_ModerateFitUp = 98.24 * pow(Area_PF_Moderate, 0.8626)
# expert curve
Volume_expert_Moderate_Guzzetti = 0.074 * pow(Area_PF_Moderate, 1.450) # Guzzetti,2009
Volume_expert_Moderate_Imaizumi = 0.39 * pow(Area_PF_Moderate, 1.31) # Imaizumi and Sidle (2007)
Volume_expert_Moderate_Abele = 0.242 * pow(Area_PF_Moderate, 1.307) # Abele (1974)
# Volume_expert_low_Whitehouse = 0.769 * pow(Area_PF_min, 1.250) # Whitehouse (1983)
Volume_expert_Moderate_Haflidason = 12.273 * pow(Area_PF_Moderate, 1.047) # Haflidason et al. (2005)



plt.plot(Area_PF_Moderate, Volume_PF_ModerateFit, color="C2", linewidth = 2, linestyle='-')
plt.plot(Area_PF_Moderate, Volume_expert_Moderate_Guzzetti, color="C1", linewidth = 2, linestyle='-')
plt.plot(Area_PF_Moderate, Volume_expert_Moderate_Abele, color="C1", linewidth = 2, linestyle=':')
plt.plot(Area_PF_Moderate, Volume_expert_Moderate_Haflidason, color="C1", linewidth = 2, linestyle='--')
plt.plot(Area_PF_Moderate, Volume_expert_Moderate_Imaizumi, color="C1", linewidth = 2, linestyle='-.')



plt.fill_between(Area_PF_Moderate, Volume_PF_ModerateFitDown, Volume_PF_ModerateFitUp, 
                 color='C2',   alpha=0.3)






plt.xlim((0, 90000)) 
plt.ylim((0, 1600000))
x_ticks=np.linspace(0, 100000 ,5)
y_ticks=np.linspace(0, 1600000, 5)


plt.xticks(x_ticks, fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, fontproperties = 'Arial', size = 20)
plt.xticks(x_ticks,
           ['0', '2.5', '5', '7.5', '10'],
           fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, 
           ['0','0.4','0.8','1.2','1.6'],
           fontproperties = 'Arial', size = 20)
plt.text(88000, 0, r'$ \times 10^4 $', fontdict = font_addTEXT)
plt.text(0, 1600000, r'$ \times 10^6 $', fontdict = font_addTEXT)
plt.text(2000, 1400000, '(d)', fontdict = font_order)
# plot the PF_High------------------------------
plt.subplot(2,3,5)

plt.scatter(Area_PF_High, Volume_PF_High, s = 15, color='k', marker='.')

Volume_PF_HighFit = 513.4 * pow(Area_PF_High, 0.6842)
Volume_PF_HighFitDown = 333.6 * pow(Area_PF_High, 0.6519)
Volume_PF_HighFitUp = 693.2 * pow(Area_PF_High, 0.7166)

# expert curve
Volume_expert_High_Guzzetti = 0.074 * pow(Area_PF_High, 1.450) # Guzzetti,2009
Volume_expert_High_Imaizumi = 0.39 * pow(Area_PF_High, 1.31) # Imaizumi and Sidle (2007)
Volume_expert_High_Abele = 0.242 * pow(Area_PF_High, 1.307) # Abele (1974)
# Volume_expert_low_Whitehouse = 0.769 * pow(Area_PF_min, 1.250) # Whitehouse (1983)
Volume_expert_High_Haflidason = 12.273 * pow(Area_PF_High, 1.047) # Haflidason et al. (2005)


plt.plot(Area_PF_High, Volume_PF_HighFit, color="C2", linewidth = 2, linestyle='-')
plt.plot(Area_PF_High, Volume_expert_High_Guzzetti, color="C1", linewidth = 2, linestyle='-')
plt.plot(Area_PF_High, Volume_expert_High_Abele, color="C1", linewidth = 2, linestyle=':')
plt.plot(Area_PF_High, Volume_expert_High_Haflidason, color="C1", linewidth = 2, linestyle='--')
plt.plot(Area_PF_High, Volume_expert_High_Imaizumi, color="C1", linewidth = 2, linestyle='-.')





plt.fill_between(Area_PF_High, Volume_PF_HighFitDown, Volume_PF_HighFitUp, 
                 color='C2',   alpha=0.3)







plt.xlim((0, 90000)) 
plt.ylim((0, 1600000))
x_ticks=np.linspace(0, 100000 ,5)
y_ticks=np.linspace(0, 1600000, 5)


plt.xticks(x_ticks, fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, fontproperties = 'Arial', size = 20)
plt.xticks(x_ticks,
           ['0', '2.5', '5', '7.5', '10'],
           fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, 
           ['0','0.4','0.8','1.2','1.6'],
           fontproperties = 'Arial', size = 20)
plt.text(88000, 0, r'$ \times 10^4 $', fontdict = font_addTEXT)
plt.text(0, 1600000, r'$ \times 10^6 $', fontdict = font_addTEXT)
plt.text(2000, 1400000, '(e)', fontdict = font_order)

plt.xlabel("Landslide Area, $ A_L~(m^2)$", font1)

# plot the PF_VeryHigh------------------------------
plt.subplot(2,3,6)

plt.scatter(Area_PF_VeryHigh, Volume_PF_VeryHigh, s = 15, color='k', marker='.')

Volume_PF_VeryHighFit = 154.1 * pow(Area_PF_VeryHigh, 0.8059)
Volume_PF_VeryHighFitDown = 76.33 * pow(Area_PF_VeryHigh, 0.7592)
Volume_PF_VeryHighFitUp = 231.9 * pow(Area_PF_VeryHigh, 0.8525)
# expert curve
Volume_expert_VeryHigh_Guzzetti = 0.074 * pow(Area_PF_VeryHigh, 1.450) # Guzzetti,2009
Volume_expert_VeryHigh_Imaizumi = 0.39 * pow(Area_PF_VeryHigh, 1.31) # Imaizumi and Sidle (2007)
Volume_expert_VeryHigh_Abele = 0.242 * pow(Area_PF_VeryHigh, 1.307) # Abele (1974)
# Volume_expert_low_Whitehouse = 0.769 * pow(Area_PF_min, 1.250) # Whitehouse (1983)
Volume_expert_VeryHigh_Haflidason = 12.273 * pow(Area_PF_VeryHigh, 1.047) # Haflidason et al. (2005)


plt.plot(Area_PF_VeryHigh, Volume_PF_VeryHighFit, color="C2", linewidth = 2, linestyle='-')
plt.plot(Area_PF_VeryHigh, Volume_expert_VeryHigh_Guzzetti, color="C1", linewidth = 2, linestyle='-')
plt.plot(Area_PF_VeryHigh, Volume_expert_VeryHigh_Abele, color="C1", linewidth = 2, linestyle=':')
plt.plot(Area_PF_VeryHigh, Volume_expert_VeryHigh_Haflidason, color="C1", linewidth = 2, linestyle='--')
plt.plot(Area_PF_VeryHigh, Volume_expert_VeryHigh_Imaizumi, color="C1", linewidth = 2, linestyle='-.')

plt.fill_between(Area_PF_VeryHigh, Volume_PF_VeryHighFitDown, Volume_PF_VeryHighFitUp, 
                 color='C2',   alpha=0.3)




plt.xlim((0, 90000)) 
plt.ylim((0, 1600000))
x_ticks=np.linspace(0, 100000 ,5)
y_ticks=np.linspace(0, 1600000, 5)


plt.xticks(x_ticks, fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, fontproperties = 'Arial', size = 20)
plt.xticks(x_ticks,
           ['0', '2.5', '5', '7.5', '10'],
           fontproperties = 'Arial', size = 20)
plt.yticks(y_ticks, 
           ['0','0.4','0.8','1.2','1.6'],
           fontproperties = 'Arial', size = 20)
plt.text(88000, 0, r'$ \times 10^4 $', fontdict = font_addTEXT)
plt.text(0, 1600000, r'$ \times 10^6 $', fontdict = font_addTEXT)

plt.text(2000, 1400000, '(f)', fontdict = font_order)







#plt.tight_layout(pad = 5, w_pad = 1, h_pad = 1)
plt.tight_layout()
plt.show()

# fig.subplots_adjust(bottom=0.5)
print("plot success!")







