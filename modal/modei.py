# state file generated using paraview version 5.8.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.8.0
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1216, 829]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [-1031.1100463867188, -431.0, 251.32000732421875]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-4541.192746213876, -3888.0303254373875, 3371.048731683073]
renderView1.CameraFocalPoint = [5085.026408567042, 3284.254072333063, -4540.900366014429]
renderView1.CameraViewUp = [0.4342655248625403, 0.33815874092433895, 0.8349024612805549]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1607.6114155509583
renderView1.CameraParallelProjection = 1
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
mode10000vtk = LegacyVTKReader(FileNames=['results/mode1-0000.vtk'])

# create a new 'Warp By Vector'
warpByVector1 = WarpByVector(Input=mode10000vtk)
warpByVector1.Vectors = ['POINTS', 'u_v_w']
warpByVector1.ScaleFactor = 1e6

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from warpByVector1
warpByVector1Display = Show(warpByVector1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'u_v_w'
u_v_wLUT = GetColorTransferFunction('u_v_w')
u_v_wLUT.RGBPoints = [2.3138280019266772e-07, 0.182591, 0.312249, 0.0, 0.02326785319705406, 0.264758, 0.381138, 0.0878313, 0.04808662342894028, 0.365461, 0.467957, 0.21076, 0.0729053936608265, 0.47128, 0.562476, 0.33476, 0.09772436166759697, 0.577033, 0.65732, 0.461526, 0.1225431318994832, 0.676429, 0.744229, 0.585735, 0.14736190213136938, 0.762578, 0.814287, 0.700202, 0.17218067236325557, 0.82839, 0.858225, 0.796812, 0.19699952763834205, 0.866783, 0.86682, 0.866745, 0.2218184106019123, 0.873345, 0.837327, 0.901572, 0.2466371808337985, 0.852219, 0.771315, 0.90763, 0.2714559510656847, 0.806935, 0.678992, 0.886227, 0.2962747212975709, 0.742071, 0.570213, 0.842918, 0.3210934915294571, 0.662741, 0.454332, 0.784263, 0.3459124595362276, 0.575165, 0.339335, 0.717723, 0.3707312297681138, 0.486469, 0.230957, 0.651243, 0.39555, 0.404088, 0.131038, 0.592767]
u_v_wLUT.ColorSpace = 'Lab'
u_v_wLUT.NanColor = [0.3725490196078431, 0.2, 0.5019607843137255]
u_v_wLUT.Discretize = 0
u_v_wLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'u_v_w'
u_v_wPWF = GetOpacityTransferFunction('u_v_w')
u_v_wPWF.Points = [2.3138280019266772e-07, 0.0, 0.5, 0.0, 0.39555, 1.0, 0.5, 0.0]
u_v_wPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
warpByVector1Display.Representation = 'Surface'
warpByVector1Display.ColorArrayName = ['POINTS', 'u_v_w']
warpByVector1Display.LookupTable = u_v_wLUT
warpByVector1Display.OSPRayScaleArray = 'u_v_w'
warpByVector1Display.OSPRayScaleFunction = 'PiecewiseFunction'
warpByVector1Display.SelectOrientationVectors = 'u_v_w'
warpByVector1Display.ScaleFactor = 526.2015371
warpByVector1Display.SelectScaleArray = 'None'
warpByVector1Display.GlyphType = 'Arrow'
warpByVector1Display.GlyphTableIndexArray = 'None'
warpByVector1Display.GaussianRadius = 26.310076855
warpByVector1Display.SetScaleArray = ['POINTS', 'u_v_w']
warpByVector1Display.ScaleTransferFunction = 'PiecewiseFunction'
warpByVector1Display.OpacityArray = ['POINTS', 'u_v_w']
warpByVector1Display.OpacityTransferFunction = 'PiecewiseFunction'
warpByVector1Display.DataAxesGrid = 'GridAxesRepresentation'
warpByVector1Display.PolarAxes = 'PolarAxesRepresentation'
warpByVector1Display.ScalarOpacityFunction = u_v_wPWF
warpByVector1Display.ScalarOpacityUnitDistance = 167.7847240626333

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
warpByVector1Display.ScaleTransferFunction.Points = [-0.0457902, 0.0, 0.5, 0.0, 0.39555, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
warpByVector1Display.OpacityTransferFunction.Points = [-0.0457902, 0.0, 0.5, 0.0, 0.39555, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(warpByVector1)
# ----------------------------------------------------------------
