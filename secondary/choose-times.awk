BEGIN {
 getline
 if (f == 0) f = 2
 if (dt0 == 0) dt0 = 10
 if (maxdt == 0) maxdt = 64*dt0
 dt = dt0
 t = $1
 print t
}

{
 t_next = $1
 while ((t += dt) < t_next) {
   print t
   dt *= f
   if (dt > maxdt) dt = maxdt
 }
 print t_next
 t = t_next
 dt = dt0
}
