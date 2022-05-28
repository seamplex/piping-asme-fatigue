from paraview.simple import *

LoadState("ax.pvsm")

GetRenderView().ViewSize = [1200,1000]
GetRenderView().Background = [1,1,1]
Render()
WriteImage("ax.png")
