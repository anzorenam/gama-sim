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

dir='gamma_spectrum'
phs_ground=np.zeros(6)
m=0
Nevent=0
Nphoton=0
photons=np.zeros([6,200000])
eprim=np.zeros(200000)
for k in range(0,4):
  name='{0}/DAT00000{1}'.format(dir,k+1)
  f=corsikaio.CorsikaParticleFile(name)
  for shower in f:
    eprim[Nevent]=shower.header['total_energy']
    parts=shower.particles
    Nevent+=1
    if np.size(parts)==1.0:
      photons[0,Nphoton]=parts['px']
      photons[1,Nphoton]=parts['py']
      photons[2,Nphoton]=parts['pz']
      photons[4,Nphoton]=(1.0/100.0)*parts['y']
      photons[3,Nphoton]=(1.0/100.0)*parts['x']
      Nphoton+=1
  f.close()
print(Nphoton,Nevent)

photons[5,:]=1000.0*np.sqrt(photons[0,:]**2.0+photons[1,:]**2.0+photons[2,:]**2.0)
ebins=np.arange(10,2000,10)
fig,ax=plt.subplots(nrows=1,ncols=1,sharex=False,sharey=False)
ax.hist(photons[5,:],bins=ebins)
plt.xscale('log')
plt.yscale('log')
fig,ax=plt.subplots(nrows=1,ncols=1,sharex=False,sharey=False)
ax.hist2d(photons[3,:],photons[4,:],bins=50)
plt.show()
