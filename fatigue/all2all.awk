{
  i[NR] = $1
  n[NR] = $2
  MB[NR] = $3
  S[NR] = $4
}
function abs(v) {return v < 0 ? -v : v}
END {
  N = NR
  for (i_A = 1; i_A <= N; i_A++) {
    for (i_B = i_A; i_B <= N; i_B++) {
      if (i_A != i_B) {
        printf("%d\t%d\t%d\t%d\t%.6f\t%.6f\n", i[i_A], i[i_B], n[i_A], n[i_B], abs(MB[i_A]-MB[i_B]), abs(S[i_A]-S[i_B]));
      }
    }
  }
}
