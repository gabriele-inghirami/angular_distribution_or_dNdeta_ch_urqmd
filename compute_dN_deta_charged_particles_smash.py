# Gabriele Inghirami - g.inghirami -A T- gsi.de - 2022 - License: PUBLIC DOMAIN

import math
import numpy as np
import os
import sys

maxe = 5.
de = 0.2
ne = int(2*maxe/de+1)
eta = np.linspace(-maxe,maxe,num=ne)
top_abs_eta = eta[-1] + de/2
dNdeta_buffer = np.zeros(ne,dtype=np.float64)
dNdeta = np.zeros(ne,dtype=np.float64)
events = 0
tot_events = 0

if(len(sys.argv)<3):
   print('Syntax: ./compute_dN_deta.py <output file> <input file 1> [input file 2] ... [input file n]\n')
   sys.exit(2)

outfile = sys.argv[1]
infiles = sys.argv[2:]

for f in infiles:
    print("Opening "+f)
    with open(f,"r") as datei:
        events = 0
        try:
            for i in range(3):
                datei.readline() #we skip the first 3 lines
        except:
            continue
        while(True):
            try:
                n_items = int(datei.readline().split()[4])
            except:
                break
            try:
                dNdeta_buffer[:]=0
                for i in range(n_items):
                    stuff = datei.readline().split()
                    #print(stuff[11])
                    if (stuff[11] != "0"): 
                        px, py, pz = np.float64(stuff[6:9])
                        p = math.sqrt(px**2+py**2+pz**2)
                        if (p == pz):
                            continue
                        eta_hadron = 0.5 * math.log( ( p + pz ) / ( p - pz ) )
                        #print(str(eta_hadron))
                        if abs(eta_hadron) >= top_abs_eta:
                            continue
                        h = int(math.floor((eta_hadron + top_abs_eta)/de)) # it's - (-top_abs_eta)
                        dNdeta_buffer[h]+=1
                if (i == n_items-1):
                    check_event = int(datei.readline().split()[2])
                    if events != check_event:
                        print("Event number mismatching in "+f+". Expected: "+str(events)+", found: "+str(check_event))
                        break
                    events+=1
                    #print(str(events))
                    dNdeta+=dNdeta_buffer
            except:
                break
        tot_events += events

# output
fileout = open(outfile,"w")
fileout.write("# events: "+str(tot_events)+"\n")
fileout.write("# deta: "+str(de)+"\n")
fileout.write("# eta    dN/deta\n")
for i in range(eta.size):
    fileout.write("{:5.2f}".format(eta[i])+"  "+"{:8.2f}".format(dNdeta[i]/(tot_events*de))+"\n")
fileout.close()
