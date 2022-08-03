import math
import numpy as np
import os
import sys

# Copyright (2022) Gabriele Inghirami (inghirami(a T)gsi.de) (modifications)
# Copyright (2022) Jan Hammelmann (hammelmann(a T)fias.uni-frankfurt.de) (original code)

# LICENSE: GPLv3

# This script takes in input an UrQMD .f15 collision file and it prints in
# output a text file with the angular probability distribution of emitted
# baryon and mesons for string and elastic interactions.
# Only the very first interaction in each event is considered.


class ANALYSIS:
    def __init__(self, inputfile, outputfile):
        """ 
        15: BB -> 2 strings
        19: elastic
        """

        self.sigma_tots = ["0.5178E+02", "0.6779E+02", "0.8344E+02", "0.9880E+02"]
        self.ProcList = [15]
        #self.ProcList = [15, 19]
        #self.ProcList = [19]
        self.ProcNames = {15 : "Strings", 19 : "Elastic"}
        #self.softstring_number = np.arange(41, 46, 1)
        self.ProcNev = {key: 0 for key in self.ProcList}
        
        self.n_theta = 50
        self.theta_max = np.pi
        self.dtheta = self.theta_max/self.n_theta
        self.theta_bins = np.linspace(0.+self.dtheta/2, self.theta_max-self.dtheta/2, self.n_theta)

        self.Proc_theta_Meson_Hist = {key: np.zeros(self.n_theta) for key in self.ProcList}
        self.Proc_theta_Baryon_Hist = {key: np.zeros(self.n_theta) for key in self.ProcList}

        self.inputfile = inputfile
        self.outfile = outputfile 

    def BaryonNumber(self, pid):        
        # baryon
        if ((pid > 0) and (pid <= 55)): 
            B = 1
        # anti-baryon
        elif ((pid < 0) and (pid >= -55)):
            B = -1
        # meson
        else:
            B = 0
        return B


    # these functions are copied from the analysis suite
    def abs3(self, p):
        "given a 4-vector p, determine the absolute value of its spatial 3-vector"
        return math.sqrt(p[1]**2 + p[2]**2 + p[3]**2)

    def get_theta(self, p):
        "determine the polar angle theta of a 4-vector p"
        pabs = self.abs3(p)
        if (pabs>0):
            return math.acos(p[3]/pabs)
        else:
            return 0.

    def read_oscar_data(self):
        Nint = 0
        interaction_type = 0
        incoming, outgoing = [], []
        infile = open(inputfile, "r")
        for line in infile:
            line = line.split()
            if ((len(line) == 9) and (line[0] == "-1")):
                # this is a new event, we read the first line
                line = infile.readline().split()
                sigma_tot = line[6]
                interaction_type = int(line[2])
                if not (interaction_type in self.ProcList and (sigma_tot in self.sigma_tots)):
                    continue
                incoming, outgoing = [], []
                N_incoming = int(line[0])
                N_outgoing = int(line[1])
                for i in range(N_incoming):
                    incoming.append(infile.readline().split())
                for i in range(N_outgoing):
                    outgoing.append(infile.readline().split())
                
                # only care about very initial reaction
                # only consider pp collisions
                Nint += 1
                # update event number
                self.ProcNev[interaction_type] += 1
                # incoming particles
                #p1 = np.array([float(incoming[0][5]), float(incoming[0][6]), float(incoming[0][7]), float(incoming[0][8])])
                #p2 = np.array([float(incoming[1][5]), float(incoming[1][6]), float(incoming[1][7]), float(incoming[1][8])])
                    
                for particle in outgoing:
                    pid = int(particle[10])
                    baryon_number = self.BaryonNumber(pid)
                    p_f = np.array([float(particle[5]), float(particle[6]), float(particle[7]), float(particle[8])])
                    theta = self.get_theta(p_f)
                    idx_theta = int( theta / self.dtheta )
                    # sometimes we can have almost exactly pi angle emission
                    if (idx_theta == self.n_theta):
                        idx_theta -= 1
                    if abs(baryon_number) > 0:
                        self.Proc_theta_Baryon_Hist[interaction_type][idx_theta] += 1
                    elif abs(baryon_number) == 0:
                        self.Proc_theta_Meson_Hist[interaction_type][idx_theta] += 1

            
        write_out = open(self.outfile, "w")
        write_out.write("# ")
        # write header
        for key in self.ProcList:
            write_out.write(self.ProcNames[key] + "(" + '{:2d}'.format(key) + ") Baryons\t "+self.ProcNames[key] + "(" + '{:2d}'.format(key) + ") Mesons\t")
            if self.ProcNev[key] == 0:
                continue
            self.Proc_theta_Baryon_Hist[key] = self.Proc_theta_Baryon_Hist[key] / (self.ProcNev[key])
            self.Proc_theta_Meson_Hist[key] = self.Proc_theta_Meson_Hist[key] / (self.ProcNev[key])
        write_out.write("\n")
        sum_baryons = {key: self.Proc_theta_Baryon_Hist[key].sum() for key in self.ProcList}
        sum_mesons = {key: self.Proc_theta_Meson_Hist[key].sum() for key in self.ProcList}
        for i, theta in enumerate(self.theta_bins):
            write_out.write(str(theta) + "\t") 
            for key in self.ProcList:
                write_out.write(str(self.Proc_theta_Baryon_Hist[key][i]) + "\t")
                write_out.write(str(self.Proc_theta_Baryon_Hist[key][i]/(self.dtheta * sum_baryons[key])) + "\t")
                write_out.write(str(self.Proc_theta_Meson_Hist[key][i]) + "\t")
                if (sum_mesons[key] > 0): # it can be 0 in case of elastic collisions, in which the initial protons bounce back
                    write_out.write(str(self.Proc_theta_Meson_Hist[key][i]/(self.dtheta * sum_mesons[key])) + "\t")
                else:
                    write_out.write(str(0.) + "\t")
            write_out.write("\n")
        write_out.close()
        
        return 

################################################################################

inputfile = sys.argv[1]
outputfile = sys.argv[2]
RunBinary = ANALYSIS(inputfile,outputfile)
Res = RunBinary.read_oscar_data()
