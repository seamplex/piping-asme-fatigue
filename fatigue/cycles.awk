{
  i_A = $1
  i_B = $2
  if (n[i_A] == "") {
    n[i_A] = $3
  }
  if (n[i_B] == "") {
    n[i_B] = $4
  }
  MB = $5
  S = $6

  if (n[i_A] > 0 && n[i_B] > 0) {
    if (i_A < i_B) {
      printf("%d\t%d\t%d\t%d\t%d\t%g\t%g\n", ++k, i_A, i_B, n[i_A], n[i_B], MB, S);
    } else {
      printf("%d\t%d\t%d\t%d\t%d\t%g\t%g\n", ++k, i_B, i_A, n[i_B], n[i_A], MB, S);
    }
  }

  deltan = (n[i_A] < n[i_B]) ? n[i_A] : n[i_B]
  n[i_A] -= deltan
  n[i_B] -= deltan
}
