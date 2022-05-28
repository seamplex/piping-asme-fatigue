Merge "temp-1.msh";

General.Trackball = 1;
General.TrackballQuaternion0 = 0.6095625110330368;
General.TrackballQuaternion1 = -0.1852332028226192;
General.TrackballQuaternion2 = -0.2299264918558048;
General.TrackballQuaternion3 = 0.735701035786993;


General.TranslationX = -40.55205048826141;
General.TranslationY = 13.86817501914351;
General.TranslationZ = 0;

s = 1.35;
General.ScaleX = s;
General.ScaleY = s;
General.ScaleZ = s;

Mesh.SurfaceEdges = 0;
Mesh.VolumeEdges = 0;

View[0].ShowElement = 0; // Show element boundaries?
View[0].RangeType = 2; // Value scale range type (1: default, 2: custom, 3: per time step)
View[0].CustomMax = 250; // User-defined maximum value to be displayed
View[0].CustomMin = 40; // User-defined minimum value to be displayed

View[0].TimeStep = 80; // Current time step displayed

Print "thermal-dist.png";
Exit;
