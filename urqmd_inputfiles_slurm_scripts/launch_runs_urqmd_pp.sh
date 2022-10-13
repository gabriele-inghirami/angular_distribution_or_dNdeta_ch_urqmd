for k in $(seq 1 10)
do
for h in 200 900 2760 7000
do
sbatch --job-name=urqmd_$h\_$k run_simulations.bash $h
done
done
