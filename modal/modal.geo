Merge "../mech.geo";

Field[5] = Box;
Field[5].XMin = -1e4;
Field[5].XMax = +1e4;
Field[5].YMin = -1e4;
Field[5].YMax = +1e4;
Field[5].ZMin = -1e4;
Field[5].ZMax = 150;

Field[5].VIn = lc_pipe;
Field[5].VOut = lc_actuator;
Field[5].Thickness = lc_actuator;

Background Field = 5;

Mesh.Optimize = 1;
Mesh.OptimizeNetgen = 1;
Mesh.HighOrderOptimize = 0;
