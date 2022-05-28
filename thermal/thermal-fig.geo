Merge "../thermal.geo";
Merge "../thermal.msh";

General.Trackball = 1;
General.TrackballQuaternion0 = 0.560736077210193;
General.TrackballQuaternion1 = 0.1177079489684888;
General.TrackballQuaternion2 = 0.1601270516028969;
General.TrackballQuaternion3 = 0.8037905310524137;

General.TranslationX = 19.30409268310939;
General.TranslationY = -55.92397664017634;

s = 1.33;
General.ScaleX = s;
General.ScaleY = s;
General.ScaleZ = s;



General.AxesFormatX = "%.0f";
General.AxesFormatY = "%.0f";
General.AxesFormatZ = "%.0f";
General.AxesLabelX = "x";
General.AxesLabelY = "y";
General.AxesLabelZ = "z";
General.Axes = 1;
General.AxesAutoPosition = 0;
General.AxesMinX = 0;
General.AxesMinY = 0;
General.AxesMinZ = 0;
General.AxesMaxX = 400;
General.AxesMaxY = 300;
General.AxesMaxZ = 300;

General.SmallAxes = 0;

Mesh.SurfaceEdges = 0;
Mesh.SurfaceFaces = 0;
Mesh.VolumeEdges = 1;
Mesh.VolumeFaces = 1;
Geometry.Points = 0;
Geometry.Lines = 1;
General.Color.Axes = {0,0,1};
Mesh.Color.Lines = {0,0,1};


//Mesh.Clip = 1;
//General.ClipOnlyDrawIntersectingVolume = 0;
//General.ClipOnlyVolume = 0;
//General.ClipWholeElements = 1;

Mesh.ColorCarousel = 2;
Mesh.Color.Zero = {255,120,0};
Mesh.Color.One = {220,220,180};
Mesh.Color.Two = {80,160,180};


//Print "thermal-mesh.svg";
Print "thermal-mesh.png";
Exit;
