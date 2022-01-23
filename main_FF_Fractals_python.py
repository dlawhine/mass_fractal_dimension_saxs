import matplotlib.pyplot as plt
params = {'text.usetex': True,
          'legend.edgecolor':'black',
          'legend.fancybox': False,
          'figure.figsize': (5.2,5.2)}
plt.rcParams.update(params)
plt.rc('text', usetex=True) #for \Small, \Huge, etc.
x = []; y = [];xfit = []; yfit = []
with open("data_A2bis_SpectreFractal_710_740.txt", "r") as data_spectre,\
        open("data_A2bis_FitFractal_710_740.txt") as data_fit:
    for line in data_spectre:
        coords = line.split()
        x.append(float(coords[0]))
        y.append(float(coords[1]))
    for line in data_fit:
        coords = line.split()
        xfit.append(float(coords[0]))
        yfit.append(float(coords[1]))
xmin = 0.001; xmax = 0.5
ymin = 0.001; ymax = 1000
fig, ax = plt.subplots()
ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax])
ax.set_xscale("log", nonpositive='clip')
ax.set_yscale("log", nonpositive='clip')
ax.set_xlabel(r'$\bf{q}$' ' ' r'{\bf{(\AA}}' r'$\bf{^{-1}}$' r'\bf{)}', fontsize=14)
ax.set_ylabel(r'$\bf{Intensity\ (kDa.g.L^{-1})}$', fontsize=14)
ax.grid(visible=None, which='both', axis='both',alpha=0.4)
ax.tick_params(axis='both', which='major', labelsize=12)
#ax.set_axisbelow(True)
ax.plot([0.0046,0.0046],[0.001,1000],linestyle=':',color='red', zorder=5)
ax.plot([0.0403,0.0403],[0.001,1000],linestyle=':',color='red', zorder=5)
ax.scatter(x,y,marker='x',color='black',s=20, linewidths=0.5, zorder=10,
           label=r'\small{\bf{Large aggregates}}')
ax.plot(xfit,yfit,linewidth=1.2,linestyle='-',color='red', zorder=15,
        label=r'\small{\bf{Mass fractal model}}' ' ' r'\footnotesize{\bf{($\xi$}=217'r'\bf{\AA}}' 
        ', '  r'$\bf{r_{0}}=49$'r'\bf{\AA}'
        ', ' r'\bf{D}=2.68' ', ' r'$\bf{\chi}^{2}$=0.16'r'\bf{)}')
ax.legend(loc='lower left', borderaxespad=0, bbox_to_anchor=(0.0, 1.02,1.0,0.2),mode='expand',
          ncol=1,fontsize = 10)
plt.text(0.002, 0.1, r'${\bf{Guinier}}$' '\n' r'$\bf{region}$' '\n'  r'${\bf{q<1/\xi}}$',
         ha='center', va='center',fontsize=12)
plt.text(0.015, 0.1, r'${ \bf{Fractal}}$' '\n' r'$\bf{region}$' '\n'  r'${\bf{1/\xi<q<2/r_{0}}}$',
         ha='center', va='center',fontsize=12)
plt.text(0.12, 2.5, r'${ \bf{Asymptotic}}$' '\n' r'$\bf{region}$' '\n'  r'${\bf{q>2/r_{0}}}$',
         ha='center', va='center',fontsize=12)
plt.text(0.015, 50, r'$\bf{q^{-D}}$',
         ha='center', va='center',fontsize=12)

plt.savefig("main_FF_Fractals_python.pdf", bbox_inches='tight',dpi=300)
plt.show()

