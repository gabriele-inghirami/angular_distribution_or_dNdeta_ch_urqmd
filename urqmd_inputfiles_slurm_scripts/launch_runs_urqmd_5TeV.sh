for h in A B C D E F G H I J K L M N O P Q R S T
do
sbatch --job-name=urqmd_pPb_$h run_urqmd_5TeV.bash pPb $h LHC
sleep 1
sbatch --job-name=urqmd_PbPb_$h run_urqmd_5TeV.bash PbPb $h LHC
sleep 1
done
