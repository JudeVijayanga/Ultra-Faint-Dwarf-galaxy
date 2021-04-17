import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ou = pd.read_csv("editCANES.csv")
ou2 = pd.read_csv("editHERCU.csv")
ou3 = pd.read_csv("editLEO.csv")
ou4 = pd.read_csv("editUMA.csv")

x1=ou.F606W-ou.F814W
y1=ou.F606W

x2=ou2.F606W-ou2.F814W
y2=ou2.F606W

x3=ou3.F606W-ou3.F814W
y3=ou3.F606W

x4=ou4.F606W-ou4.F814W
y4=ou4.F606W

fig,axs = plt.subplots(2,2)

fig.suptitle('Color Magnitude Diagrams of UFDG')

axs[0][0].scatter(x1,y1,marker="x",color='g',label="CANES")
axs[0][0].set_xlim(0,1.2)
axs[0][0].set_ylim(17,28)
axs[0][0].legend()
axs[0][0].set_xlabel("V-I")
axs[0][0].set_ylabel('I')
axs[0][0].invert_yaxis()
axs[0][0].grid(True)

axs[0][1].scatter(x2,y2,marker="x",color='grey',label="HERCU")
axs[0][1].set_xlim(0,1.2)
axs[0][1].set_ylim(17,28)
axs[0][1].legend()
axs[0][1].set_xlabel("V-I")
axs[0][1].set_ylabel('I')
axs[0][1].invert_yaxis()
axs[0][1].grid(True)

axs[1][0].scatter(x3,y3,marker="x",color='red',label="LEO")
axs[1][0].set_xlim(0,1.2)
axs[1][0].set_ylim(17,28)
axs[1][0].legend()
axs[1][0].set_xlabel("V-I")
axs[1][0].set_ylabel('I')
axs[1][0].invert_yaxis()
axs[1][0].grid(True)

axs[1][1].scatter(x4,y4,marker="x",color='blue',label="UMA")
axs[1][1].set_xlim(0,1.2)
axs[1][1].set_ylim(17,28)
axs[1][1].legend()
axs[1][1].set_xlabel("V-I")
axs[1][1].set_ylabel('I')
axs[1][1].grid(True)
axs[1][1].invert_yaxis()


fig.tight_layout()
plt.savefig("Ultra_faint_DG.pdf",density='500')

plt.show()
