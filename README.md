# Content of the repository:

## python scripts

- pp_angular_distribution_urqmd.py: python script to compute the angular distribution probability of baryons and mesons
  originating in the first string or elastic interaction in pp collisions simulated with UrQMD.
- compute_dN_deta_charged_particles_urqmd.py: python script to compute dN/deta of charged particles from UrQMD .f14 output files
- compute_dN_deta_charged_particles_smash.py: python script to compute dN/deta of charged particles from SMASH Oscar2013 particle_lists.oscar output files
- combine_dN_deta_charged_particles.py: python script that sums up two or more results of compute_dN_deta_charged_particles.py (both from UrQMD or SMASH data)
- compute_dN_deta_charged_particles_urqmd_w_limit.py: python script to compute dN/deta of charged particles from SMASH Oscar2013 particle_lists.oscar output files,
                                                      but only events with at least one charged hadron with |eta| < eta_limit are accepted
- compute_dN_dy_interacting_particles_urqmd.py: python script that computes dN/dy for interacting and non interacting (cross section scaled to 0) hadrons
- combine_dN_deta_charged_particles_w_limit.py: sums up the results produced by compute_dN_deta_charged_particles_urqmd_w_limit.py

This mini repository also contains:
- gnuplot_scripts : to plot the results
- urmqd_inputfiles_slurm_scripts : prototypes of UrQMD inputfiles and slurm scripts to run the simulations to create the data

## licenses:

- the python script pp_angular_distribution_urqmd.py is released under the GPLv3 license
- the gnuplot scripts are released as PUBLIC DOMAIN code
- the python scripts that compute and sum up dN/deta are released as public domain
