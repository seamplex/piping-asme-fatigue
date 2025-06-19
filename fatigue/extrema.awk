function abs(v) {return v < 0 ? -v : v}
{
  # leemos MB, S y el numero de ciclos en funcion del indice i
  MB[$1] = $5
  S[$1] = $8
  n[$1] = $10

  eps = 0.01
}
END {
  i = 0
  printf("%d\t%d\t%.4g\t%.4g\t%s\n", i, n[i], MB[i], S[i], "minmax");
  lastMB = MB[1];
  for (i = 2; i < NR-2; i++) {
    max = (MB[i]-lastMB)>eps && (MB[i]-MB[i+1])>eps;
    min = (lastMB-MB[i])>eps && (MB[i+1]-MB[i])>eps;
    left = (MB[i]-lastMB)>eps;
    right = (MB[i+1]-MB[i])>eps;
    if ((max || min) && left != right) {
      printf("%d\t%d\t%.4g\t%.4g\t%s\n", i, n[i], MB[i], S[i], (left==1)?"max":"min");
    }
    if (abs(MB[i+1]-MB[i]) > 0.5*eps) {
      lastMB = MB[i];
    }
  }
  printf("%d\t%d\t%.4g\t%.4g\t%s\n", i, n[i], MB[i], S[i], "minmax");
}
