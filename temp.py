import matplotlib.pyplot as plt
a=[113,85,90,150,149,88,93,115,135,80,77,82,129]
b=[67,98,89,120,133,150,84,69,89,79,120,112,100]
plt.hist([a,b],bins=[ 60,80,100,120,140,160],label=["men","women"],color=["green","orange"],rwidth=0.9)

plt.legend()
plt.show()