for h in A B C D E F G H I J K L M N O P Q R S T U V X Y Z a b c d e f g h i l m n o p q r s t u v x y z
do
sbatch --job-name=urqmd_PbPb_$h run_urqmd_5TeV_beginning.bash $h LHC
sleep 1
done
