for h in A B C D E F G H I L M N O P Q R S T U V
do
sbatch --job-name=urqmd_2_76_$h run_urqmd_dNdeta_pp_2_760.bash 2760_pp n$h "LHC"
done
