set preamble "\usepackage{amsmath}"

set width 12*unit(cm) 
set size ratio 0.25

set axis x arrow nomirrored
set axis y arrow nomirrored
ifelse(xxx,1,set key above, unset key)

set yrange [0:11.5]
set y2range [0:280]
set y2tics 100

set grid x1 y1y2

set terminal pdf
set output "pt-xxx.pdf"

ifelse(xxx,4,set xlabel  "Time~$t$ [seg]")

set y1label "Pressure~$p$ [MPa]"
set y2label "Temperature~$T$ [C]"

# set xrange [0:t2-t1-dt]
plot \
     "pt-xxx.dat" u 1:2 w lp lt 1 lw 2 pt 16 color dandelion  axes x1y2 ti "ifelse(xxx,1,`Temperature $T(t)$')",\
     "pt-xxx.dat" u 1:3 w lp lt 1 lw 2 pt 17 color navyblue   axes x1y1 ti "ifelse(xxx,1,`Pressure $p(t)$')"
