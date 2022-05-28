include(../forloop.m4)
include(../scls.m4)

dnl TODO: add the whole report to the file
forloop(`i',1,n_scls,`LINEARIZE_STRESS FROM scl_xi(i) scl_yi(i) scl_zi(i) TO  scl_xf(i) scl_yf(i) scl_zf(i)   Mt M_`'i   MBt MB_`'i
')

forloop(`i', 1, scls_inox, `PRINT %.0f "M_`'i =" M_`'i "MPa < Sm =" Sm_351(T) "MPa" SEP " "
')
forloop(`i', eval(scls_inox+1), n_scls, `PRINT %.0f "M_`'i =" M_`'i "MPa < Sm =" Sm_carbon(T) "MPa" SEP " "
')

forloop(`i',1, scls_inox, `PRINT %.0f "MB_`'i =" MB_`'i "MPa < 1.5 Sm =" 1.5*Sm_351(T) "MPa" SEP " "
')
forloop(`i', eval(scls_inox+1), n_scls, `PRINT %.0f "MB_`'i =" MB_`'i " MPa < 1.5 Sm =" 1.5*Sm_carbon(T) "MPa"  SEP " "
')
