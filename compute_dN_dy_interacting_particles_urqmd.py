# Gabriele Inghirami - g.inghirami@gsi.de - 2022 - License: GPLv.3

import math
import numpy as np
import os
import sys

maxY = 5.
dY = 0.1
nY = int(2*maxY/dY+1)
rap = np.linspace(-maxY,maxY,num=nY)
top_abs_Y = rap[-1] + dY/2
dNdY_buffer = np.zeros((nY,2),dtype=np.float64)
dNdY = np.zeros((nY,2),dtype=np.float64)
events = 0

# index of interacting hadrons
ki = 0
# index of non interacting hadrons
kn = 1

if(len(sys.argv)<3):
   print('Syntax: ./compute_dN_dy.py <output file> <input file 1> [input file 2] ... [input file n]\n')
   sys.exit(2)

outfile = sys.argv[1]
infiles = sys.argv[2:]

for f in infiles:
    print("Opening "+f)
    with open(f,"r") as datei:
        while(True):
            try:
                for i in range(17):
                    datei.readline() #we skip the first 17 lines
            except:
                break
            try:
                n_items = int(datei.readline().split()[0])
                datei.readline() #we skip the next line
            except:
                break
            try:
                dNdY_buffer[:,:]=0
                for i in range(n_items):
                    stuff = datei.readline().split()
                    en, px, py, pz = np.float64(stuff[4:8])
                    if (en == pz):
                        continue
                    rap_hadron = 0.5 * math.log( ( en + pz ) / ( en - pz ) )
                    if abs(rap_hadron) >= top_abs_Y:
                        continue
                    if (np.float64(stuff[17]) > 0):
                        indx = ki
                    else: 
                        indx = kn
                    h = int(math.floor((rap_hadron + top_abs_Y)/dY)) # it's - (-top_abs_Y)
                    dNdY_buffer[h,indx]+=1
                if (i == n_items-1):
                    events+=1
                    print("Event: "+str(events))
                    dNdY+=dNdY_buffer
            except:
                break

# output
fileout = open(outfile,"w")
fileout.write("# events: "+str(events)+"\n")
fileout.write("# dy (rapidity): "+str(dY)+"\n")
fileout.write("# y (rapidity)       dN/dy (interacting)       dN/dy (non interacting)\n")
for i in range(rap.size):
    fileout.write("{:5.2f}".format(rap[i])+"    "+"{:8.2f}".format(dNdY[i,ki]/(events*dY))+"    "+"{:8.2f}".format(dNdY[i,kn]/(events*dY))+"\n")
fileout.close()
