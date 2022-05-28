divert(-1)dnl
include(../scls.m4)dnl
include(../forloop.m4)dnl
divert(0)dnl
# vtk DataFile Version 2.0
Stress Classification Lines
ASCII
DATASET POLYDATA
POINTS eval(2*n_scls) double
esyscmd(`feenox scl-vtk.fee')
LINES n_scls eval(3*n_scls)
forloop(i, 1, n_scls, `2 eval(i-1) eval(i-1+n_scls)
')
POINT_DATA eval(2*n_scls)
SCALARS SCLs double
LOOKUP_TABLE default
forloop(i, 1, n_scls, i
)forloop(i, 1, n_scls, i
)
