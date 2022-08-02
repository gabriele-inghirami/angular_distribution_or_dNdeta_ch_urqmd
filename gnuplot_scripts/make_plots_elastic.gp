set term pos eps col enh font "Helvetica, 22" 

set xlabel "{/Symbol q}_{cm} [{/Symbol \260}]"
set ylabel "P({/Symbol q})"

set format y "10^{%L}"

set ls 1 lc "orange" dt 1 lw 4
set ls 2 lc "forest-green" dt 1 lw 4
set ls 3 lc "blue" dt 1 lw 4
set ls 4 lc "dark-red" dt 1 lw 4

f(x) = x*90/acos(0)
g(x) = x*acos(0)/90

set mytics 10

set logscale y

set mxtics 10

set xrange [0:2.0]

set key right center

set title "UrQMD 3.4, pp collision, elastic interactions, baryons"

set out "probability_distributions_elastic_forward.eps"

plot "200_elastic.dat" u (f($1)):(g($3)) w l ls 1 title "200 GeV"


set out "probability_distributions_elastic_backward.eps"

set xrange [178:180]

set key left center

plot "200_elastic.dat" u (f($1)):(g($3)) w l ls 2 title "200 GeV"
