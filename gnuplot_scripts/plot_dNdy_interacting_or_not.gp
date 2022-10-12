set term pos eps col enh font "Helvetica, 22"
set out "dNdy_interacting_or_not.eps"

set xlabel "y (rapidity)"
set ylabel "dN/dy"

set title "Pb+Pb, {/Symbol \326}s_{NN} = 5.02 TeV, b=0, t = 0.5 fm"

fo = "out_PbPb_urqmd_new.txt"

set key center center font ",18"

set mytics 2
set mxtics 10

set xrange [-5:5]

plot fo u 1:2 w l lw 3 dt 1 lc "red" t "interacting", fo u 1:3 w l lw 3 dt 1 lc "blue" t "non interacting"
