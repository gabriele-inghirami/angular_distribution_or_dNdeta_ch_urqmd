#!/usr/bin/bash
#SBATCH --output=sl_%x_%j
#SBATCH --partition=main
#SBATCH --account=hyihp
#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --mem-per-cpu=2G
#SBATCH --cpus-per-task=1
#SBATCH --time=0-7:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=inghirami@fias.uni-frankfurt.de

iterations=1

workdir=$LH/pp_collisions/

udir=$workdir/urqmd-3.4

rundir=$workdir/$SLURM_JOB_NAME

infile_template=inputfile$1

if [ ! -d $rundir ]
then
    cp -R $udir $rundir
    cd $rundir
    make lhc
    #make 
    urqmd_exe=urqmd.$(uname -m).lhc 
    #urqmd_exe=urqmd.$(uname -m) 
fi

for k in $(seq 1 $iterations)
do
    for i in $(seq 1 $SLURM_NTASKS)
    do
        rnds=$(printf %d 0x$(xxd -l 3 -ps -c 10 /dev/urandom))
        infile=in_$i\_$k
	cp $infile_template $infile
        export ftn09=$infile
        sed -i -e "s/rsd 0/rsd $rnds/" $infile
        export ftn14=out_$i\_$k.f14
        ./$urqmd_exe &

    done
    wait
done
sleep 20
