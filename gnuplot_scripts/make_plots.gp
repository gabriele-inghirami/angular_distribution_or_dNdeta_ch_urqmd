set term pos eps col enh font "Helvetica, 22" size 14,5

u200="200.dat"
u900="900.dat"
u2760="2760.dat"
u7000="7000.dat"

sd="jan_h_smash_data/"
s200=sd."angular_smash_sqrts-200.dat"
s900=sd."angular_smash_sqrts-200.dat"
s2760=sd."angular_smash_sqrts-2760.dat"
s7000=sd."angular_smash_sqrts-7000.dat"

p200=sd."angular_pythia_sqrts-200.dat"
p900=sd."angular_pythia_sqrts-200.dat"
p2760=sd."angular_pythia_sqrts-2760.dat"
p7000=sd."angular_pythia_sqrts-7000.dat"

set key top center font ",14"

set out "probability_distributions.eps"

set xlabel "[{/Symbol q}]_{cm} {/Symbol \260}"
set ylabel "P({/Symbol q})"

set format y "10^{%L}"

set ls 1 lc "orange" dt 1 lw 4
set ls 2 lc "forest-green" dt 1 lw 4
set ls 3 lc "blue" dt 1 lw 4
set ls 4 lc "dark-red" dt 1 lw 4
set ls 5 lc "orange" dt 2 lw 4
set ls 6 lc "forest-green" dt 2 lw 4
set ls 7 lc "blue" dt 2 lw 4
set ls 8 lc "dark-red" dt 2 lw 4
set ls 9 lc "orange" dt 3 lw 4
set ls 10 lc "forest-green" dt 3 lw 4
set ls 11 lc "blue" dt 3 lw 4
set ls 12 lc "dark-red" dt 3 lw 4

f(x) = x*90/acos(0)
g(x) = x*acos(0)/90

set multiplot layout 1, 2 title "pp collisions, UrQMD 3.4 (BB->strings), SMASH 2.2 (hard strings) and Pythia, P({/Symbol q}) comparison"

set mytics 10

set logscale y

set xtics (0,30,60,90,120,150,180)

set title "Baryons"

plot u200 u (f($1)):(g($3)) w l ls 1 title "UrQMD, 200 GeV x  1", \
     s200 u 1:2 w l ls 5 title "SMASH, 200 GeV x 1", \
     p200 u 1:2 w l ls 9 title "PYTHIA, 200 GeV x 1", \
     u900 u (f($1)):(g($3)*10) w l ls 2 title "UrQMD, 900 GeV x 10",\
     s900 u 1:(($2)*10) w l ls 6 title "SMASH, 900 GeV x 10", \
     p900 u 1:(($2)*10) w l ls 10 title "PYTHIA, 900 GeV x 10", \
     u2760 u (f($1)):(g($3)*100) w l ls 3 title "UrQMD, 2760 GeV x 10^2",\
     s2760 u 1:(($2)*100) w l ls 7 title "SMASH, 2760 GeV x 10^2", \
     p2760 u 1:(($2)*100) w l ls 11 title "PYTHIA, 2760 GeV x 10^2", \
     u7000 u (f($1)):(g($3)*1000) w l ls 4 title "UrQMD, 7000 GeV x 10^3", \
     s7000 u 1:(($2)*1000) w l ls 8 title "SMASH, 7000 GeV x 10^3", \
     p7000 u 1:(($2)*1000) w l ls 12 title "PYTHIA, 7000 GeV x 10^3" \

unset ylabel

set title "Mesons"

plot u200 u (f($1)):(g($5)) w l ls 1 title "UrQMD, 200 GeV x  1", \
     s200 u 1:3 w l ls 5 title "SMASH, 200 GeV x 1", \
     p200 u 1:3 w l ls 9 title "PYTHIA, 200 GeV x 1", \
     u900 u (f($1)):(g($5)*10) w l ls 2 title "UrQMD, 900 GeV x 10",\
     s900 u 1:(($3)*10) w l ls 6 title "SMASH, 900 GeV x 10", \
     p900 u 1:(($3)*10) w l ls 10 title "PYTHIA, 900 GeV x 10", \
     u2760 u (f($1)):(g($5)*100) w l ls 3 title "UrQMD, 2760 GeV x 10^2",\
     s2760 u 1:(($3)*100) w l ls 7 title "SMASH, 2760 GeV x 10^2", \
     p2760 u 1:(($3)*100) w l ls 11 title "PYTHIA, 2760 GeV x 10^2", \
     u7000 u (f($1)):(g($5)*1000) w l ls 4 title "UrQMD, 7000 GeV x 10^3", \
     s7000 u 1:(($3)*1000) w l ls 8 title "SMASH, 7000 GeV x 10^3", \
     p7000 u 1:(($3)*1000) w l ls 12 title "PYTHIA, 7000 GeV x 10^3" \

unset multiplot
