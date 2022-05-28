SetFactory("OpenCASCADE");

Merge "mech.brep";

Physical Volume("pipe_cs") = {2, 9, 10, 11};
Physical Volume("pipe_ss") = {7};

Physical Volume("nozzle_cs") = {1};
Physical Volume("actuator_cs") = {3, 4, 5};
Physical Volume("valve_ss") = {6, 8};


Physical Surface("internal") = {3,8,9,11,34,106,107,112,113,117,118,119,120,123,124,125,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,147,148,150,154,155,156,158,162,163,164,166,172,173,175,176,180,187,188,189,190,191,192};

Physical Surface("tank") = {146};
Physical Surface("axial1") = {174};
Physical Surface("axial2") = {178};
Physical Surface("valve-vertical") = {114};
Physical Curve("vertical") = {322,368};
Physical Curve ("valve-horizontal") =  {27};

Mesh.Algorithm = 6;     //  (1: MeshAdapt, 2: Automatic, 5: Delaunay, 6: Frontal-Delaunay, 7: BAMG, 8: Frontal-Delaunay for Quads, 9: Packing of Parallelograms)
Mesh.Algorithm3D = 10;  //  (1: Delaunay, 4: Frontal, 7: MMG3D, 9: R-tree, 10: HXT)

Merge "lcs.geo";
Mesh.CharacteristicLengthMax = lc_actuator;
Mesh.CharacteristicLengthMin = 0.1*lc_pipe;


Field[1] = Box;
Field[1].XMin = -1e4;
Field[1].XMax = +1e4;
Field[1].YMin = -1e4;
Field[1].YMax = +1e4;
Field[1].ZMin = -1e4;
Field[1].ZMax = 150;

Field[1].VIn = lc_pipe;
Field[1].VOut = lc_actuator;
Field[1].Thickness = lc_actuator;

Field[2] = Distance;
Field[2].FacesList = {4};

Field[3] = Threshold;
Field[3].IField = 2;
Field[3].LcMin = Mesh.CharacteristicLengthMin;
Field[3].LcMax = lc_actuator;
Field[3].DistMin = 5;
Field[3].DistMax = 300;

Field[4] = Min;
Field[4].FieldsList = {1,3};
Background Field = 4;


Mesh.ElementOrder = 2;
Mesh.SecondOrderLinear = 0;

Mesh.Optimize = 1;
Mesh.OptimizeNetgen = 1;
Mesh.HighOrderOptimize = 2; // (0: none, 1: optimization, 2: elastic+optimization, 3: elastic, 4: fast curving)
