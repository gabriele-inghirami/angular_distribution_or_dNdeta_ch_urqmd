set term pos eps col enh font "Helvetica, 22"

set xlabel "{/Symbol h}"
set ylabel "dN/d{/Symbol h}_{ch}"

set xrange [-3.5:3.5]
set yrange [0:8]

set mxtics 2
set mytics 2

set key top center font ",18"

set out "dNdeta_pp_urqmd.eps"

plot "res7000.dat" w l lt 1 lw 3 lc "dark-red" t "7 TeV", "res2760.dat" w l lt 1 lw 3 lc "blue" t "2.76 TeV", "res900.dat" w l lt 1 lw 3 lc "forest-green" t "900 GeV", "res200.dat" w l lt 1 lw 3 lc "orange" t "200 GeV"
