for h in A B C D E F G H I L M N O P Q
do
sbatch --job-name=urqmd_200_$h run_urqmd_dNdeta_200.bash Au_200 $h
done
