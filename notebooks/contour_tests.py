# %%
from IPython import get_ipython

# %%
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('test.csv')
n = len(df)

#df.iloc[0:n,:]
#df1 = df.sort_values('Concentration', axis = 0, ascending = True)
#df2 = df.sort_values('Temperature', axis = 0, ascending = True)

mapping = {(x, y): z for (x, y, z) in df[["Concentration", "Temperature", "Resistance"]].values}

mat = np.zeros((n, n))

conc = df['Concentration']
temp = df['Temperature']

#tt = []
for i, x in np.ndenumerate(conc):
    for j, y in np.ndenumerate(temp):
        mat[j, i] = mapping.get((x, y), 0)  
       

#print(mat)

get_ipython().run_line_magic('matplotlib', 'inline')

#min(conc), max(conc), min(temp), max(temp)
levels = np.linspace(0, 10)
img = plt.contourf(finalmat, extent = [min(conc), max(conc), max(temp), min(temp)], levels = levels, cmap = 'RdYlGn')
#plt.grid()
bounds = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#pylab.colorbar(ticks = bounds)

plt.colorbar(img, ticks = bounds, label = 'Chemical Resistance')
#plt.clim(0,10)
plt.xlabel('Concentration (vol%)', fontsize = 12.0)
plt.ylabel('Temperature (C)', fontsize = 12.0)





