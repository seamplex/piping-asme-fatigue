include(`../forloop.m4')dnl
include(`n_modes.m4')dnl
READ_MESH modes.msh DIMENSIONS 3 {
forloop(`i', `1', n_modes, `READ_FUNCTION u`'i  READ_FUNCTION v`'i  READ_FUNCTION w`'i
')
}

FUNCTION sx(freq) FILE spectrum-x.dat
FUNCTION sy(freq) FILE spectrum-y.dat
FUNCTION sz(freq) FILE spectrum-z.dat

FUNCTION f(i) FILE modes.dat COLUMNS 1 2

ax(x,y,z) := { sqrt(
forloop(`i', `1', n_modes, `+(sx(`'i`')*u`'i`'(x,y,z))^2
') ) }
ay(x,y,z) := { sqrt(
forloop(`i', `1', n_modes, `+(sy(`'i`')*v`'i`'(x,y,z))^2
') ) }
az(x,y,z) := { sqrt(
forloop(`i', `1', n_modes, `+(sz(`'i`')*w`'i`'(x,y,z))^2
') ) }

WRITE_MESH seismic.msh ax ay az
WRITE_MESH seismic.vtk VECTOR ax ay az
