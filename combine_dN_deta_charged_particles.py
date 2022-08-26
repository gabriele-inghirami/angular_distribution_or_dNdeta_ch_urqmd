# Gabriele Inghirami - g.inghirami -A T- gsi.de - 2022 - License: PUBLIC DOMAIN

import math
import numpy as np
import os
import sys

if(len(sys.argv)<4):
   print('Syntax: ./combine_dN_deta_charged_particles.py <output file> <input file 1> <input file 2> [input file 3] ... [input file n]\n')
   sys.exit(2)

outfile = sys.argv[1]
infile = sys.argv[2]
infiles = sys.argv[3:]

eta_list = []
dN_list = []

with open(infile,"r") as ff:
    events = int(ff.readline().split()[2])
    deta = float(ff.readline().split()[2])
    ff.readline() 
    for line in ff:
        eta_val, dN_val = np.float64(line.split())
        eta_list.append(eta_val)
        dN_list.append(dN_val*deta*events)

eta = np.array(eta_list)
dN = np.array(dN_list)
total_events = events

for f in infiles:
    print("Opening "+f)
    with open(f,"r") as ff:
        events = int(ff.readline().split()[2])
        ff.readline() 
        ff.readline() 
        h = 0
        for line in ff:
           dN[h] += np.float64(line.split()[1])*deta*events
           h += 1
        total_events += events

# output
fileout = open(outfile,"w")
fileout.write("# events: "+str(total_events)+"\n")
fileout.write("# deta: "+str(deta)+"\n")
fileout.write("# eta    dN/deta\n")
for i in range(eta.size):
    fileout.write("{:5.2f}".format(eta[i])+"  "+"{:8.2f}".format(dN[i]/(total_events*deta))+"\n")
fileout.close()
