#!/usr/bin/env python3.7
# -*- coding: utf8 -*-

import matplotlib.pyplot as plt
import corsikaio
import numpy as np
import seaborn as sns
import scipy.stats as stat
import os

sns.set(rc={"figure.figsize":(8,4)})
sns.set_context('paper',font_scale=1.5,rc={'lines.linewidth':1.5})
sns.set_style('ticks')
plt.rc('text',usetex=True)
plt.rc('text.latex',preamble=r'\usepackage[utf8]{inputenc} \usepackage[T1]{fontenc} \usepackage[spanish]{babel} \usepackage{amsmath,amsfonts,amssymb} \usepackage{siunitx}')

home=os.environ['HOME']
edir=['0.2GeV','0.5GeV','1GeV','2GeV','5GeV','10GeV']
dir='{0}/Descargas/gamma-event/gamma-sim/photons'.format(home)
phs_ground=np.zeros(6)
m=0
for e in edir:
  Nevent=0
  for k in range(0,4):
    name='{0}/{1}/DAT00000{2}'.format(dir,e,k+1)
    f=corsikaio.CorsikaParticleFile(name)
    for shower in f:
      Nevent+=1
      parts=shower.particles
      if np.size(parts)>=1.0:
        phs_ground[m]+=1.0
    f.close()
  phs_ground[m]=(1.0/Nevent)*phs_ground[m]
  m+=1
ebins=np.array([0.2,0.5,1.0,2.0,5.0,10.0])
fig,ax=plt.subplots(nrows=1,ncols=1,sharex=False,sharey=True)
ax.loglog(ebins,phs_ground)
plt.xlabel(r'Energy $\left(\si{\giga\electronvolt}\right)$',x=0.9,ha='right')
plt.ylabel(r'Attenuation')
plt.ylim(1e-5,1e0)
plt.show()
