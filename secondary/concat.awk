BEGIN {
 t = 0;
 n = 1;
 last_t = 0;
}
{
 if (n != $1) {
  n = $1;
  t += last_t+1;
  print t-1,0 >> "transient-sep.dat"
  print t,1   >> "transient-sep.dat"
  print t+1,0 >> "transient-sep.dat"
 }
 last_t = $2;
 $1 = $2 + t;
 $2 = n;
 print $0;
}
