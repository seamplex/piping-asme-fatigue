include(`../forloop.m4')dnl
include(`../scls.m4')dnl
forloop(`i', 1, n_scls, `
LINEARIZE_STRESS FROM scl_xi(i) scl_yi(i) scl_zi(i)  TO scl_xf(i) scl_yf(i) scl_zf(i) {
 MBt scl`'i_MBtr
 MB1 scl`'i_MB1
 MB2 scl`'i_MB2
 MB3 scl`'i_MB3 }
 
FILE scl`'i PATH results/scl-$1-`'i.dat MODE a
PRINT FILE scl`'i %g $1 t %.2f {
 sigmax(scl_xi(i),scl_yi(i),scl_zi(i)) sigmay(scl_xi(i),scl_yi(i),scl_zi(i)) sigmaz(scl_xi(i),scl_yi(i),scl_zi(i))
  tauxy(scl_xi(i),scl_yi(i),scl_zi(i))  tauyz(scl_xi(i),scl_yi(i),scl_zi(i))  tauzx(scl_xi(i),scl_yi(i),scl_zi(i))
 sigma1(scl_xi(i),scl_yi(i),scl_zi(i)) sigma2(scl_xi(i),scl_yi(i),scl_zi(i)) sigma3(scl_xi(i),scl_yi(i),scl_zi(i))
 scl`'i_MB1 scl`'i_MB2 scl`'i_MB3
 tresca(scl_xi(i),scl_yi(i),scl_zi(i)) scl`'i_MBtr T(scl_xi(i),scl_yi(i),scl_zi(i)) 
 %g n
}

')dnl
