BEGIN {
 getline
 t = $1
}

{
 t_next = $1
 print t, t_next-t
 t = t_next
}

END {
  print t_next, 1
}
