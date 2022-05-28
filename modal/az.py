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
renderView1.ViewSize = [1010, 829]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [-1031.1100463867188, -431.0, 251.32000732421875]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-6883.880861593258, -4153.755152270835, 2243.6739048063296]
renderView1.CameraFocalPoint = [1686.0214883057863, 107.60308174250386, 46.66082038541059]
renderView1.CameraViewUp = [0.19800645799238106, 0.10428486427142399, 0.9746374247263453]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 3075.289696300858
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
seismicvtk = LegacyVTKReader(FileNames=['/home/gtheler/seamplex/writing/nafems_case/modal/seismic.vtk'])

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from seismicvtk
seismicvtkDisplay = Show(seismicvtk, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'ax_ay_az'
ax_ay_azLUT = GetColorTransferFunction('ax_ay_az')
ax_ay_azLUT.AutomaticRescaleRangeMode = 'Never'
ax_ay_azLUT.RGBPoints = [0.0, 1.0, 0.988235, 0.968627, 0.06, 1.0, 0.952941, 0.878431, 0.15000000000000002, 0.968627, 0.905882, 0.776471, 0.30000000000000004, 0.94902, 0.898039, 0.647059, 0.44999999999999996, 0.901961, 0.878431, 0.556863, 0.6000000000000001, 0.847059, 0.858824, 0.482353, 0.75, 0.690196, 0.819608, 0.435294, 0.8999999999999999, 0.513725, 0.768627, 0.384314, 1.0499999999999998, 0.337255, 0.721569, 0.337255, 1.2000000000000002, 0.278431, 0.658824, 0.392157, 1.35, 0.231373, 0.639216, 0.435294, 1.5, 0.203922, 0.6, 0.486275, 1.6500000000000001, 0.172549, 0.568627, 0.537255, 1.7999999999999998, 0.141176, 0.517647, 0.54902, 1.9500000000000002, 0.133333, 0.458824, 0.541176, 2.0999999999999996, 0.12549, 0.396078, 0.529412, 2.2500000000000004, 0.117647, 0.321569, 0.521569, 2.4000000000000004, 0.121569, 0.258824, 0.509804, 2.55, 0.133333, 0.227451, 0.501961, 2.7, 0.145098, 0.192157, 0.490196, 2.8499999999999996, 0.188235, 0.164706, 0.470588, 3.0, 0.258824, 0.196078, 0.439216]
ax_ay_azLUT.ColorSpace = 'Lab'
ax_ay_azLUT.NanColor = [0.25, 0.0, 0.0]
ax_ay_azLUT.ScalarRangeInitialized = 1.0
ax_ay_azLUT.VectorComponent = 2
ax_ay_azLUT.VectorMode = 'Component'

# get opacity transfer function/opacity map for 'ax_ay_az'
ax_ay_azPWF = GetOpacityTransferFunction('ax_ay_az')
ax_ay_azPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
ax_ay_azPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
seismicvtkDisplay.Representation = 'Surface'
seismicvtkDisplay.ColorArrayName = ['POINTS', 'ax_ay_az']
seismicvtkDisplay.LookupTable = ax_ay_azLUT
seismicvtkDisplay.OSPRayScaleArray = 'ax_ay_az'
seismicvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
seismicvtkDisplay.SelectOrientationVectors = 'ax_ay_az'
seismicvtkDisplay.ScaleFactor = 526.2
seismicvtkDisplay.SelectScaleArray = 'None'
seismicvtkDisplay.GlyphType = 'Arrow'
seismicvtkDisplay.GlyphTableIndexArray = 'None'
seismicvtkDisplay.GaussianRadius = 26.310000000000002
seismicvtkDisplay.SetScaleArray = ['POINTS', 'ax_ay_az']
seismicvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
seismicvtkDisplay.OpacityArray = ['POINTS', 'ax_ay_az']
seismicvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
seismicvtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
seismicvtkDisplay.PolarAxes = 'PolarAxesRepresentation'
seismicvtkDisplay.ScalarOpacityFunction = ax_ay_azPWF
seismicvtkDisplay.ScalarOpacityUnitDistance = 187.5363574834021

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
seismicvtkDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1993, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
seismicvtkDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1993, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for ax_ay_azLUT in view renderView1
ax_ay_azLUTColorBar = GetScalarBar(ax_ay_azLUT, renderView1)
ax_ay_azLUTColorBar.Orientation = 'Horizontal'
ax_ay_azLUTColorBar.WindowLocation = 'AnyLocation'
ax_ay_azLUTColorBar.Position = [0.3655445544554455, 0.14113389626055486]
ax_ay_azLUTColorBar.Title = 'Equivalent acceleration in z'
ax_ay_azLUTColorBar.ComponentTitle = '[g]'
ax_ay_azLUTColorBar.TitleFontFamily = 'Times'
ax_ay_azLUTColorBar.LabelFontFamily = 'Times'
ax_ay_azLUTColorBar.RangeLabelFormat = '%-#6.1f'

# set color bar visibility
ax_ay_azLUTColorBar.Visibility = 1

# show color legend
seismicvtkDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(seismicvtk)
# ----------------------------------------------------------------