# state file generated using paraview version 5.4.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1167, 806]
renderView1.AnnotationColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesLabelColor = [0.0, 0.0, 0.0]
renderView1.OrientationAxesOutlineColor = [0.0, 0.0, 0.0]
renderView1.CenterOfRotation = [-440.75, 1136.49999986703, -291.0]
renderView1.StereoType = 0
renderView1.CameraPosition = [2522.8338271678986, -1680.1692974188416, 463.5519005142727]
renderView1.CameraFocalPoint = [3118.301779084614, -348.9894477358489, 108.40033838894121]
renderView1.CameraViewUp = [0.09699044050851355, 0.21583190705586397, 0.9716014832978557]
renderView1.CameraParallelScale = 1475.1994993228
renderView1.Background = [1.0, 1.0, 1.0]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.YTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.GridColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.XLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.YLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
legacyVTKReader1 = LegacyVTKReader(FileNames=['./results/mech-9-0000.vtk'])

# create a new 'Clip'
clip1 = Clip(Input=legacyVTKReader1)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'T']
clip1.Value = 259.189
clip1.Crinkleclip = 1

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Normal = [0.0, 1.0, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'T'
tLUT = GetColorTransferFunction('T')
tLUT.RGBPoints = [50.0, 0.0, 0.0, 1.0, 310.0, 1.0, 0.0, 0.0]
tLUT.ColorSpace = 'HSV'
tLUT.NanColor = [0.498039215686, 0.498039215686, 0.498039215686]
tLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'T'
tPWF = GetOpacityTransferFunction('T')
tPWF.Points = [50.0, 0.0, 0.5, 0.0, 310.0, 1.0, 0.5, 0.0]
tPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from clip1
clip1Display = Show(clip1, renderView1)
# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.AmbientColor = [0.0, 0.0, 0.0]
clip1Display.ColorArrayName = ['POINTS', 'T']
clip1Display.LookupTable = tLUT
clip1Display.OSPRayScaleArray = 'T'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'u-v-w'
clip1Display.ScaleFactor = 227.300000026594
clip1Display.SelectScaleArray = 'T'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'T'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = tPWF
clip1Display.ScalarOpacityUnitDistance = 35.6475921808239
clip1Display.GaussianRadius = 169.57000122070315
clip1Display.SetScaleArray = ['POINTS', 'T']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'T']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.GridColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]

# show color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for tLUT in view renderView1
tLUTColorBar = GetScalarBar(tLUT, renderView1)
tLUTColorBar.Orientation = 'Horizontal'
tLUTColorBar.WindowLocation = 'AnyLocation'
tLUTColorBar.Position = [0.29522203956441645, 0.15889630168942506]
tLUTColorBar.Title = 'T'
tLUTColorBar.ComponentTitle = ''
tLUTColorBar.TitleColor = [0.168627450980392, 0.184313725490196, 0.384313725490196]
tLUTColorBar.TitleFontFamily = 'Times'
tLUTColorBar.LabelColor = [0.172549019607843, 0.184313725490196, 0.384313725490196]
tLUTColorBar.LabelFontFamily = 'Times'
tLUTColorBar.LabelFormat = '%-0.2f'
tLUTColorBar.AddRangeLabels = 0
tLUTColorBar.RangeLabelFormat = '%-0.2f'
tLUTColorBar.ScalarBarLength = 0.3299999999999997

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(legacyVTKReader1)
# ----------------------------------------------------------------
