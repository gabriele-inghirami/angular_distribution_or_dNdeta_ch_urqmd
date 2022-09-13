for h in B C D E F G H I J K L M N O P Q R S T U V X Y Z
#for h in A 
do
sbatch --job-name=urqmd_PbPb_$h run_urqmd_5TeV_beginning.bash $h LHC
sleep 1
done
