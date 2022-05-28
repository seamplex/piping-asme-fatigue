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
seismicvtk = LegacyVTKReader(FileNames=['seismic.vtk',])

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from legacyVTKReader1
legacyVTKReader1Display = Show(legacyVTKReader1, renderView1)
# trace defaults for the display properties.
legacyVTKReader1Display.Representation = 'Surface'
legacyVTKReader1Display.AmbientColor = [0.0, 0.0, 0.0]
legacyVTKReader1Display.ColorArrayName = ['POINTS', 'ax-ay-az']
legacyVTKReader1Display.LookupTable = axayazLUT
legacyVTKReader1Display.OSPRayScaleArray = 'ax-ay-az'
legacyVTKReader1Display.OSPRayScaleFunction = 'PiecewiseFunction'
legacyVTKReader1Display.SelectOrientationVectors = 'ax-ay-az'
legacyVTKReader1Display.ScaleFactor = 240.95
legacyVTKReader1Display.SelectScaleArray = 'None'
legacyVTKReader1Display.GlyphType = 'Arrow'
legacyVTKReader1Display.GlyphTableIndexArray = 'None'
legacyVTKReader1Display.DataAxesGrid = 'GridAxesRepresentation'
legacyVTKReader1Display.PolarAxes = 'PolarAxesRepresentation'
legacyVTKReader1Display.ScalarOpacityFunction = axayazPWF
legacyVTKReader1Display.ScalarOpacityUnitDistance = 87.2659132584268
legacyVTKReader1Display.GaussianRadius = 287.2685
legacyVTKReader1Display.SetScaleArray = [None, '']
legacyVTKReader1Display.ScaleTransferFunction = 'PiecewiseFunction'
legacyVTKReader1Display.OpacityArray = [None, '']
legacyVTKReader1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
legacyVTKReader1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
legacyVTKReader1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
legacyVTKReader1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
legacyVTKReader1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
legacyVTKReader1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
legacyVTKReader1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
legacyVTKReader1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
legacyVTKReader1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
legacyVTKReader1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
legacyVTKReader1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
legacyVTKReader1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(legacyVTKReader1)
# ----------------------------------------------------------------
