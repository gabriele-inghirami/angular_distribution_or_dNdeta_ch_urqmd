set term pos eps col enh font "Helvetica, 22"

set xlabel "{/Symbol h}"
set ylabel "dN/d{/Symbol h}"

set xrange [-5:5]

set key bottom center

set out "dNdeta_Au_200GeV_comparison.eps"

set title "Au+Au at {/Symbol \326}s_{NN} = 200 GeV, 0-5% centrality, charged particles"

plot "expdata.dat" u 1:4 w p ps 1.2 pt 5 lc "black" t "Experiment", "dNdeta_urqmd.dat" w p pt 7 ps 1.2 lc "red" t "UrQMD", "dNdeta_smash.dat" w p pt 13 ps 1.2 lc "blue" t "SMASH"
